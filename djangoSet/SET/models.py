from django.db import models
from datetime import datetime

class year_level(models.Model): 
    year_level_id = models.PositiveSmallIntegerField(primary_key=True)
    year_level_desc = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.year_level_desc}'

class student_status(models.Model):
    student_status_id = models.CharField(max_length=3, primary_key=True)
    student_status_desc = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.student_status_desc}'
    

class department(models.Model):
    department_id = models.CharField(max_length=6, primary_key=True)
    department_desc = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.department_desc}'

class programs(models.Model):
    program_id = models.CharField(max_length=8, primary_key=True)
    program_desc = models.CharField(max_length=100)
    dept_id = models.ForeignKey(department, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.program_desc}'

class section(models.Model):
    section_id = models.CharField(max_length=8, primary_key=True)
    program = models.ForeignKey(programs, on_delete=models.CASCADE, default="PLP", related_name='sections')
    year_level = models.ForeignKey(year_level, on_delete=models.CASCADE, related_name='sections')
    section = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.section_id}'

class student_info(models.Model):
    student_id = models.CharField(max_length=8, primary_key=True)
    surname = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    first_name = models.CharField(max_length=100)
    section = models.ForeignKey(section, on_delete=models.CASCADE, related_name='students')
    status = models.ForeignKey(student_status, on_delete=models.CASCADE, related_name='students')

    def full_name(self):
        names = [self.surname, self.first_name]
        if self.middle_name:
            names.insert(1, self.middle_name)  # Insert middle name if it exists
        return ' '.join(names)

    def __str__(self):
        # Use the full_name method to get the full name for the string representation
        return f'{self.student_id}'
    
class academic_year(models.Model):
    acad_year = models.CharField(max_length=6, primary_key=True, default="24-25")
    academic_year_desc = models.CharField(max_length=20)
   
    def __str__(self):
        return f'{self.acad_year}'

class academic_yearsem(models.Model):
    year_sem_id = models.CharField(max_length=10, primary_key=True)
    acad_year = models.ForeignKey(academic_year, on_delete=models.CASCADE, related_name='semesters')
    semester_desc = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.year_sem_id} {self.semester_desc}'

class subjects(models.Model):
    subject_code = models.CharField(max_length=10, primary_key=True)
    subject_desc = models.CharField(max_length=100)
    assoc_college = models.ForeignKey(department, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.subject_code} {self.subject_desc}'

class professor_status(models.Model):
    professor_status_id = models.CharField(max_length=2, primary_key=True)
    professor_status_desc = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.professor_status_desc}'

class professor_info(models.Model):
    professor_id = models.CharField(max_length=12, primary_key=True)
    surname = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    first_name = models.CharField(max_length=100)
    status = models.ForeignKey(professor_status, on_delete=models.CASCADE, related_name='professors')
    department = models.ForeignKey(department, on_delete=models.CASCADE, related_name='professors')
    is_dean = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.surname} {self.first_name} {self.department}'

class professor_subjs(models.Model):  
    prof_subjects_id = models.CharField(primary_key=True, max_length=100)
    year_sem_id = models.ForeignKey(academic_yearsem, on_delete=models.CASCADE, related_name='professor_subjects')
    professor_id = models.ForeignKey(professor_info, on_delete=models.CASCADE, related_name='professor_subjects')
    subject_code = models.ForeignKey(subjects, on_delete=models.CASCADE, related_name='professor_subjects')
    section_id = models.ForeignKey(section, on_delete=models.CASCADE, related_name='professor_subjects')

    def __str__(self):
        return f'{self.year_sem_id} {self.subject_code} -- {self.professor_id}'

class student_enrolled_subjs(models.Model):
    student_enrolled_subj_id = models.CharField(primary_key=True, max_length=100)
    student_id = models.ForeignKey(student_info, on_delete=models.CASCADE, default="21-00260", related_name='enrolled_subjects')
    prof_subj_id = models.ForeignKey(professor_subjs, on_delete=models.CASCADE, related_name='enrolled_students')
    is_evaluated = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.student_enrolled_subj_id}'

class categories(models.Model):
    category_id = models.CharField(max_length=5, primary_key=True)
    category_desc = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.category_id} {self.category_desc}'

class numerical_questions(models.Model):
    numerical_question_id = models.CharField(max_length=4, primary_key=True)
    category = models.ForeignKey(categories, on_delete=models.CASCADE, related_name='numerical_questions')
    question = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.numerical_question_id}'

class numerical_ratings(models.Model):
    numerical_id = models.CharField(primary_key=True, max_length=100)
    student_subj_id = models.ForeignKey(student_enrolled_subjs, on_delete=models.CASCADE, null=True, related_name='numerical_ratings')
    numerical_question_id = models.ForeignKey(numerical_questions, on_delete=models.CASCADE, related_name='numerical_ratings')
    numerical_rating = models.PositiveSmallIntegerField()
    numerical_rating_date = models.DateTimeField(default=datetime.now) 

    def __str__(self):
        return f'{self.numerical_id}'

class feedback_questions(models.Model): 
    feedback_question_id = models.IntegerField(primary_key=True)
    question = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.feedback_question_id}'

class feedbacks(models.Model):
    feedback_id = models.CharField(primary_key=True, max_length=100)
    student_subj_id = models.ForeignKey(student_enrolled_subjs, on_delete=models.CASCADE, null=True, related_name='feedbacks')
    feedback_question_id = models.ForeignKey(feedback_questions, on_delete=models.CASCADE, related_name='feedbacks')
    feedback_text = models.TextField()
    feedback_date = models.DateTimeField(default=datetime.now) 

    def __str__(self):
        return f'{self.feedback_id}'

