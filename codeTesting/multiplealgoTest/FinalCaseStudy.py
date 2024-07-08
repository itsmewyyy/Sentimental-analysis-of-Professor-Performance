''' Final Case Study

Ryan Celestino Intalan
France Angelo Alcantara
Gian Carlo Catalan

'''

#Necessities
import re
import pandas as pd
import matplotlib.pyplot as mpl

#Models and Pre-processing
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

#Metrics
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score

#----DATA PREPROCESSING----
#Load text from data file
cmt = pd.read_excel("Feedback.xlsx")

#Data summarization
print("DATASET")
print("DIMENSION: ", cmt.shape)
print()
print("SUMMARY")
print(cmt.groupby("Label").size()) #prints out total numbers per label type (-1, 0, 1)
print()

#Data visualization of data distribution
values = cmt["Label"] 

# Count the occurences of each value (-1, 0, 1)
value_counts = values.value_counts()

# heights and labels for the bars
labels = value_counts.index.astype(str).to_list()
heights = value_counts.to_list()

# Create the bar chart
mpl.bar(labels, heights)
mpl.title("Data Distribution")
mpl.xlabel("Values")
mpl.ylabel("Count")

# Create pie chart
mpl.figure(figsize=(6, 6))  # Adjust figure size if needed
mpl.pie(heights, labels=labels, autopct="%1.1f%%")
mpl.title("Data Distribution")

# Show the chart
mpl.show(block=False)  # block=False allows code to run


# Function to clean comments to remove special characters
def clean_cmt(text):
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text) 
    text = text.lower() 
    return text

cmt["cleaned_comments"] = cmt["Comments"].apply(clean_cmt)

# Create a bag-of-words representation
vectorizer = CountVectorizer()
features = vectorizer.fit_transform(cmt["cleaned_comments"])


#---EVALUATE ALGORITHMS----

#Splitting the dataset for training and testing using the single split method
x_train, X_test, y_train, y_test = train_test_split(features, cmt["Label"], test_size=0.2, random_state=42) #20% will be used for testing data

#models to evaluate
models = {
    "Naive Bayes": MultinomialNB(),
    "Random Forest Classifier": RandomForestClassifier(),
    "Gradient Boosting Classifier": GradientBoostingClassifier(n_estimators=200, random_state=42),
    "Support Vector Classifier": SVC(kernel='linear')
}

#Evaluating each algorithm
for name, model in models.items():
    model.fit(x_train, y_train)
  
#ACCURACY
#Computing accuracies
accuracies = {}
for model_name, model in models.items():
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    accuracies[model_name] = accuracy

# Print accuracies for all models
print("Model accuracies:")
for model_name, accuracy in accuracies.items():
    print(f"- {model_name}: {accuracy:.4f}")

#PRECISION
#Computing precisions
precisions = {}
for model_name, model in models.items():
    y_pred = model.predict(X_test)
    precision = precision_score(y_test, y_pred, average="weighted")
    precisions[model_name] = precision

# Print precisions for all models
print()
print("Model precisions: ")
for model_name, precision in precisions.items():
    print(f"- {model_name}: {precision:.4f}")

#RECALL
#Computing recall
recalls = {}
for model_name, model in models.items():
    y_pred = model.predict(X_test)
    recall = recall_score(y_test, y_pred, average="weighted")
    recalls[model_name] = recall

# Print recall for all models
print()
print("Model recall: ")
for model_name, recall in recalls.items():
    print(f"- {model_name}: {recall:.4f}")

#F1 SCORES
#Computing f1 scores
f1scores = {}
for model_name, model in models.items():
    y_pred = model.predict(X_test)
    f1 = f1_score(y_test, y_pred, average="weighted")
    f1scores[model_name] = f1

# Print f1 scores for all models
print()
print("Model f1 score: ")
for model_name, f1 in f1scores.items():
    print(f"- {model_name}: {f1:.4f}")

#CONFUSION MATRIX
cmatrix = {}
for model_name, model in models.items():
    y_pred = model.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)
    cmatrix[model_name] = cm

# Print all confusion matrix
print()
print("Confusion Matrix: ")
print()
for model_name, cm in cmatrix.items():
    print(f"- {model_name} -")
    print(cm)
    print()


#Choosing the best model for the prediction of new comments based on f1 scores
b_model_name = max(f1scores, key=f1scores.get)
b_model = models[b_model_name]
print()
print("Best model:", b_model_name)


#User input of comment to test the prediction
new_comment = input("Enter new comment: ") #input comment
cleaned_comment = clean_cmt(new_comment) #runs the clean function to remove unecessary characters
new_features = vectorizer.transform([cleaned_comment])
predicted_sentiment = b_model.predict(new_features)[0]
print(f"Predicted sentiment for new comment: {predicted_sentiment}")



