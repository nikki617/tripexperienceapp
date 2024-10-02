import streamlit as st
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
!streamlit run app.py
from openai import OpenAI
import os
os.environ["OPENAI_API_KEY"] = st.secrets["MyOpenAIkey"]

# Define the user input
st.header("Share with us your experience of the latest trip.")
user_input = st.text_area("")

!streamlit run app.py
# Function to handle user input
def handle_input(user_input):
    sentiment = detect_sentiment(user_input)
    if sentiment == 'negative':
        if 'airline' in user_input.lower():
            st.write("We're sorry to hear about your experience. Our customer service will contact you soon to resolve the issue or provide compensation.")
        else:
            st.write("We're sorry to hear about your experience. Unfortunately, the airline is not liable for issues beyond our control, such as weather-related delays.")
    else:
        st.write("Thank you for your feedback! We're glad you had a positive experience with us.")

# StreamLit app layout
st.title("Airline Experience Feedback")
user_input = st.text_area("Share with us your experience of the latest trip.")
if st.button("Submit"):
    handle_input(user_input)
