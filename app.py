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