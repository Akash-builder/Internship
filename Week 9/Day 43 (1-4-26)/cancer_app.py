import streamlit as st 
import numpy as np 
from sklearn.datasets import load_breast_cancer 
from sklearn.ensemble import RandomForestClassifier 
data = load_breast_cancer() 
X = data.data 
y = data.target 
model = RandomForestClassifier() 
model.fit(X, y) 
st.title("🎗 Breast Cancer Prediction") 
inputs = [] 
for i, feature in enumerate(data.feature_names[:5]): 
    val = st.number_input(feature, float(X[:, i].min()), float(X[:, i].max())) 
    inputs.append(val) 
# fill remaining features with mean 
remaining = list(np.mean(X[:, 5:], axis=0)) 
inputs.extend(remaining) 
prediction = model.predict([inputs]) 
st.write("Prediction:", data.target_names[prediction][0])