
import re
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score
import matplotlib.pyplot as plt
import seaborn as sns

#----DATA PREPROCESSING----
#Load text from data file
cmt = pd.read_excel("Feedback.xlsx")

cmt.head()

#Data summarization
print("DATASET")
print("DIMENSION: ", cmt.shape)
print()
print("SUMMARY")
print(cmt.groupby("Label").size()) #prints out total numbers per label type (-1, 0, 1)
print()

# Clean comments to remove special characters
def clean_cmt(text):
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text) 
    text = text.lower() 
    return text

cmt["cleaned_comments"] = cmt["Comments"].apply(clean_cmt)

# Create a bag-of-words representation
vectorizer = CountVectorizer()
features = vectorizer.fit_transform(cmt["cleaned_comments"])


x_train, X_test, y_train, y_test = train_test_split(features, cmt["Label"], test_size=0.2, random_state=42)


model = MultinomialNB()
model.fit(x_train, y_train)


# Evaluate performance
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average="weighted")
recall = recall_score(y_test, y_pred, average="weighted")
f1 = f1_score(y_test, y_pred, average="weighted")

print(f"Accuracy: {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1 Score: {f1:.4f}")



new_comment = input("Enter new comment: ") 
cleaned_comment = clean_cmt(new_comment) 
new_features = vectorizer.transform([cleaned_comment])
predicted_sentiment = model.predict(new_features)[0]

print()
print(new_comment)
if predicted_sentiment == 1:
    print("Sentiment: Positive")
elif predicted_sentiment == 0:
    print("Sentiment: neutral")
elif predicted_sentiment == -1:
    print("Sentiment: neutral")

