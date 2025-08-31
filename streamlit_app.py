# https://first-app-87ehw8hgy4u.streamlit.app

# import streamlit package to source code
import streamlit as st

# show website title 
st.title("agent archives")
# enter your name to name variable 
name = st.text_input("enter your name")
# show name from name variable 
st.write(f"welcome {name}") 
# select character to option variable
option = st.selectbox(
    "select character?",
    ("Lelouch", "Itachi Uchiha", "Sorawong", "Jesus", "mahatma Gandhi"),
)
# image variable 
characters = {"Lelouch":"Picture1.png", "Itachi Uchiha":"Picture2.png", 
              "Sorawong":"Picture3.png", "Jesus":"Picture4.png", 
              "mahatma Gandhi":"Picture5.png"}
# show image variable
st.image(characters[option], width=550)
# what they have done variable 
done = {"Lelouch":"sacrificed himself for world peace",
        "Itachi Uchiha":"Itachi Uchiha made the ultimate sacrifice for the greater good by eliminating his entire clan, the Uchiha, except for his younger brother Sasuke. This was done to prevent a coup d'état by the Uchiha against Konohagakure (the Hidden Leaf Village) which would have led to a devastating war. (he prevented a war)", 
              "Sorawong":"help the community and the sport industry bringing lots of events to Thailand",
        "Jesus":"healing the sick, feeding the hungry, and ultimately sacrificing himself for the salvation of humanity.", 
              "mahatma Gandhi":"advocacy of social justice and equality. His actions resulted in the end of British colonial rule in India and inspired movements for civil rights and freedom around the world. Creating a culture of peace, in proving the effectiveness of non-violent non-cooperation."}

# show what they did for greater good
st.write("**What they did for greater good.**")
# show what they have done 
st.write(done[option])
#Job variable
Job = {"Lelouch":"leads a rebellion against the Holy Britannian Empire and becomes 99th emperor Britannian Empire.",
       "Itachi Uchiha":"Anbu captain and akaski member", 
              "Sorawong":"Minister of tourism and sports in Thailand ",
       "Jesus":"Jewish preacher and religious leader", 
              "mahatma Gandhi":"Freedom fighter, Advocate, Politition, Activist, revolutionary, Journalist, and lawyer."}
# show job title
st.write("**Job**")
# show job
st.write(Job[option])
# quote variable 
quote = {"Lelouch":"### If the king doesn't move, then his subjects won't follow.\n### The only ones who should kill, are those who are prepared to be killed.",
         "Itachi Uchiha":"### People's lives don't end when they die. It ends when they lose faith. Those who cannot acknowledge their true self eventually fail. I won't put myself above you and tell you this and that, it's too late.", 
              "Sorawong":" ",
         "Jesus":"### For God so loved the world, that he gave his only Son, that whoever believes in him should not perish but have eternal life", 
              "mahatma Gandhi":"### Be the change that you wish to see in the world.\nLive as if you were to die tomorrow. Learn as if you were to live forever."}
#show quote 
st.write(quote[option])
