import streamlit as st
import pandas as pd
import os

st.title("Inventory Management System")

FILE_NAME = "inventory.csv"

# -------------------------------
# Load Inventory
# -------------------------------
def load_inventory():
    if os.path.exists(FILE_NAME):
        return pd.read_csv(FILE_NAME)
    else:
        return pd.DataFrame(
            columns=["ProductID", "ProductName", "Category", "Price", "Stock"]
        )

# -------------------------------
# Save Inventory
# -------------------------------
def save_inventory(df):
    df.to_csv(FILE_NAME, index=False)

# Load Data
df = load_inventory()

# Sidebar Menu
st.sidebar.title("Menu")
option = st.sidebar.selectbox(
    "Select an operation:",
    [
        "View Inventory",
        "Add Product",
        "Remove Product",
        "Search Product",
        "Update Stock",
        "Total Inventory Value",
    ],
)

# -------------------------------
# VIEW INVENTORY
# -------------------------------
if option == "View Inventory":
    st.header("View Inventory")
    st.dataframe(df)

# -------------------------------
# ADD PRODUCT
# -------------------------------
elif option == "Add Product":
    st.header("Add Product")

    pid = st.number_input("Enter Product ID", min_value=1, step=1)
    pname = st.text_input("Enter Product Name")
    category = st.text_input("Enter Category")
    price = st.number_input("Enter Price", min_value=1.0, step=1.0)
    stock = st.number_input("Enter Stock", min_value=0, step=1)

    if st.button("Add Product"):
        if pid in df["ProductID"].values:
            st.error("Product ID already exists. Use a new ID.")
        elif pname.strip() == "" or category.strip() == "":
            st.error("Product Name and Category cannot be empty.")
        else:
            new_row = {
                "ProductID": pid,
                "ProductName": pname,
                "Category": category,
                "Price": price,
                "Stock": stock,
            }
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
            save_inventory(df)
            st.success("Product added successfully!")

# -------------------------------
# REMOVE PRODUCT
# -------------------------------
elif option == "Remove Product":
    st.header("Remove Product")

    pid = st.number_input("Enter Product ID to remove", min_value=1, step=1)

    if st.button("Remove Product"):
        if pid not in df["ProductID"].values:
            st.error("Product ID not found.")
        else:
            df = df[df["ProductID"] != pid]
            save_inventory(df)
            st.success("Product removed successfully!")

# -------------------------------
# SEARCH PRODUCT
# -------------------------------
elif option == "Search Product":
    st.header("Search Product")

    search_name = st.text_input("Enter Product Name to search")

    if st.button("Search"):
        result = df[
            df["ProductName"].str.contains(search_name, case=False, na=False)
        ]

        if result.empty:
            st.warning("No matching product found.")
        else:
            st.dataframe(result)

# -------------------------------
# UPDATE STOCK
# -------------------------------
elif option == "Update Stock":
    st.header("Update Stock")

    pid = st.number_input("Enter Product ID", min_value=1, step=1)
    new_stock = st.number_input("Enter New Stock Value", min_value=0, step=1)

    if st.button("Update Stock"):
        if pid not in df["ProductID"].values:
            st.error("Product ID not found.")
        else:
            df.loc[df["ProductID"] == pid, "Stock"] = new_stock
            save_inventory(df)
            st.success("Stock updated successfully!")

# -------------------------------
# TOTAL INVENTORY VALUE
# -------------------------------
elif option == "Total Inventory Value":
    st.header("Total Inventory Value")

    if df.empty:
        st.warning("Inventory is empty.")
    else:
        temp_df = df.copy()
        temp_df["TotalValue"] = temp_df["Price"] * temp_df["Stock"]
        total_value = temp_df["TotalValue"].sum()

        st.subheader("Inventory with Total Value per Product")
        st.dataframe(temp_df)

        st.subheader("Final Total Inventory Value")
        st.success(f"Total Inventory Value = {total_value}")
