import streamlit as st

st.title("agent archives")
name = st.text_input("enter your name")
st.write(f"welcome {name}") 
option = st.selectbox(
    "select character?",
    ("Lelouch", "Itachi Uchiha", "Sorawong", "Jesus", "mahatma Gandhi"),
)
characters = {"Lelouch":"Picture1.png", "Itachi Uchiha":"Picture2.png", 
              "Sorawong":"Picture3.png", "Jesus":"Picture4.png", 
              "mahatma Gandhi":"Picture5.png"}
st.image(characters[option])
