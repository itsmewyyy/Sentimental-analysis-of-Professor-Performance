from celery import shared_task
from django.utils import timezone
from .models import feedbacks, feedback_questions
from reportsAnalysis.models import processed_feedbacks, filtered_feedbacks
from joblib import load

import os
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from django.conf import settings

# Load the model and vectorizer globally to avoid reloading them in every task
MODEL_PATH = os.path.join(settings.BASE_DIR, 'reportsAnalysis', 'model.pkl')
VECTORIZER_PATH = os.path.join(settings.BASE_DIR, 'reportsAnalysis', 'vectorizer.pkl')

model = load(MODEL_PATH)
vectorizer = load(VECTORIZER_PATH)

# Load stopwords
stop_words = set(stopwords.words('english')) | set(["akin","aking","ako","alin","am","amin","aming","ang","ano","anumang","apat","at","atin","ating","ay","bababa","bago","bakit","bawat","bilang","dahil","dalawa","dapat","din","dito","doon","gagawin","gayunman","ginagawa","ginawa","ginawang","gumawa","gusto","habang","hanggang","huwag","iba","ibaba","ibabaw","ibig","ikaw","ilagay","ilalim","ilan","inyong","isa","isang","itaas","ito","iyo","iyon","iyong","ka","kahit","kailangan","kailanman","kami","kanila","kanilang","kanino","kanya","kanyang","kapag","kapwa","karamihan","katiyakan","katulad","kaya","kaysa","ko","kong","kumuha","kung","laban","lahat","lamang","likod","lima","maaari","maaaring","maging","makita","marami","marapat","may","mayroon","mga","minsan","mismo","mula","muli","na","nabanggit","naging","nagkaroon","nais","nakita","namin","napaka","narito","nasaan","ng","ngayon","ni","nila","nilang","nito","niya","niyang","noon","o","pa","paano","pababa","paggawa","pagitan","pagkakaroon","pagkatapos","palabas","pamamagitan","panahon","pangalawa","para","paraan","pareho","pataas","pero","pumunta","pumupunta","sa","saan","sabi","sabihin","sarili","sila","sino","siya","tatlo","tayo","tulad","tungkol","una"]) 
lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    lowercase_text = text.lower()
    cleaned_text = re.sub(r"[^a-zA-Z0-9\s]", "", lowercase_text)
    tokens = word_tokenize(cleaned_text)
    tokens = [token for token in tokens if token not in stop_words]
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return ' '.join(tokens)

@shared_task
def process_feedback_task(feedback_data):
    processed_feedback_instances = []
    filtered_feedback_instances = []

    for question_id, feedback in feedback_data['feedbackRatings'].items():
        processed_text = preprocess_text(feedback)
        
        try:
            feedback_question_instance = feedback_questions.objects.get(feedback_question_id=question_id)
            feedback_instance = feedbacks.objects.get(
                student_subj_id=feedback_data['student_enrolled_subj_id'],
                feedback_question_id=feedback_question_instance
            )

            # Store preprocessed feedback
            processed_feedback_instance = processed_feedbacks(
                feedback_id=feedback_instance,
                processed_text=processed_text,
                processed_date=timezone.now()
            )
            processed_feedback_instances.append(processed_feedback_instance)

            # Perform sentiment analysis
            features = vectorizer.transform([processed_text])
            sentiment = model.predict(features)[0]
            sentiment_label = "positive" if sentiment == 1 else "neutral" if sentiment == 0 else "negative"

            filtered_feedback_instance = filtered_feedbacks(
                feedback_id=feedback_instance,
                sentiment_rating=sentiment,
                sentiment_label=sentiment_label,
                analysis_date=timezone.now()
            )
            filtered_feedback_instances.append(filtered_feedback_instance)

        except feedback_questions.DoesNotExist:
            return f"Feedback question with ID {question_id} does not exist"
    
    # Save results
    processed_feedbacks.objects.bulk_create(processed_feedback_instances)
    filtered_feedbacks.objects.bulk_create(filtered_feedback_instances)

    return "Feedback processed successfully"
