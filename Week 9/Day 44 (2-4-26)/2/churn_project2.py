# ============================================
# CUSTOMER CHURN PREDICTION (ULTIMATE FIX)
# ============================================

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# ----------- TITLE -----------
st.title("Customer Churn Prediction System")

# ----------- LOAD DATASET -----------
data = pd.read_csv("churn prediction.csv")
st.write(data.head())

# ----------- DATA CLEANING -----------

# Drop ID column if exists
if "CustomerID" in data.columns:
    data.drop("CustomerID", axis=1, inplace=True)

# Fill missing values
data = data.ffill()

# ----------- DATE CONVERSION -----------

if "LastPurchaseDate" in data.columns:
    data['LastPurchaseDate'] = pd.to_datetime(data['LastPurchaseDate'], errors='coerce')
    data['LastPurchaseDate'] = data['LastPurchaseDate'].map(
        lambda x: x.toordinal() if pd.notnull(x) else 0
    )

# ----------- TARGET COLUMN -----------

data['Churn'] = data['Churn'].map({'Yes':1, 'No':0})

# ----------- ONE HOT ENCODING (KEY FIX) -----------

# Automatically convert ALL categorical columns
data = pd.get_dummies(data, drop_first=True)

# ----------- SPLIT -----------

X = data.drop("Churn", axis=1)
y = data["Churn"]

# ----------- SCALING -----------

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ----------- TRAIN TEST SPLIT -----------

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# ----------- MODELS -----------

models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Random Forest": RandomForestClassifier()
}

results = {}

st.header("Model Performance")

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred, zero_division=0)
    rec = recall_score(y_test, y_pred, zero_division=0)
    f1 = f1_score(y_test, y_pred, zero_division=0)

    results[name] = acc

    st.subheader(name)
    st.write(f"Accuracy: {acc:.2f}")
    st.write(f"Precision: {prec:.2f}")
    st.write(f"Recall: {rec:.2f}")
    st.write(f"F1 Score: {f1:.2f}")

# ----------- BEST MODEL -----------

best_model_name = max(results, key=results.get)
best_model = models[best_model_name]

st.success(f"Best Model: {best_model_name}")

# ----------- EDA -----------

st.header("Churn Distribution")

fig, ax = plt.subplots()
y.value_counts().plot(kind='bar', ax=ax)
ax.set_title("Churn Distribution")

st.pyplot(fig)

# ----------- PREDICTION UI -----------

st.header("Predict Churn")

inputs = []

for col in X.columns:
    val = st.number_input(f"{col}", value=0.0)
    inputs.append(val)

if st.button("Predict"):
    input_data = scaler.transform([inputs])
    prediction = best_model.predict(input_data)

    if prediction[0] == 1:
        st.error("Customer is likely to CHURN ❌")
    else:
        st.success("Customer will NOT churn ✅")