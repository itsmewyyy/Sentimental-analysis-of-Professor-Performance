from rest_framework.views import APIView
from rest_framework.response import Response
from .models import categories, numerical_questions, academic_yearsem, EvaluationPeriod, professor_status, feedback_questions, programs, department, year_level, student_info, student_enrolled_subjs, feedbacks, professor_info, section, subjects, student_status
from .serializers import StudentSerializer, YearLevelInfoSerializer, AcademicYearSemSerializer, ProfSubjsSerizalier, EvaluationPeriodSerializer, ProfessorStatusSerializer, SubmitRatingsSerializer, EnrolledSubjectsSerializer, AdminSerializer, ProfessorInfoSerializer, ProgramsSerializer, DepartmentSerializer, SectionSerializer, SubjectInfoSerializer, FeedbackQuestionsSerializer, NumericalCategorySerializer, NumericalQuestionsSerializer, StudentStatusSerializer
from rest_framework import status
from userLogin.models import admin_acc, student_acc
from django.contrib.auth.hashers import make_password
from .tasks import (process_feedback_task)
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.http import JsonResponse



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
    

class SubjectTaggingView(APIView):
    def get(self, requset):

        Subjects = [

        ]
        return Response(Subjects, status=status.HTTP_200_OK)

class SectionTaggingView(APIView):
    def get(self, requset):

        Sections = [

        ]
        return Response(Sections, status=status.HTTP_200_OK)

