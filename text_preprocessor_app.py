import streamlit as st
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
import string

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

st.title("🧼 NLP Text Preprocessing App")
text_input = st.text_area("Enter your raw text here:")

if st.button("Preprocess"):
    text = text_input.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    
    ps = PorterStemmer()
    stemmed = [ps.stem(w) for w in tokens]
    
    lemmatizer = WordNetLemmatizer()
    lemmatized = [lemmatizer.lemmatize(w) for w in tokens]

    st.subheader("Cleaned Tokens:")
    st.write(tokens)
    st.subheader("Stemmed:")
    st.write(stemmed)
    st.subheader("Lemmatized:")
    st.write(lemmatized)
