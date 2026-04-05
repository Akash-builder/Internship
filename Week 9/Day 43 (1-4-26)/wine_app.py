import numpy as np 
from sklearn.datasets import load_wine 
from sklearn.ensemble import RandomForestClassifier 
data = load_wine() 
X = data.data 
y = data.target 
model = RandomForestClassifier() 
model.fit(X, y) 
st.title(" Wine Classification") 
inputs = [] 
for i, feature in enumerate(data.feature_names[:5]): 
    val = st.number_input(feature, float(X[:, i].min()), float(X[:, 
i].max())) 
inputs.append(val) 
remaining = list(np.mean(X[:, 5:], axis=0)) 
inputs.extend(remaining) 
prediction = model.predict([inputs]) 
st.write("Prediction:", data.target_names[prediction][0])