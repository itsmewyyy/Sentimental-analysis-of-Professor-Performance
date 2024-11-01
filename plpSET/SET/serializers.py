from rest_framework import serializers
from datetime import datetime
from .models import section, programs, year_level, academic_year, academic_yearsem, professor_status, department, student_info, numerical_ratings, feedbacks, student_enrolled_subjs, numerical_questions, feedback_questions, professor_subjs, professor_info, subjects, categories, student_status
from userLogin.models import admin_acc
from django.utils import timezone

class SectionSerializer(serializers.ModelSerializer):

    name = serializers.CharField(source='section')

    class Meta:
        model = section
        fields = ['section_id', 'name', 'program', 'year_level']


class ProgramSerializer(serializers.ModelSerializer):
    sections = SectionSerializer(many=True, read_only=True)

    class Meta: 
        model = programs
        fields = ['program_id', 'program_desc', 'sections', 'dept_id']

class ProgramsSerializer(serializers.ModelSerializer):

    class Meta: 
        model = programs
        fields = ['program_id', 'program_desc', 'dept_id']


class YearLevelSerializer(serializers.ModelSerializer):
    programs = serializers.SerializerMethodField()

    class Meta:
        model = year_level
        fields = ['year_level_id', 'year_level_desc', 'programs']

    def get_programs(self, obj):
        programs_list = programs.objects.filter(sections__year_level=obj).distinct()
        return ProgramSerializer(programs_list, many=True).data


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = department
        fields = ['department_id', 'department_desc']


class CollegeSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='dept_id.department_id')
    description = serializers.CharField(source='dept_id.department_desc')
    years = YearLevelSerializer(many=True, read_only=True)

    class Meta:
        model = programs
        fields = ['name', 'description', 'years']

class StudentSerializer(serializers.ModelSerializer):
    full_name = serializers.ReadOnlyField()

    class Meta:
        model = student_info
        # Include the editable fields
        fields = ['student_id', 'first_name', 'middle_name', 'surname', 'section', 'status', 'full_name', 'extension_name']  

class SubmitRatingsSerializer(serializers.Serializer):
    numericalRatings = serializers.DictField(child=serializers.IntegerField())
    feedbackRatings = serializers.DictField(child=serializers.CharField())
    student_enrolled_subj_id = serializers.CharField()  # Add this field to identify the student-subject enrollment

    def create(self, validated_data):
        # Process and save numerical ratings
        for numerical_question_id, rating in validated_data['numericalRatings'].items():
            try:
                # Fetch the instance
                numerical_question_instance = numerical_questions.objects.get(numerical_question_id=numerical_question_id)
                student_enrolled_subj_instance = student_enrolled_subjs.objects.get(
                pk=validated_data['student_enrolled_subj_id']
            )

                # Create NumericalRatings instance
                numerical_ratings.objects.create(
                    numerical_id = f"{student_enrolled_subj_instance}_{numerical_question_instance}",
                    student_subj_id=student_enrolled_subj_instance, 
                    numerical_question_id=numerical_question_instance,  # Use the instance here
                    numerical_rating=rating,
                    numerical_rating_date=timezone.now() 
                )
            except numerical_questions.DoesNotExist:  # Fixed exception reference
                raise serializers.ValidationError(f"Numerical question with ID {numerical_question_id} does not exist.")

        # Process and save feedback ratings
        for question_id, feedback in validated_data['feedbackRatings'].items():
            try:

                #Fetch instance

                feedback_question_instance = feedback_questions.objects.get(feedback_question_id=question_id)
                student_enrolled_subj_instance = student_enrolled_subjs.objects.get(
                pk=validated_data['student_enrolled_subj_id']
            )

                feedbacks.objects.create(
                    feedback_id = f"{student_enrolled_subj_instance}_{feedback_question_instance}",
                    student_subj_id=student_enrolled_subj_instance, 
                    feedback_question_id=feedback_question_instance,
                    feedback_text=feedback,
                    feedback_date=timezone.now() 
                )
            except Exception as e:  
                raise serializers.ValidationError(f"Error creating feedback for question ID {question_id}: {str(e)}")

        # Update is_evaluated to True for the student enrolled in the subject
        try:
            student_enrolled_subj = student_enrolled_subjs.objects.get(
                pk=validated_data['student_enrolled_subj_id']
            )
            student_enrolled_subj.is_evaluated = True
            student_enrolled_subj.save()
        except student_enrolled_subjs.DoesNotExist:  
            raise serializers.ValidationError(f"Student enrolled subject with ID {validated_data['student_enrolled_subj_id']} does not exist.")

        return validated_data
    

