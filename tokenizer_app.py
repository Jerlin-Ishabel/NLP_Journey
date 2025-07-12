import streamlit as st
from nltk.tokenize import word_tokenize, sent_tokenize
import nltk

nltk.download('punkt')

st.title("🧠 Mini NLP Tokenizer App")
st.write("Welcome Ishaa! Paste your paragraph below:")

user_input = st.text_area("Your Text", "Ishaa is learning NLP. She is excited to explore AI!")

if st.button("Tokenize"):
    word_tokens = word_tokenize(user_input)
    sent_tokens = sent_tokenize(user_input)

    st.subheader("🔹 Sentence Tokens:")
    st.write(sent_tokens)

    st.subheader("🔢 Total sentence:")
    st.write(len(sent_tokens))

    st.subheader("🔹 Word Tokens:")
    st.write(word_tokens)

    st.subheader("🔢 Total Words:")
    st.write(len(word_tokens))