# Views for Databases
class AdminListView(APIView):

    def get(self, request):
      
        admins = admin_acc.objects.all()
        
        serializer = AdminSerializer(admins, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProfessorListView(APIView):

    def get(self, request):
 
        professors = professor_info.objects.all()
     
        serializer = ProfessorInfoSerializer(professors, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)

class DepartmentListView(APIView):

    def get(self, request):
 
        departments = department.objects.all()
     
        serializer = DepartmentSerializer(departments, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)

class ProgramListView(APIView):

    def get(self, request):
 
        program = programs.objects.all()

        serializer = ProgramsSerializer(program, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)


class SectionListView(APIView):

    def get(self, request):
 
        sections = section.objects.all()

        serializer = SectionSerializer(sections, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)

class SubjectListView(APIView):

    def get(self, request):
 
        subject = subjects.objects.all()

        serializer = SubjectInfoSerializer(subject, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)

class FeedbackQuestionsView(APIView):

     def get(self, request):
        feedbackquestion = feedback_questions.objects.all()

        serializer = FeedbackQuestionsSerializer(feedbackquestion, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)


class NumericalCategoryView(APIView):

     def get(self, request):
        category = categories.objects.all()

        serializer = NumericalCategorySerializer(category, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)


class NumericalQuestionsView(APIView):

     def get(self, request):
        numericalquestion = numerical_questions.objects.all()

        serializer = NumericalQuestionsSerializer(numericalquestion, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)

class StudentStatusView(APIView):

     def get(self, request):
        statuses = student_status.objects.all()

        serializer = StudentStatusSerializer(statuses, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)

class ProfessorStatusView(APIView):

     def get(self, request):
        statuses = professor_status.objects.all()

        serializer = ProfessorStatusSerializer(statuses, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)

class YearLevelView(APIView):

     def get(self, request):
        statuses = year_level.objects.all()

        serializer = YearLevelInfoSerializer(statuses, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class StudentListView(APIView):

     def get(self, request):
        statuses = student_info.objects.all()

        serializer = StudentSerializer(statuses, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)



#ADD, EDIT, AND DELETE
#STUDENT
class StudentDetailView(APIView):
    def get_object(self, student_id):
        try:
            return student_info.objects.get(student_id=student_id)
        except student_info.DoesNotExist:
            return None

    def get(self, request, student_id):
        student = self.get_object(student_id)
        if not student:
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Student added successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, student_id):
        student = self.get_object(student_id)
        if not student:
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, student_id):
        student = self.get_object(student_id)
        if not student:
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
        
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class NumericalQuestionDetailView(APIView):
    def get_object(self, numerical_question_id):
        try:
            return numerical_questions.objects.get(numerical_question_id=numerical_question_id)
        except numerical_questions.DoesNotExist:
            return None

    def get(self, request, numerical_question_id):
        numerical_question = self.get_object(numerical_question_id)
        if not numerical_question :
            return Response({"error": "not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = NumericalQuestionsSerializer(numerical_question)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer =  NumericalQuestionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "added successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, numerical_question_id):
        numerical_question  = self.get_object(numerical_question_id)
        if not numerical_question :
            return Response({"error": "not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = NumericalQuestionsSerializer(numerical_question , data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, numerical_question_id):
        numerical_question  = self.get_object(numerical_question_id)
        if not numerical_question :
            return Response({"error": "not found"}, status=status.HTTP_404_NOT_FOUND)
        
        numerical_question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
class NumericalCategoryDetailView(APIView):
    def get_object(self, category_id):
        try:
            return categories.objects.get(category_id=category_id)
        except categories.DoesNotExist:
            return None

    def get(self, request, category_id):
        category = self.get_object(category_id)
        if not category:
            return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = NumericalCategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer =  NumericalCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Category added successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, category_id):
        category = self.get_object(category_id)
        if not category:
            return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = NumericalCategorySerializer(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, category_id):
        category = self.get_object(category_id)
        if not category:
            return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
        
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
class FeedbackQuestionDetailView(APIView):
    def get_object(self, feedback_question_id):
        try:
            return feedback_questions.objects.get(feedback_question_id=feedback_question_id)
        except feedback_questions.DoesNotExist:
            return None

    def get(self, request, feedback_question_id):
        feedback_question = self.get_object(feedback_question_id)
        if not feedback_question :
            return Response({"error": "not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = FeedbackQuestionsSerializer(feedback_question)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer =  FeedbackQuestionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "added successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, feedback_question_id):
        feedback_question  = self.get_object(feedback_question_id)
        if not feedback_question :
            return Response({"error": "not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = FeedbackQuestionsSerializer(feedback_question , data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, feedback_question_id):
        feedback_question  = self.get_object(feedback_question_id)
        if not feedback_question :
            return Response({"error": "not found"}, status=status.HTTP_404_NOT_FOUND)
        
        feedback_question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
class CollegeDetailView(APIView):
    def get_object(self, department_id):
        try:
            return department.objects.get(department_id=department_id)
        except department_id.DoesNotExist:
            return None

    def get(self, request, department_id):
        dept = self.get_object(department_id)
        if not dept :
            return Response({"error": "not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = DepartmentSerializer(dept)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer =  DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "added successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, department_id):
        dept  = self.get_object(department_id)
        if not dept :
            return Response({"error": "not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = DepartmentSerializer(dept , data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, department_id):
        dept  = self.get_object(department_id)
        if not dept :
            return Response({"error": "not found"}, status=status.HTTP_404_NOT_FOUND)
        
        dept.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProgramDetailView(APIView):
    def get_object(self, program_id):
        try:
            return programs.objects.get(program_id=program_id)
        except program_id.DoesNotExist:
            return None

    def get(self, request, program_id):
        program = self.get_object(program_id)
        if not  program :
            return Response({"error": "not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProgramsSerializer( program)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer =  ProgramsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "added successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, program_id):
        program  = self.get_object(program_id)
        if not  program :
            return Response({"error": "not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProgramsSerializer( program , data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, program_id):
        program  = self.get_object(program_id)
        if not program :
            return Response({"error": "not found"}, status=status.HTTP_404_NOT_FOUND)
        
        program.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SectionDetailView(APIView):
    def get_object(self, section_id):
        try:
            return section.objects.get(section_id=section_id)
        except section_id.DoesNotExist:
            return None

    def get(self, request, section_id):
        sections = self.get_object(section_id)
        if not sections :
            return Response({"error": "not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = SectionSerializer( sections)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer =  SectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "added successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, section_id):
        sections  = self.get_object(section_id)
        if not  sections :
            return Response({"error": "not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = SectionSerializer(  sections , data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, section_id):
        sections  = self.get_object(section_id)
        if not sections:
            return Response({"error": "not found"}, status=status.HTTP_404_NOT_FOUND)
        
        sections.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SubjectDetailView(APIView):
    def get_object(self, subject_code):
        try:
            return subjects.objects.get(subject_code=subject_code)
        except subject_code.DoesNotExist:
            return None

    def get(self, request, subject_code):
        subject = self.get_object(subject_code)
        if not section  :
            return Response({"error": "not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = SubjectInfoSerializer( subject)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer =  SubjectInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "added successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, subject_code):
        subject  = self.get_object(subject_code)
        if not  subject :
            return Response({"error": "not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = SubjectInfoSerializer( subject , data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, subject_code):
        subject  = self.get_object(subject_code)
        if not subject:
            return Response({"error": "not found"}, status=status.HTTP_404_NOT_FOUND)
        
        subject.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProfessorDetailView(APIView):
    def get_object(self, professor_id):
        try:
            return professor_info.objects.get(professor_id=professor_id)
        except professor_id.DoesNotExist:
            return None

    def get(self, request, professor_id):
        prof = self.get_object(professor_id)
        if not section  :
            return Response({"error": "not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProfessorInfoSerializer(prof )
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer =  ProfessorInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "added successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, professor_id):
        prof   = self.get_object(professor_id)
        if not  prof  :
            return Response({"error": "not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProfessorInfoSerializer( prof  , data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, professor_id):
        prof  = self.get_object(professor_id)
        if not prof :
            return Response({"error": "not found"}, status=status.HTTP_404_NOT_FOUND)
        
        prof.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AdminDetailView(APIView):
    def get_object(self, admin_acc_id):
        try:
            return admin_acc.objects.get(admin_acc_id=admin_acc_id)
        except admin_acc.DoesNotExist:
            return None

    def get(self, request, admin_acc_id):
        prof = self.get_object(admin_acc_id)
        if not prof:
            return Response({"error": "not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = AdminSerializer(prof)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        password = data.get("password")
        confirm_password = data.get("confirm_password")

        if password != confirm_password:
            return Response({"error": "Passwords do not match"}, status=status.HTTP_400_BAD_REQUEST)

        # Hash the password
        data["password"] = make_password(password)
        
        serializer = AdminSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Professor added successfully!"}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, admin_acc_id):
        prof = self.get_object(admin_acc_id)
        if not prof:
            return Response({"error": "not found"}, status=status.HTTP_404_NOT_FOUND)
        
        data = request.data
        password = data.get("password")
        confirm_password = data.get("confirm_password")

        if password != confirm_password:
            return Response({"error": "Passwords do not match"}, status=status.HTTP_400_BAD_REQUEST)

        # Hash the password
        data["password"] = make_password(password)
        
        serializer = AdminSerializer(prof, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, admin_acc_id):
        prof = self.get_object(admin_acc_id)
        if not prof:
            return Response({"error": "not found"}, status=status.HTTP_404_NOT_FOUND)
        
        prof.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class ProfSubjs(APIView):
    def post(self, request):
        serializer =  ProfSubjsSerizalier(data=request.data)
        if serializer.is_valid():
            prof_subj = serializer.save()
            return Response({"prof_subjects_id": prof_subj.prof_subjects_id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EnrolledSubjsPost(APIView):
    def post(self, request):
        serializer =  EnrolledSubjectsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "added successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SetAcademicTermView(APIView):
    def post(self, request):
        serializer = AcademicYearSemSerializer(data=request.data)
        if serializer.is_valid():
            # Save the new academic term, which includes creating or getting `academic_year`
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class EvaluationStatusView(APIView):
    def get(self, request):
        try:
            # Retrieve the latest evaluation period
            evaluation_period = EvaluationPeriod.objects.latest('start_date')
            serializer = EvaluationPeriodSerializer(evaluation_period)
            
            # Check if the current date is within the evaluation period
            is_active = evaluation_period.is_active()
            return Response({
                'status': 'active' if is_active else 'inactive',
                'evaluation_period': serializer.data
            })
        except EvaluationPeriod.DoesNotExist:
            return Response({
                'status': 'inactive',
                'evaluation_period': None
            }, status=status.HTTP_404_NOT_FOUND)
    
    def post(self, request):
        serializer = EvaluationPeriodSerializer(data=request.data)
        if serializer.is_valid():
            # Save new evaluation period
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def get_current_year_sem(request):
   
    current_year_sem = academic_yearsem.objects.latest('year_sem_id')
    data = {
        "year_sem_id": current_year_sem.year_sem_id,
        "acad_year": current_year_sem.acad_year.acad_year,  
        "semester_desc": current_year_sem.semester_desc,
    }
    return JsonResponse(data)



def get_student_profile(request):
    # Retrieve the student ID from the query parameters
    student_id = request.GET.get('student_id')

    if not student_id:
        return JsonResponse({'error': 'Student ID not provided'}, status=400)

    # Fetch data from the models
    student_account = get_object_or_404(student_acc, student_acc_number=student_id)
    student_details = get_object_or_404(student_info, student_id=student_id)

    # Construct response data
    profile_data = {
        'account': {
            'student_acc_number': student_account.student_acc_number,
            'plp_email': student_account.plp_email,
            'date_of_birth': student_account.date_of_birth,
        },
        'info': {
            'surname': student_details.surname,
            'first_name': student_details.first_name,
            'middle_name': student_details.middle_name,
            'extension_name': student_details.extension_name,
            'status': student_details.status.student_status_desc,  # Assuming student_status has a status_name field
            'section': student_details.section.section_id,  # Assuming section has a section_name field
        }
    }

    return JsonResponse(profile_data)