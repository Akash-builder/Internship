import streamlit as st 
import numpy as np 
import pandas as pd 
import seaborn as sns 
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import StandardScaler 
from sklearn.ensemble import RandomForestClassifier 
st.title("Titanic Survival Prediction              
# ========================= 
# Load & Train Model (inside app) 
# ========================= 
@st.cache_resource 
def train_model(): 
    df = sns.load_dataset("titanic") 
    # Drop unnecessary columns 
    ") 
    df.drop(['deck', 'embark_town', 'alive', 'class', 'who'], axis=1, 
    inplace=True) 
    # Handle missing values 
    df['age'] = df['age'].fillna(df['age'].mean()) 
    df['embarked'] = df['embarked'].fillna(df['embarked'].mode()[0]) 
    # Encoding 
    df['sex'] = df['sex'].map({'male':1, 'female':0}) 
    df['embarked'] = df['embarked'].map({'S':0, 'C':1, 'Q':2}) 
    df['adult_male'] = df['adult_male'].astype(int) 
    df['alone'] = df['alone'].astype(int) 
    X = df.drop('survived', axis=1) 
    y = df['survived'] 
    X_train, X_test, y_train, y_test = train_test_split( 
    X, y, test_size=0.2, random_state=42 
    ) 
    scaler = StandardScaler() 
    X_train = scaler.fit_transform(X_train) 
    model = RandomForestClassifier()
    model.fit(X_train, y_train) 
    return model, scaler 
    model, scaler = train_model() 
# ========================= 
# User Input UI 
# ========================= 
pclass = st.selectbox("Passenger Class", [1, 2, 3]) 
sex = st.selectbox("Sex", ["Male", "Female"]) 
age = st.slider("Age", 1, 80, 25) 
sibsp = st.number_input("Siblings/Spouses aboard", 0, 10, 0) 
parch = st.number_input("Parents/Children aboard", 0, 10, 0) 
fare = st.number_input("Fare", 0.0, 600.0, 50.0) 
embarked = st.selectbox("Embarked", ["S", "C", "Q"]) 
adult_male = st.selectbox("Adult Male", ["Yes", "No"]) 
alone = st.selectbox("Alone", ["Yes", "No"]) 
# ========================= 
# Prediction 
# ========================= 
if st.button("Predict"): 
    # Encoding (same as training) 
    sex = 1 if sex == "Male" else 0 
    embarked = {"S":0, "C":1, "Q":2}[embarked] 
    adult_male = 1 if adult_male == "Yes" else 0 
    alone = 1 if alone == "Yes" else 0 
    # Feature order MUST match training 
    input_data = np.array([[pclass, sex, age, sibsp, parch, fare, embarked, 
    adult_male, alone]]) 
    # Scaling 
    input_data = scaler.transform(input_data) 
    # Prediction 
    prediction = model.predict(input_data) 
    if prediction[0] == 1: 
    st.success("Passenger Survived ") 
    else: 
    st.error("Passenger Did Not Survive ") 