# Serializer for Professor Info
class ProfessorInfoSerializer(serializers.ModelSerializer):
    department_desc = serializers.SerializerMethodField()

    full_name = serializers.ReadOnlyField()

    class Meta:
        model = professor_info
        fields = ['professor_id', 'surname', 'first_name','middle_name', 'full_name', 'department', 'department_desc',   'is_dean', 'status'] 

    # Method to get department description
    def get_department_desc(self, obj):
        return obj.department.department_desc if obj.department else None

# Serializer for Subject Info
class SubjectInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = subjects
        fields = ['subject_code', 'subject_desc', 'assoc_college' ]

# Serializer for Student Enrolled Subjects
class EnrolledSubjectsSerializer(serializers.ModelSerializer):
    prof_info = ProfessorInfoSerializer(source='prof_subj_id.professor_id', read_only=True)
    subj_name = SubjectInfoSerializer(source='prof_subj_id.subject_code', read_only=True)

    class Meta:
        model = student_enrolled_subjs
        fields = ['student_enrolled_subj_id', 'prof_info', 'subj_name', 'is_evaluated', 'student_id', 'prof_subj_id']

#Serializer for Admin List
class AdminSerializer(serializers.ModelSerializer):

    class Meta:
        model = admin_acc
        # Include the editable fields
        fields = ['admin_acc_id', 'admin_username', 'is_mis', 'is_dean', 'is_secretary', 'dept_id', 'password']  


#Serializer for Feedback Questions
class FeedbackQuestionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = feedback_questions
        fields = ['feedback_question_id', 'question']  

#Serializer for Category
class NumericalCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = categories
        fields = ['category_id', 'category_desc']  

#Serializer for Numerical Questions
class NumericalQuestionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = numerical_questions
        fields = ['category', 'numerical_question_id', 'question']  

class StudentStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = student_status
        fields = ['student_status_id', 'student_status_desc',]  


class ProfessorStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = professor_status
        fields = ['professor_status_id', 'professor_status_desc',]  


class YearLevelInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = year_level
        fields = ['year_level_id', 'year_level_desc']  

class ProfSubjsSerizalier(serializers.ModelSerializer):
    class Meta:
        model = professor_subjs
        fields = ['prof_subjects_id', 'year_sem_id', 'professor_id', 'subject_code', 'section_id']



class AcademicYearSemSerializer(serializers.ModelSerializer):
    acad_year = serializers.CharField(write_only=True)  # Accept the academic year as a string

    class Meta:
        model = academic_yearsem
        fields = ['year_sem_id', 'acad_year', 'semester_desc']

    def create(self, validated_data):
        # Extract acad_year and semester_desc from validated data
        acad_year_code = validated_data.pop('acad_year')  # This is the year (e.g., "24-25")
        semester_desc = validated_data['semester_desc']   # This will be "1st Semester" or "2nd Semester"

        # Retrieve or create the academic year instance
        acad_year_instance, created = academic_year.objects.get_or_create(
            acad_year=acad_year_code,
            defaults={'academic_year_desc': f"Academic Year {acad_year_code}"}
        )

        # Set the academic year instance in the validated data
        validated_data['acad_year'] = acad_year_instance

        # Create year_sem_id using the submitted academic year and semester number
        semester_number = validated_data['year_sem_id'].split('-')[-1]  # Assuming year_sem_id is in the format "24-25-1" or "24-25-2"
        validated_data['year_sem_id'] = f"{acad_year_code}-{semester_number}"  # e.g., "24-25-1" or "24-25-2"
        
        return super().create(validated_data)
    

from .models import EvaluationPeriod

class EvaluationPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = EvaluationPeriod
        fields = ['start_date', 'end_date', 'year_semester']
        
    def validate(self, data):
        # Ensure start_date is before end_date
        if data['start_date'] >= data['end_date']:
            raise serializers.ValidationError("The start date must be before the end date.")
        return data