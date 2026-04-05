import streamlit as st 
import numpy as np 
from sklearn.datasets import load_iris 
from sklearn.ensemble import RandomForestClassifier 
data = load_iris() 
X = data.data 
y = data.target 
model = RandomForestClassifier() 
model.fit(X, y) 
st.title(" Iris Flower Prediction") 
sl = st.slider("Sepal Length", 4.0, 8.0, 5.0) 
sw = st.slider("Sepal Width", 2.0, 4.5, 3.0) 
pl = st.slider("Petal Length", 1.0, 7.0, 4.0) 
pw = st.slider("Petal Width", 0.1, 2.5, 1.0) 
input_data = np.array([[sl, sw, pl, pw]]) 
prediction = model.predict(input_data) 
st.write("Prediction:", data.target_names[prediction][0])