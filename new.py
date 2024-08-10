import streamlit as st

# Title of the app
st.title("Simple Calculator")

# Sidebar for operation selection
st.sidebar.title("Select Operation")
operation = st.sidebar.selectbox("Choose an operation:", ["Addition", "Subtraction", "Multiplication", "Division"])

# Input fields for the numbers
st.write("Enter the numbers:")
num1 = st.number_input("First number", value=0.0)
num2 = st.number_input("Second number", value=0.0)

# Perform the calculation based on the selected operation
result = None
if operation == "Addition":
    result = num1 + num2
elif operation == "Subtraction":
    result = num1 - num2
elif operation == "Multiplication":
    result = num1 * num2
elif operation == "Division":
    if num2 != 0:
        result = num1 / num2
    else:
        st.error("Division by zero is not allowed.")

# Display the result
if result is not None:
    st.write(f"The result of {operation.lower()} is: {result}")
