import streamlit as st 
import pandas as pd 
# ------------------------------- 
# Page Title 
# ------------------------------- 
st.title("Streamlit Hands-On Assignment ") 
# ------------------------------- 
# 1) Display Name, Role, Skills 
# ------------------------------- 
st.header("1) Display Name, Role, Skills") 
 
st.write(" Name: John Doe") 
st.write(" Role: Computer Science Student") 
st.write(" Skills: Python, SQL, DSA, Java, Streamlit") 
 
st.divider() 
 
# ------------------------------- 
# 2) Take user input (Name, Age) and display using button 
# ------------------------------- 
st.header("2) User Input with Button") 
 
name = st.text_input("Enter your name:") 
age = st.number_input("Enter your age:", min_value=1, max_value=100) 
 
if st.button("Submit Details"): 
    st.success(f"Hello {name}! You are {age} years old.") 
 
st.divider() 
 
# ------------------------------- 
# 3) Checkbox to show/hide text 
# ------------------------------- 
st.header("3) Checkbox Show/Hide Text") 
 
show_text = st.checkbox("Show text") 
 
if show_text: 
    st.write(" This text is visible because checkbox is selected!") 
else: 
    st.write(" Text is hidden. Select checkbox to show it.") 
 
st.divider() 
 
# ------------------------------- 
# 4) Selectbox to choose programming language 
# ------------------------------- 
st.header("4) Selectbox - Choose a Programming Language") 
 
language = st.selectbox( 
    "Select a language:", 
    ["Python", "Java", "JavaScript", "C++", "C#"] 
) 
st.write(f" You selected: {language}") 
 
st.divider() 
 
# ------------------------------- 
# 5) Simple Counter using button 
# ------------------------------- 
st.header("5) Counter using Button") 
 
if "count" not in st.session_state: 
    st.session_state.count = 0 
 
if st.button("Increase Counter"): 
    st.session_state.count += 1 
 
st.write(" Counter Value:", st.session_state.count) 
 
st.divider() 
 
# ------------------------------- 
# 6) Display a DataFrame using Streamlit 
# ------------------------------- 
st.header("6) Display a DataFrame") 
 
data = { 
    "Name": ["H", "Raj", "Anu"], 
    "Marks": [90, 85, 88], 
    "Passed": [True, True, True] 
} 
 
df = pd.DataFrame(data) 
st.dataframe(df) 
 
st.divider() 
 
# ------------------------------- 
# 7) Upload CSV and display contents 
# ------------------------------- 
st.header("7) Upload CSV and Display Contents") 
 
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"]) 
 
if uploaded_file is not None: 
    df_uploaded = pd.read_csv(uploaded_file) 
    st.success("CSV Uploaded Successfully!") 
    st.dataframe(df_uploaded) 
 
st.divider() 
 
# ------------------------------- 
# 8) Display an Image 
# ------------------------------- 
st.header("8) Display an Image") 
 
st.image("image.jpg", caption="Displayed Image using Streamlit", 
use_container_width=True) 
 
st.divider() 
 
# ------------------------------- 
# 9) Sidebar menu with courses 
# ------------------------------- 
st.sidebar.title(" Course Menu") 
 
course = st.sidebar.selectbox( 
    "Choose a course:", 
    ["Data Science", "Full Stack Java", "Full Stack Python", "Dot Net"] 
) 
 
st.sidebar.success(f"You selected: {course}") 
 
st.header("9) Sidebar Selection Output") 
st.write(f" Selected Course: {course}") 
 
st.divider() 
 
# ------------------------------- 
# 10) Success message when button clicked 
# ------------------------------- 
st.header("10) Success Message on Button Click") 
 
if st.button("Click Me for Success Message"): 
    st.success(" Button clicked successfully! Task completed!") 
    