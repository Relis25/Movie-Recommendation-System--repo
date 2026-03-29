import pandas as pd
import pickle as pk
from sklearn.feature_extraction.text import TfidfVectorizer
import streamlit as st

model = pk.load(open('model.pkl','rb'))
scaler = pk.load(open('scaler.pkl','rb'))

st.title("🎬 Movie Review Sentiment Analyzer")
st.subheader("Classify reviews as Positive, Negative, or Neutral")

review = st.text_input('Enter a Movie Review')

if st.button('Analyze Sentiment'):
    if review.strip() !="":
        review_scale = scaler.transform([review]).toarray()
        result = model.predict(review_scale)

        if result[0] == 0:
            st.write('Negative Review')
        elif result[0] == 1:
            st.write('Positive Review')
        elif result[0] == 2:  
            st.write('Neutral Review')
    else:
        st.warning("⚠️ Please enter a review before analyzing.")  