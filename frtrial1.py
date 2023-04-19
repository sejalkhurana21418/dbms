import streamlit as st

# Define some sample merchandise data
merchandise = [
    {'name': 'T-shirt', 'price': 20},
    {'name': 'Hoodie', 'price': 40},
    {'name': 'Mug', 'price': 10},
    {'name': 'Sticker', 'price': 5},
]

# Define the Streamlit app
def app():
    st.title('Merchandise Store')

    # Display the merchandise data in a table
    st.write('Here are some of our products:')
    st.table(merchandise)

    # Allow the user to select a product and quantity
    product = st.selectbox('Select a product:', [item['name'] for item in merchandise])
    quantity = st.number_input('Quantity:', min_value=1, value=1)

    # Calculate the total price based on the selected product and quantity
    total_price = next(item['price'] for item in merchandise if item['name'] == product) * quantity

    # Display the total price to the user
    st.write(f'Total price for {quantity} {product}(s): ${total_price}')

# Run the Streamlit app
if __name__ == '__main__':
    app()
