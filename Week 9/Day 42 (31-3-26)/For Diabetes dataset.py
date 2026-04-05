# Step 1: Import Libraries 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
# Step 2: Load Dataset 
df = pd.read_csv("diabetes.csv") 
# Step 3: Explore Data 
print(df.head()) 
print(df.columns) 
print(df.info()) 
# Step 4: Define Features and Target 
X = df.drop("Outcome", axis=1) 
y = df["Outcome"] 
# Step 5: Train-Test Split 
from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, 
random_state=42) 
# Step 6: Feature Scaling 
from sklearn.preprocessing import StandardScaler 
scaler = StandardScaler() 
X_train = scaler.fit_transform(X_train) 
X_test = scaler.transform(X_test) 
# ------------------------------- 
#  LOGISTIC REGRESSION 
# ------------------------------- 
from sklearn.linear_model import LogisticRegression 
model = LogisticRegression() 
model.fit(X_train, y_train) 
y_pred = model.predict(X_test) 
from sklearn.metrics import accuracy_score 
print("Logistic Regression Accuracy:", accuracy_score(y_test, y_pred)) 
# ------------------------------- 
#  KNN 
# ------------------------------- 
from sklearn.neighbors import KNeighborsClassifier 
model = KNeighborsClassifier(n_neighbors=5) 
model.fit(X_train, y_train) 
y_pred = model.predict(X_test) 
print("KNN Accuracy:", accuracy_score(y_test, y_pred)) 
# ------------------------------- 
#  SVM 
# ------------------------------- 
from sklearn.svm import SVC 
model = SVC() 
model.fit(X_train, y_train) 
y_pred = model.predict(X_test) 
print("SVM Accuracy:", accuracy_score(y_test, y_pred)) 
# ------------------------------- 
#  NAIVE BAYES 
# ------------------------------- 
from sklearn.naive_bayes import GaussianNB 
model = GaussianNB() 
model.fit(X_train, y_train) 
y_pred = model.predict(X_test) 
print("Naive Bayes Accuracy:", accuracy_score(y_test, y_pred)) 
# ------------------------------- 
#  DECISION TREE 
# ------------------------------- 
from sklearn.tree import DecisionTreeClassifier 
model = DecisionTreeClassifier() 
model.fit(X_train, y_train) 
y_pred = model.predict(X_test) 
print("Decision Tree Accuracy:", accuracy_score(y_test, y_pred)) 
# ------------------------------- 
#  RANDOM FOREST 
# ------------------------------- 
from sklearn.ensemble import RandomForestClassifier 
model = RandomForestClassifier() 
model.fit(X_train, y_train) 
y_pred = model.predict(X_test) 
print("Random Forest Accuracy:", accuracy_score(y_test, y_pred))