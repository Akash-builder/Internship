import numpy as np 
from tensorflow.keras.models import load_model 
from PIL import Image 
import pickle 
from tensorflow.keras.preprocessing.sequence import pad_sequences 
st.title("Deep Learning Models Demo") 
option = st.sidebar.selectbox("Select Model", ["CNN","FNN","RNN"]) 
# CNN / FNN 
if option in ["CNN","FNN"]: 
    model = load_model(f"models/{option.lower()}_model.h5") 
    file = st.file_uploader("Upload Image") 
    if file: 
        img = Image.open(file).resize((32,32)) 
        img = np.array(img)/255.0 
        img = img.reshape(1,32,32,3) 
        pred = model.predict(img) 
        classes 
        ["airplane","car","bird","cat","deer","dog","frog","horse","ship","truck"] 
        st.image(img[0]) 
        st.write("Prediction:", classes[np.argmax(pred)]) 
# RNN 
elif option=="RNN": 
    model = load_model("models/rnn_model.h5") 
    with open("models/tokenizer.pkl","rb") as f: 
        tokenizer = pickle.load(f) 
    text = st.text_input("Enter text") 
    if st.button("Predict"): 
        seq = tokenizer.texts_to_sequences([text])[0] 
        seq = pad_sequences([seq],maxlen=5,padding='pre') 
        pred = np.argmax(model.predict(seq),axis=1) 
        for word,index in tokenizer.word_index.items(): 
            if index == pred: 
                st.write("Next word:",word)