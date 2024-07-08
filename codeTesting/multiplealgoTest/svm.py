import re
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score
from imblearn.over_sampling import RandomOverSampler

#Load text from data file
cmt = pd.read_excel("Feedback.xlsx")

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


model = SVC(kernel='linear')
model.fit(x_train, y_train)

#Computes the accuracy, precision, recall, and f1 score to evaluate the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average="weighted")
recall = recall_score(y_test, y_pred, average="weighted")
f1 = f1_score(y_test, y_pred, average="weighted")

print(f"Accuracy: {accuracy:.4f}")
print(f"Confusion Matrix:\n{confusion_matrix(y_test, y_pred)}")
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1 Score: {f1:.4f}")

#User input of comment to test the prediction
new_comment = input("Enter: ") #input comment
cleaned_comment = clean_cmt(new_comment) #runs the clean function to remove unecessary characters
new_features = vectorizer.transform([cleaned_comment])
predicted_sentiment = model.predict(new_features)[0]
print(f"Predicted sentiment: {predicted_sentiment}")



