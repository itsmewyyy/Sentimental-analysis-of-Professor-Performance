from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import categories, numerical_questions, feedback_questions, programs, department, year_level, student_info, student_enrolled_subjs, feedbacks
from reportsAnalysis.models import processed_feedbacks, filtered_feedbacks
from .serializers import StudentSerializer, SubmitRatingsSerializer, EnrolledSubjectsSerializer
from rest_framework import status
import joblib
import re
import os
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from django.utils import timezone
from django.conf import settings 


class CategoriesAndQuestionsView(APIView):
    #questions for numerical ratings

    def get(self, request):
        data = []
        for category in categories.objects.all():
            questions = numerical_questions.objects.filter(category=category)
            data.append({
                'category_id': category.category_id,
                'category_desc': category.category_desc,
                'questions': [{'numerical_question_id': q.numerical_question_id, 'question': q.question} for q in questions]
            })
        return Response(data)
    
class FeedbackQuestionsView(APIView):
     #feedback questions

     def get(self, request):
        questions = feedback_questions.objects.all()
        data = [{'feedback_question_id': q.feedback_question_id, 'question': q.question} for q in questions]
        return Response(data)



class CollegeListView(APIView):
    #all colleges, programs, years under the program, and sections.

    def get(self, request):
        # Retrieve all departments
        colleges = department.objects.all()
        
        # Create a list to hold the serialized data for colleges
        college_data = []

        for college in colleges:
            # Get all programs associated with the department or college
            programs_list = programs.objects.filter(dept_id=college)

            years_data = []
            for year in year_level.objects.all():
                # Initialize the year data
                year_data = {
                    'year_level_id': year.year_level_id,
                    'year_level_desc': year.year_level_desc,
                    'programs': []
                }

                # Fetch programs that have sections associated with this year level
                for program in programs_list:
                    # Fetch sections for this program in the current year level
                    sections = program.sections.filter(year_level=year)
                    program_data = {
                        'program_id': program.program_id,
                        'program_desc': program.program_desc,
                        'sections': [{'section_id': section.section_id, 'name': section.section} for section in sections]
                    }
                    year_data['programs'].append(program_data)

                years_data.append(year_data) 

            college_data.append({
                'name': college.department_id,
                'description': college.department_desc,
                'years': years_data
            })

        return Response(college_data, status=status.HTTP_200_OK)


