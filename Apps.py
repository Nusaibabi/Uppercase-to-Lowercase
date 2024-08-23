import streamlit as st

st.header('Lowercase to Uppercase Application')
a= st.text_input('Enter a text')
btn=st.button('Click')
if btn:
    b=a.upper()
    st.subheader(b)

