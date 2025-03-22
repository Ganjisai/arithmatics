import streamlit as st
st.title('arithmatic operations')

num1=st.number_input('enter a number')
num2=st.number_input('enter another number')
operation=st.selectbox('operation',('add','subtract','multiply','divide'))
if operation=='add':
    st.write("the sum is")
    st.write(num1+num2)
elif operation=='subtract':
    st.write("the difference is")
    st.write(num1-num2)
elif operation=='multiply':
    st.write("the product is:")
    st.write(num1*num2)
elif operation=='divide':
    st.write("the division is:")
    st.write(num1/num2)
