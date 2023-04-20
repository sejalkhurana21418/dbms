import streamlit as st


import sqlite3

#

# Establish a connection to the database
conn = sqlite3.connect.connect(
  host="127.0.0.1",
  user="root",
  password="sejal@2004",
  database="BrandedInk",
)

# Create a cursor object to execute SQL queries
cursor = conn.cursor()


import pandas as pd




# Create a function to query the database and return results as a pandas dataframe
def run_query(query):
    return pd.read_sql_query(query, conn)

# Define the Streamlit app
def app():
    st.title('Franchise Company Dashboard')
    menu = ['Product', 'Customer', 'Cart', 'Cart Products', 'Coupon', 'Orderr', 'Billing Details', 'Category', 'Franchise']
    choice = st.sidebar.selectbox('Select Entity', menu)

    # Display data for the selected entity
    if choice == 'Product':
        st.subheader('Product List')
        query = 'SELECT * FROM product'
        results = run_query(query)
        st.dataframe(results)

    elif choice == 'Customer':
        st.subheader('Customer List')
        query = 'SELECT * FROM customer'
        results = run_query(query)
        st.dataframe(results)

    elif choice == 'Cart':
        st.subheader('Cart List')
        query = 'SELECT * FROM cart'
        results = run_query(query)
        st.dataframe(results)

    elif choice == 'Cart Products':
        st.subheader('Cart Products List')
        query = 'SELECT * FROM cart_products'
        results = run_query(query)
        st.dataframe(results)

    elif choice == 'Coupon':
        st.subheader('Coupon List')
        query = 'SELECT * FROM coupon'
        results = run_query(query)
        st.dataframe(results)

    elif choice == 'Order':
        st.subheader('Order List')
        query = 'SELECT * FROM order'
        results = run_query(query)
        st.dataframe(results)

    elif choice == 'Billing Details':
        st.subheader('Billing Details List')
        query = 'SELECT * FROM billing_details'
        results = run_query(query)
        st.dataframe(results)

    elif choice == 'Category':
        st.subheader('Category List')
        query = 'SELECT * FROM category'
        results = run_query(query)
        st.dataframe(results)

    elif choice == 'Franchise':
        st.subheader('Franchise List')
        query = 'SELECT * FROM franchise'
        results = run_query(query)
        st.dataframe(results)

# Run the Streamlit app
if __name__ == '__main__':
    app()