class SectionStudentsView(APIView):
    def get(self, request, section_id):
        # Get students by the section_id 
        students = student_info.objects.filter(section__section_id=section_id)
        
        if not students.exists():
            return Response({"error": "No students found for this section"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = StudentSerializer(students, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)


class EnrolledSubjsView(APIView):
    def get(self, request, student_id=None):
        if not student_id:
            return Response({"error": "student_id is required"}, status=status.HTTP_400_BAD_REQUEST)

        # Filter enrolled subjects by student_id
        enrolled_subjs = student_enrolled_subjs.objects.filter(student_id__student_id=student_id)

        if enrolled_subjs.exists():
            serializer = EnrolledSubjectsSerializer(enrolled_subjs, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "No subjects found for this student"}, status=status.HTTP_404_NOT_FOUND)


class SubmitRatingsView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Load sentiment analysis model and vectorizer
        model_path = os.path.join(settings.BASE_DIR, 'reportsAnalysis', 'model.pkl')
        vectorizer_path = os.path.join(settings.BASE_DIR, 'reportsAnalysis', 'vectorizer.pkl')
        
        self.model = joblib.load(model_path)
        self.vectorizer = joblib.load(vectorizer_path)

        # Load stopwords 
        self.stop_words = set(stopwords.words('english')) | set([
            "akin", "aking", "ako", "alin", "am", "amin", "aming", "ang", "ano", "anumang", "apat", "at", "atin", 
            "ating", "ay", "bababa", "bago", "bakit", "bawat", "bilang", "dahil", "dalawa", "dapat", "din", "dito", 
            "doon", "gagawin", "gayunman", "ginagawa", "ginawa", "ginawang", "gumawa", "gusto", "habang", "hanggang", 
            "huwag", "iba", "ibaba", "ibabaw", "ibig", "ikaw", "ilagay", "ilalim", "ilan", "inyong", "isa", "isang", 
            "itaas", "ito", "iyo", "iyon", "iyong", "ka", "kahit", "kailangan", "kailanman", "kami", "kanila", "kanilang", 
            "kanino", "kanya", "kanyang", "kapag", "kapwa", "karamihan", "katiyakan", "katulad", "kaya", "kaysa", "ko", 
            "kong", "kumuha", "kung", "laban", "lahat", "lamang", "likod", "lima", "maaari", "maaaring", "maging", 
            "makita", "marami", "marapat", "may", "mayroon", "mga", "minsan", "mismo", "mula", "muli", "na", "nabanggit", 
            "naging", "nagkaroon", "nais", "nakita", "namin", "napaka", "narito", "nasaan", "ng", "ngayon", "ni", "nila", 
            "nilang", "nito", "niya", "niyang", "noon", "o", "pa", "paano", "pababa", "paggawa", "pagitan", "pagkakaroon", 
            "pagkatapos", "palabas", "pamamagitan", "panahon", "pangalawa", "para", "paraan", "pareho", "pataas", "pero", 
            "pumunta", "pumupunta", "sa", "saan", "sabi", "sabihin", "sarili", "sila", "sino", "siya", "tatlo", "tayo", 
            "tulad", "tungkol", "una"
        ])
    
    def preprocess_text(self, text): # preprocess the text
        lowercase_text = text.lower()
        cleaned_text = re.sub(r"[^a-zA-Z0-9\s]", "", lowercase_text)

        tokens = word_tokenize(cleaned_text)
        tokens = [token for token in tokens if token not in self.stop_words]

        lemmatizer = WordNetLemmatizer()
        tokens = [lemmatizer.lemmatize(token) for token in tokens]

        return ' '.join(tokens)

    def post(self, request):
        serializer = SubmitRatingsSerializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.save()  # Save numerical and feedback ratings
            processed_feedback_instances = []
            filtered_feedback_instances = []

            # Preprocess feedback ratings and analyze sentiment
            for question_id, feedback in validated_data['feedbackRatings'].items():
                # Preprocess the feedback text
                processed_text = self.preprocess_text(feedback)

                try:
                    # Fetch the feedback question instance
                    feedback_question_instance = feedback_questions.objects.get(feedback_question_id=question_id)

                    # Fetch the corresponding feedback instance that was just created
                    feedback_instance = feedbacks.objects.get(
                        student_subj_id=validated_data['student_enrolled_subj_id'],
                        feedback_question_id=feedback_question_instance
                        
                    )

                    # Store preprocessed feedback in processed_feedbacks table
                    processed_feedback_instance = processed_feedbacks(
                        feedback_id=feedback_instance,  # Use the ID from the feedback instance
                        processed_text=processed_text,
                        processed_date=timezone.now()
                    )
                    processed_feedback_instances.append(processed_feedback_instance)

                    # Perform sentiment analysis on the preprocessed text
                    features = self.vectorizer.transform([processed_text])
                    sentiment = self.model.predict(features)[0]
                    sentiment_label = "positive" if sentiment == 1 else "neutral" if sentiment == 0 else "negative"

                    # Prepare to store sentiment analysis result in filtered_feedbacks table
                    filtered_feedback_instance = filtered_feedbacks(
                        feedback_id=feedback_instance,  # Use the ID from the feedback instance
                        sentiment_rating=sentiment,
                        sentiment_label=sentiment_label,
                        analysis_date=timezone.now()
                    )
                    filtered_feedback_instances.append(filtered_feedback_instance)
                
                except (feedback_questions.DoesNotExist, student_enrolled_subjs.DoesNotExist) as e:
                    return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
            
            # Bulk create processed feedbacks and filtered feedbacks
            processed_feedbacks.objects.bulk_create(processed_feedback_instances)
            filtered_feedbacks.objects.bulk_create(filtered_feedback_instances)

            return Response({"message": "Ratings and feedback submitted successfully"}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


