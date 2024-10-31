import os
import re
import nltk
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from imblearn.over_sampling import SMOTE
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from collections import Counter
import pickle
import joblib

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')

def preprocess_text(text):
    lowercase_text = text.lower()
    cleaned_text = re.sub(r"[^a-zA-Z0-9\s]", "", lowercase_text) 

    tokens = word_tokenize(cleaned_text)

    stop_words = set(stopwords.words('english')) | set(["akin","aking","ako","alin","am","amin","aming","ang","ano","anumang","apat","at","atin","ating","ay","bababa","bago","bakit","bawat","bilang","dahil","dalawa","dapat","din","dito","doon","gagawin","gayunman","ginagawa","ginawa","ginawang","gumawa","gusto","habang","hanggang","huwag","iba","ibaba","ibabaw","ibig","ikaw","ilagay","ilalim","ilan","inyong","isa","isang","itaas","ito","iyo","iyon","iyong","ka","kahit","kailangan","kailanman","kami","kanila","kanilang","kanino","kanya","kanyang","kapag","kapwa","karamihan","katiyakan","katulad","kaya","kaysa","ko","kong","kumuha","kung","laban","lahat","lamang","likod","lima","maaari","maaaring","maging","makita","marami","marapat","may","mayroon","mga","minsan","mismo","mula","muli","na","nabanggit","naging","nagkaroon","nais","nakita","namin","napaka","narito","nasaan","ng","ngayon","ni","nila","nilang","nito","niya","niyang","noon","o","pa","paano","pababa","paggawa","pagitan","pagkakaroon","pagkatapos","palabas","pamamagitan","panahon","pangalawa","para","paraan","pareho","pataas","pero","pumunta","pumupunta","sa","saan","sabi","sabihin","sarili","sila","sino","siya","tatlo","tayo","tulad","tungkol","una"]) 
    tokens = [token for token in tokens if token not in stop_words]

    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    
    return ' '.join(tokens)

# Load training data from excel
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Feedback.xlsx')
feedbacks = pd.read_excel(file_path)
feedbacks["Comments"] = feedbacks["Comments"].fillna("")
feedbacks["processed_feedback"] = feedbacks["Comments"].apply(preprocess_text)

# Vectorize feedbacks
vectorizer = TfidfVectorizer(ngram_range=(1, 2))
features = vectorizer.fit_transform(feedbacks["processed_feedback"])
label = feedbacks["Label"]

# Oversample using SMOTE
smote = SMOTE(sampling_strategy={1: 2360, 0: 2360, -1: 2360}, random_state=100)
features_res, label_res = smote.fit_resample(features, label)

# Train-test split
x_train, X_test, y_train, y_test = train_test_split(features_res, label_res, test_size=0.2, random_state=42)

# Train Naive Bayes model
model = MultinomialNB(alpha=1.0)
model.fit(x_train, y_train)

# Define the directory for saving files
save_directory = os.path.dirname(os.path.abspath(__file__))  # Get the current script directory

# Save the model and vectorizer using joblib in the same directory
joblib.dump(model, os.path.join(save_directory, 'model.pkl'))
joblib.dump(vectorizer, os.path.join(save_directory, 'vectorizer.pkl'))

# Save any additional configurations or objects using pickle
config = {"model_type": "Naive Bayes", "vectorizer_type": "TF-IDF"}
with open(os.path.join(save_directory, 'config.pkl'), 'wb') as config_file:
    pickle.dump(config, config_file)

print("Model, vectorizer, and configurations saved successfully.")

