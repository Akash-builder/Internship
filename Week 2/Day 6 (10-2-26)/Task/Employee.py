import streamlit as st 
import pandas as pd 
st.title("Employee Salary Filter App") 
st.header("Upload Employee CSV File") 
uploaded_file = st.file_uploader("Employee", type=["csv"]) 
if uploaded_file is not None: 
    df = pd.read_csv(uploaded_file) 
st.subheader("Full Employee Data") 
st.dataframe(df) 
st.subheader("Employees with Salary > 50,000") 
if "Salary" in df.columns: 
    filtered_df = df[df["Salary"] > 50000] 
    st.dataframe(filtered_df) 
else: 
    st.error("CSV must contain a 'Salary' column.") 
st.divider() 
st.header("Role Based Content Display") 
role = st.selectbox("Select your role:", ["Student", "Intern", "Employee", "Admin"]) 
if role == "Student": 
    st.write("Welcome Student! You can explore employee data and learn filtering concepts.") 
elif role == "Intern": 
    st.write("Welcome Intern! You can analyze employee salary data and generate insights.") 
elif role == "Employee": 
    st.write("Welcome Employee! You can check salary-based employee records.") 
elif role == "Admin": 
    st.write("Welcome Admin! You have access to all employee records and filtering options.")