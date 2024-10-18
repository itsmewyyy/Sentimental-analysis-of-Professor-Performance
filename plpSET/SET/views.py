from rest_framework.views import APIView
from rest_framework.response import Response
from .models import categories, numerical_questions, feedback_questions, programs, department, year_level, student_info, student_enrolled_subjs, feedbacks
from .serializers import StudentSerializer, SubmitRatingsSerializer, EnrolledSubjectsSerializer
from rest_framework import status
from .tasks import process_feedback_task


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

    def post(self, request):
        serializer = SubmitRatingsSerializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.save()

            # Trigger the Celery task to process feedback asynchronously
            process_feedback_task.delay(validated_data)

            return Response({"message": "Ratings and feedback submitted successfully. Processing in background."}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)