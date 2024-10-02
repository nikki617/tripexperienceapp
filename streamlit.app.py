import streamlit as st
from langchain.chains import RoutingChain
from langchain_community import detect_sentiment

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
