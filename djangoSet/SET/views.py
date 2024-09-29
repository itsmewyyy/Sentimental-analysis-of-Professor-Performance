from rest_framework.views import APIView
from rest_framework.response import Response
from .models import categories, numerical_questions, feedback_questions, programs, department, year_level
from .serializers import CollegeSerializer
from rest_framework import status


class CategoriesAndQuestionsView(APIView):
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
     def get(self, request):
        questions = feedback_questions.objects.all()
        data = [{'feedback_question_id': q.feedback_question_id, 'question': q.question} for q in questions]
        return Response(data)




class CollegeListView(APIView):
    """
    View to list all colleges with their year levels, programs, and sections.
    """

    def get(self, request):
        # Retrieve all departments (colleges)
        colleges = department.objects.all()
        
        # Create a list to hold the serialized data for colleges
        college_data = []

        for college in colleges:
            # Get all programs associated with the department (college)
            programs_list = programs.objects.filter(dept_id=college)

            # Prepare the years data structure
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

                years_data.append(year_data)  # Add the year data to years_data

            # Append college data with its corresponding year levels
            college_data.append({
                'name': college.department_id,
                'description': college.department_desc,
                'years': years_data
            })

        return Response(college_data, status=status.HTTP_200_OK)