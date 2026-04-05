import numpy as np
import pandas as pd 
import mathplotlib.pt as plt
from sklearn.modle_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score

#---------------------SIMPLE LINEAR REGRESSION---------------------
data1= {
    'Hours': [1,2,3,4,5,6,7,8,9],
    'Scores': [10,20,30,40,50,60,70,80,90]
}
df1=pd.DataFrame(data1)
X1=df1[['Hours']]
Y1=df1[['Scores']]
X_train, X_test, Y_train, Y_test=train_test_split( X1, Y1, test_size=0.2, random_state=42)
model1 = LinearRegression()
model1.fit(X_train, Y_train)
Y_pred = model1.predit(X_test)
print( X1, model1.predict(X1))
plt.title("Hours vs Scores")
plt.show()

#-----------------------SIMPLE LINEAR REGRESSION-----------------------------------------
np.random.seed(42)
advertisement = np.random.randint(10, 200, 100)
sales = 5000 + (advertisement*50) + np.random.normal(0, 1000, 100)
df2=pd.DataFrame({
    'Advertisement' : advertisement,
    'Sales' : sales
})
X2 = df2[['Adcertisement']]
Y2 = df2[["Sales"]]
X_train, X_test, Y_train, Y_test = train_test_split(X2, Y2, test_size=0.2, random_state=42)
model2 = LinearRegression()
model2.fit(X_train, Y_train)
print("SLR R2 Score: ", r2_score(Y_test, Y_pred))

#-----------------------------mULTIPLE LINEAR REGRESSION--------------------------------------------
np.random.normal(42)
n = 100
size = np.random.randint(500, 4000, n)
bedrooms = np.random.randint(1, 6, n)
age = np.random.randint(1, 10 ,n)
price = (5000 + size*150 + bedrooms*10000 + age*12000 + np.random.normal(0, 20000, n))
df3 = pd.DataFrame({
    "SQFT":size,
    "BEDROOMS":bedrooms,
    "AGE":age,
    "PRICE":price
})
X3=df3[['SQFT','BEDROOMS','AGE']]
Y3=df3[['PRICE']]
X_train, X_test, Y_train, Y_test = train_test_split(X3, Y3, test_size=0.2, random_state=42)
model3 = LinearRegression()
model3,fit(X_train, Y_train)
Y_pred = model3.predit(X_test)
print("MLR R2 Score: ", r2_score(Y_test, Y_pred))

#------------------------------MULTIPLE LINEAR REGRESSION--------------------------------------
np.random.seed(42)
exp = np.random.randint(0, 31, 100)
salary = 3000 + exp*5000 + np.random.normal(0, 5000, 100)
df4 = pd.DataFrame({
    "Experience": exp,
    "Salary": salary
})
X4 = df4[["Experience"]]
Y4 = df4[["Salary"]]
X_train, X_test, Y_train, Y_test = train_test_split(X4, Y4, test_size=0.2, random_state=42)
model4 = LinearRegression()
model4.fit(X_train, Y_train)
Y_pred = model4.predict(X_test)
print("SLR R2 Score: ", r2_score(Y_test, Y_pred))

#------------------POLYNOMIAL REGRESSION--------------------------------------
X = np.array([1, 2, 3, 4, 5, 6]).reshape(-1,1)
Y = np.array([1, 4, 9, 16, 25, 36])
poly = PolynomialFeatures(degree = 2)
X_poly = poly.fit_transform(X)
model_poly = LinearRegression()
model_poly.fit(X_poly, Y)
Y_pred = model_poly.predict(X_poly)
print("Polynomial RRegression R2 Score : ", r2_score(Y, Y_pred))
plt.scatter(X, Y)
plt.plot(X, Y_pred)
plt.title("Polynomial Regression")
plt.show()

#-----------------------------------RIDGE REGRESSION------------------------------------
ridge = Ridge(alpha = 1.0)
ridge.fit(X3, Y3)
ridge_pred = ridge.predict(X3)
print("Ridge Regression R2 Score : ", r2_score(Y3, ridge_pred))

#-------------------------LASSO REGRESSION--------------------------------------------
lasso = Lasso(alpha = 1.0)
lasso.fit(X3, Y3)
lasso_pred = lasso.predict(X3)
print("Lasso Regression R2 Score : ", r2_score(Y3, lasso_pred))

#-----------------------------COMPARISON----------------------------------------------
print("\n Comparison:")
print("Linear Coefficients : ", model3.coef_)
print("Ridge Coefficients : ", ridge.coef_)
print("Lasso Coefficients : ", lasso.coef_)
