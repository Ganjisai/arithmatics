import streamlit as st

st.title('Arithmetic Operations')

num1 = st.number_input('Enter a number', format="%.2f")
num2 = st.number_input('Enter another number', format="%.2f")
operation = st.selectbox('Operation', ('Add', 'Subtract', 'Multiply', 'Divide'))

if st.button("Calculate"):
    if operation == 'Add':
        st.write("The sum is:", num1 + num2)
    elif operation == 'Subtract':
        st.write("The difference is:", num1 - num2)
    elif operation == 'Multiply':
        st.write("The product is:", num1 * num2)
    elif operation == 'Divide':
        if num2 == 0:
            st.error("Division by zero is not allowed!")
        else:
            st.write("The division result is:", num1 / num2)
if st.button("Continue"):
    st.experimental_rerun()
