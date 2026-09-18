import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Simple Calculator",
    page_icon="🧮",
    layout="centered"
)

# Title
st.title("🧮 Simple Calculator")
st.write("Enter two numbers, choose an operation, and calculate the result.")

# Input numbers
number1 = st.number_input(
    "Enter the first number",
    value=0.0
)

number2 = st.number_input(
    "Enter the second number",
    value=0.0
)

# Select operation
operation = st.selectbox(
    "Choose an operation",
    ["Addition", "Subtraction", "Multiplication", "Division"]
)

# Calculate button
if st.button("Calculate", use_container_width=True):

    if operation == "Addition":
        result = number1 + number2
        st.success(f"Result: {result}")

    elif operation == "Subtraction":
        result = number1 - number2
        st.success(f"Result: {result}")

    elif operation == "Multiplication":
        result = number1 * number2
        st.success(f"Result: {result}")

    elif operation == "Division":
        if number2 == 0:
            st.error("You cannot divide by zero.")
        else:
            result = number1 / number2
            st.success(f"Result: {result}")
