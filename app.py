import streamlit as st
import json
from chatbot import get_course_recommendations

# Load course data
with open("courses.json", "r") as f:
    course_data = json.load(f)

st.title("🎓 SmartCourseBot")
st.write("Ask me for course recommendations (e.g., 'I want to learn Python or web development').")

# User input
user_input = st.text_input("What do you want to learn today?")

# Response area
if user_input:
    response = get_course_recommendations(user_input, course_data)
    st.markdown(response)