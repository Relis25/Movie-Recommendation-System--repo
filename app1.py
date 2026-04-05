import pickle as pk
import streamlit as st


model = pk.load(open('model.pkl', 'rb'))
scaler = pk.load(open('scaler.pkl', 'rb'))  

st.title("🎬 Movie Review Sentiment Analyzer")
st.subheader("Classify reviews as Positive, Negative, or Neutral")

review = st.text_input("Enter a Movie Review")

if st.button('Analyze Sentiment'):
    if review.strip() != "":
        # Transform text into TF-IDF features
        review_scale = scaler.transform([review]).toarray()  
        result = model.predict(review_scale)[0]              

        if result == 0:
            st.success("Negative Review")
        elif result == 1:
            st.success("Positive Review")
        elif result == 2:
            st.success("Neutral Review")
    else:
        st.warning("⚠️ Please enter a review before analyzing.")