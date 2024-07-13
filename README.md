# Sentimental-analysis-of-Professor-Performance
Analyzing Pamantasan ng Lungsod ng Pasig Student Sentiments Towards Professor Performance A Naive Bayes Approach.

## Development Phases
### TECH STACK:
 Django 
 Vue
 MySQL

### 1. Design Phase

Designing the Student and Admin Side. Portal, Login Page, and Homepages.
Access the design file [here.](https://www.figma.com/design/PlZzJbSWQX5gVi2vTSaCHK/AAAaa-thesis?node-id=0-1&t=BN8PqhEH9J4X3dU8-1)

### 2. Code Testing and Simulation

Install the following to run the simulation: matploblib, gradio, pandas, scikitlearn, numpy, seaborn, jupyter 

### 3. Frontend Development

Student and Admin Login

Student Side
- Development of SET (Numerical and Feedback)

Admin Side (in no particular order)
- Generating reports and analysis
- Filtered feedbacks based on sentiment
- Graphs
- Summary of prof performance for each faculty. Ranking type based on total number of positive, neutral, and negative comments.
- Comparison and analysis of Numerical ratings and Comments (High numerical ratings -  negative feedbacks and vice versa)
- Recurring feedbacks/comments
- Recommendations 

### 4. Database Design and Development

Admin Login Information
- ID no.
- Password

Student Information
- Student no.
- Full name
- Courses
- Professors for each course

College and Professors
- Colleges
- Professors' name
- PT or FT
- Courses 

Numerical and Questions
- Each questions for the feedback and numerical

Numerical ratings
- Ratings for prof for each student

Feedback answers 
- answers for each prof
- Comment/Feedback id
- Student id

Trained data
- Trained historical data

Sorted out comments
- Feedback answers
- Comment/Feedback id
- Student id
- Sentiment category
- Sentiment score

### 5. Backend Development

Student Side
- Logging in pulls the students information from the database
- Submit button pushes each SET to the database to use for analysis generation

Admin Side
- Selection of faculty > Professor pulls the information from the database. 
- Adding or Removing feedback questions and numerical
- CRUD operations for admin
- English, Tagalog, and Taglish Sentimental Analysis. Storing to database.
- Recommendation system


### 6. Integration of Frontend and Backend
### 7. Testing and Debugging 

