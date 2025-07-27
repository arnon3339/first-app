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
done = {"Lelouch":"sacrificed himself for world peace",
        "Itachi Uchiha":"Itachi Uchiha made the ultimate sacrifice for the greater good by eliminating his entire clan, the Uchiha, except for his younger brother Sasuke. This was done to prevent a coup d'état by the Uchiha against Konohagakure (the Hidden Leaf Village) which would have led to a devastating war. (he prevented a war)", 
              "Sorawong":"help the community and the sport industry bringing lots of events to Thailand",
        "Jesus":"healing the sick, feeding the hungry, and ultimately sacrificing himself for the salvation of humanity.", 
              "mahatma Gandhi":"advocacy of social justice and equality. His actions resulted in the end of British colonial rule in India and inspired movements for civil rights and freedom around the world. Creating a culture of peace, in proving the effectiveness of non-violent non-cooperation."}
st.write(done[option])
