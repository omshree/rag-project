
import joblib

import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

model = joblib.load("../models/best_model.pkl")
tfidf_vectorizer = joblib.load("../models/tfidf_vectorizer.pkl")

nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

# Function to preprocess text
def clean_text(text):
    text = text.lower() 
    text = re.sub(r'<.*?>', '', text) 
    text = re.sub(r'[^a-zA-Z0-9]', ' ', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub(r'\s+', ' ', text).strip() 
    tokens = nltk.word_tokenize(text)
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]
    return ' '.join(tokens)

def predict_category(text):
    cleaned_text = clean_text(text)
    text_tfidf = tfidf_vectorizer.transform([cleaned_text])
    prediction = model.predict(text_tfidf)
    return prediction[0]




