import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.navie_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv("Titanic.csv")
df = df[['Survived', 'Pclass', 'Age', 'Fare']]
df = df.dropna()
X = df[['Pclass', 'Age', 'Fare']]
Y = df['Survived']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

#---------------------LOGISTIC REGRESSION-------------------------------
model = LogisticRegression()
model.fit(X_train, Y_train)
Y_pred = model.predict(X_test)
print("\n Logistic Regression")
print("Accuracy : ", accuracy_score(Y_test, Y_pred))
print(classification_report(Y_test, Y_pred))

#------------------------KNN-----------------------------------------
model = KNeighborsClassifier(n_neighbors = 5)
model.fit(X_train, Y_train)
Y_pred = moedel.predict(X_train)
print("KNN")
print("Accuracy : ", accuracy_score(Y_test, Y_pred))

#-----------------------SVM-------------------------------------------
model = SVC()
model.fit(X_train, Y_train)
Y_pred = model.predict(X_test)
print("\n SVM ")
print("Accuracy : ", accuracy_score(Y_test, Y_pred))\

#-----------------------------NAVIE BAYES--------------------------
model = GaussianNB()
model.fit(X_train, Y_train)
Y_pred = model.predict(X_test)
print("\n Naive Bayes ")
print("Accuracy : ", accuracy_score(Y_test, Y_pred))

#-------------------------DECISION TREE----------------------------------
model = DecisionTreeClassifier()
model.fit(X_train, Y_train)
Y_pred = model.predict(X_test)
print("\n Decision Tree ")
print("Accuracy : ", accuracy_score(Y_test, Y_pred))

#--------------------------RANDOM FOREST---------------------------------
model = RandomForestClassifier()
model.fit(X_train, Y_train)
Y_pred = model.predict(X_test)
print("\n Random Forest ")
print("Accuracy : ", accuracy_score(Y_test, Y_pred))