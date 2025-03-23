import streamlit as st

st.title('Arithmetic Operations')

num1 = st.number_input('Enter a number', format="%.2f")
num2 = st.number_input('Enter another number', format="%.2f")
operation = st.selectbox('Operation', ('Add', 'Subtract', 'Multiply', 'Divide'))

if st.button("Calculate"):
    try:
        if operation == 'Add':
            result = num1 + num2
            st.write("The sum is:", result)
        elif operation == 'Subtract':
            result = num1 - num2
            st.write("The difference is:", result)
        elif operation == 'Multiply':
            result = num1 * num2
            st.write("The product is:", result)
        elif operation == 'Divide':
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero!")
            result = num1 / num2
            st.write("The division result is:", result)
    except ZeroDivisionError as e:
        st.error(f"Error: {e}")  
    except Exception as e:
        st.error(f"Something went wrong! {e}") 


if st.button("Continue"):
    st.experimental_rerun()
