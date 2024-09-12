from django.db import models

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

class programs(models.Model):
    program_id = models.CharField(max_length=8, primary_key=True)
    program_desc = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.program_desc}'


class student_info(models.Model):
    student_id = models.CharField(max_length=8, primary_key=True)
    surname = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    first_name = models.CharField(max_length=100)
    program = models.ForeignKey(programs, on_delete=models.CASCADE, default = "PLP")
    year_level = models.ForeignKey(year_level, on_delete=models.CASCADE)
    section = models.CharField(max_length=10)
    status = models.ForeignKey(student_status, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.student_id} {self.surname} {self.first_name} {self.middle_name} - {self.section}'

class academic_year(models.Model):
    year_sem_id = models.CharField(max_length=10, primary_key=True)
    academic_year_desc = models.CharField(max_length=20)
    semester_desc = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.academic_year_desc} {self.semester_desc}'

class subjects(models.Model):
    subject_code = models.CharField(max_length=10, primary_key=True)
    subject_desc = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.subject_code} {self.subject_desc}'

class department(models.Model):
    department_id = models.CharField(max_length=6, primary_key=True)
    department_desc = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.department_desc}'

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
    status = models.ForeignKey(professor_status, on_delete=models.CASCADE)
    department = models.ForeignKey(department, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.surname} {self.first_name} {self.department}'

class professor_current_subjs(models.Model):  
    prof_subj_id = models.AutoField(primary_key=True)
    year_sem_id = models.ForeignKey(academic_year, on_delete=models.CASCADE)
    professor_id = models.ForeignKey(professor_info, on_delete=models.CASCADE)
    subject_code = models.ForeignKey(subjects, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.year_sem_id} {self.subject_code} -- {self.professor_id}'

class student_enrolled_subjs(models.Model):
    student_enrolled_subj_id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(student_info, on_delete=models.CASCADE, default = "00-00000")
    year_sem_id = models.ForeignKey(academic_year, on_delete=models.CASCADE)
    prof_subj_id = models.ForeignKey(professor_current_subjs, on_delete=models.CASCADE)
    units = models.PositiveSmallIntegerField() 
    grades = models.DecimalField(max_digits=5, decimal_places=2, null=True)

    def __str__(self):
        return f'{self.student_id} -- {self.prof_subj_id}'

class categories(models.Model):
    category_id = models.CharField(max_length=3, primary_key=True)
    category_desc = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.category_id}'

class numerical_questions(models.Model):
    numerical_question_id = models.CharField(max_length=4, primary_key=True)
    category = models.ForeignKey(categories, on_delete=models.CASCADE)
    question =  models.CharField(max_length=150)

    def __str__(self):
        return f'{self.category} {self.question}'


class numerical_ratings(models.Model):
    numerical_id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(student_info, on_delete=models.CASCADE)
    prof_subj_id = models.ForeignKey(professor_current_subjs, on_delete=models.CASCADE)
    numerical_question_id = models.ForeignKey(numerical_questions, on_delete=models.CASCADE)
    numerical_rating = models.PositiveSmallIntegerField()
    numerical_date = models.DateField()

    def __str__(self):
        return f'{self.numerical_question_id} - {self.numerical_rating}'

class feedback_questions(models.Model): 
    feedback_question_id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.feedback_question_id} {self.question}'
    
class feedbacks(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(student_info, on_delete=models.CASCADE)
    prof_subj_id = models.ForeignKey(professor_current_subjs, on_delete=models.CASCADE)
    feedback_question_id = models.ForeignKey(feedback_questions, on_delete=models.CASCADE)
    feedback_text =  models.TextField()
    feedback_date = models.DateField()

    def __str__(self):
        return f'{self.feedback_id}'

class filtered_feedbacks(models.Model):
    sentiment_id = models.AutoField(primary_key=True)
    feedback_id = models.ForeignKey(feedbacks, on_delete=models.CASCADE)
    sentiment_rating = models.IntegerField()
    sentiment_label = models.CharField(max_length=12)
    analysis_date = models.DateField
    
    def __str__(self):
        return f'{self.feedback_id} - {self.sentiment_label}'