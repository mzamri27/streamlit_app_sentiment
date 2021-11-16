from textblob import TextBlob
import streamlit as st
import re

@st.cache
def getPolarity(text):

    polar = TextBlob(text).sentiment.polarity

    if polar > 0.0:
        return 'Positive'
    elif polar < 0.0:
        return 'Negative'
    else:
        return 'Normal'

st.title("Sentiment Analysis Assessment")
st.write("Sentiment analysis is the process of detecting positive or negative"
"sentiment in text. It’s often used by businesses to detect sentiment in social "
"data, gauge brand reputation, and understand customers.")

st.subheader("Types of Sentiment Analysis")
st.write("""Sentiment analysis focuses on polarity (positive, negative, neutral)
 but also on feelings and emotions (angry, happy, sad, etc), urgency (urgent,
 not urgent) and even intentions (interested v. not interested).
""")

st.subheader("Try yourself!")
mystr = st.text_input("Write any 'Positive', 'Negative' words in this text field")


if st.button("Classify"):
    st.write(getPolarity(mystr))
