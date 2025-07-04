import streamlit as st
st.title("first project")
import streamlit as st
from datetime import time

appointment = st.slider(
    "Schedule your appointment:", value=(time(11, 30), time(12, 45))
)
st.write("You're scheduled for:", appointment)


age = st.slider("whats ur number?", 0, 130, 1000000000000)
st.write("my number is ", age,)


options = st.multiselect(
    "what is ur name?",
    ["Aaron", "Abigail", "Adam", "Adrian", "Aiden", "Alan", "Albert", "Alexa", "Alexander", "Alexandra", "Alice", "Alicia", "Allison", "Amanda", "Amber", "Amelia", "Amy", "Andrea", "Andrew", "Angela", "Anna", "Anthony", "April", "Arthur", "Ashley", "Audrey", "Austin", "Barbara", "Benjamin", "Bethany", "Beverly", "Bianca", "Blake", "Brandon", "Brenda", "Brian", "Brittany", "Brooke", "Caleb"],
    default=["Aaron", "Adam"],
)

st.write("You selected:", options)

options = st.multiselect(
    "what is ur name?",
    ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin", "Lee", "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson", "Walker"],
    default=["Smith"],
)

st.write("You selected:", options)