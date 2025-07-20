import streamlit as st

st.title("agent archives")
name = st.text_input("enter your name")
st.write(f"welcome {name}") 
st.selectbox(["x", "y"])
