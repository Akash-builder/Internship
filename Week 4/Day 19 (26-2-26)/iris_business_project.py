import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# -----------------------------
# LOAD DATA
# -----------------------------
iris = load_iris()

df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["species"] = iris.target
df["species"] = df["species"].map(dict(enumerate(iris.target_names)))

df.columns = ["sepal_length", "sepal_width",
              "petal_length", "petal_width", "species"]

# -----------------------------
# KPI 1: TOTAL RECORDS
# -----------------------------
print("\n========== KPI SUMMARY ==========")
print("Total Records:", len(df))

# -----------------------------
# KPI 2: SPECIES DISTRIBUTION
# -----------------------------
species_count = df["species"].value_counts()
species_percent = df["species"].value_counts(normalize=True) * 100

print("\nSpecies Count:\n", species_count)
print("\nSpecies Percentage:\n", species_percent)

# -----------------------------
# KPI 3: AVERAGE FEATURES
# -----------------------------
print("\nAverage Feature Values by Species:\n",
      df.groupby("species").mean())

# -----------------------------
# KPI 4: CORRELATION MATRIX
# -----------------------------
corr_matrix = df.drop("species", axis=1).corr()
print("\nCorrelation Matrix:\n", corr_matrix)

# -----------------------------
# KPI 5: OUTLIER DETECTION
# -----------------------------
print("\nOutlier Summary:")

for col in df.columns[:-1]:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    outliers = df[(df[col] < lower) | (df[col] > upper)]

    print(f"{col}: {len(outliers)} outliers")

# -----------------------------
# VISUALIZATIONS
# -----------------------------

# 1. Species Distribution
fig1 = px.pie(df, names="species",
              title="Species Distribution")
fig1.show()

# 2. Boxplots
for feature in df.columns[:-1]:
    fig = px.box(df, x="species", y=feature,
                 title=f"{feature} by Species")
    fig.show()

# 3. Scatter Matrix
fig3 = px.scatter_matrix(
    df,
    dimensions=df.columns[:-1],
    color="species",
    title="Feature Relationships"
)
fig3.show()

# 4. Correlation Heatmap
fig4 = px.imshow(
    corr_matrix,
    text_auto=True,
    title="Correlation Heatmap"
)
fig4.show()

# -----------------------------
# MACHINE LEARNING MODEL
# -----------------------------
X = df.drop("species", axis=1)
y = df["species"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

model = RandomForestClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", accuracy)
print("\nClassification Report:\n",
      classification_report(y_test, y_pred))