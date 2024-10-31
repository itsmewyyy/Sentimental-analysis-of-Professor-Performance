from django.db import models
from SET.models import feedbacks, feedback_questions, numerical_questions, professor_info, academic_yearsem, department, categories
from datetime import datetime


class training_data(models.Model):
    training_data_id = models.AutoField(primary_key=True)
    sample_feedback = models.CharField(max_length=255)
    label = models.IntegerField()

class RecurringPhrase(models.Model):
    phrase = models.CharField(max_length=255)
    year_sem_id = models.ForeignKey(academic_yearsem, on_delete=models.CASCADE, default = "")
    prof_id = models.ForeignKey(professor_info, on_delete=models.CASCADE, default = "")
    department = models.ForeignKey(department, on_delete=models.CASCADE, default = "")
    total_count = models.IntegerField(default=0)
    sentiment_rating = models.IntegerField(default = 0)
    sentiment_label = models.CharField(max_length=12, default = "Neutral")
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.phrase} - {self.total_count}'

class processed_feedbacks(models.Model):
    feedback_id = models.ForeignKey(feedbacks, on_delete=models.CASCADE)
    processed_text = models.TextField() 
    processed_date = models.DateTimeField(default=datetime.now)
    recurring_phrases = models.ManyToManyField(RecurringPhrase, blank=True)
    is_processed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.feedback_id}'
    
class filtered_feedbacks(models.Model):
    sentiment_id = models.AutoField(primary_key=True)
    feedback_id = models.ForeignKey(feedbacks, on_delete=models.CASCADE, related_name='filtered_feedbacks')
    sentiment_rating = models.IntegerField()
    sentiment_label = models.CharField(max_length=12)
    analysis_date = models.DateTimeField(default=datetime.now) 
    processed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.feedback_id} - {self.sentiment_label}'

#Summaries in macro level - college focus
class college_numerical_total(models.Model):
    college_numerical_total_id = models.CharField(primary_key=True,max_length=50)
    year_sem_id = models.ForeignKey(academic_yearsem, on_delete=models.CASCADE)
    department = models.ForeignKey(department, on_delete=models.CASCADE)
    total_average = models.FloatField()

    def __str__(self):
        return f'{self.college_numerical_total_id} - {self.total_average}'
    
class college_numerical_summary(models.Model):
    college_numerical_summary_id = models.CharField(primary_key=True,max_length=50)
    year_sem_id = models.ForeignKey(academic_yearsem, on_delete=models.CASCADE)
    department = models.ForeignKey(department, on_delete=models.CASCADE)
    category = models.ForeignKey(categories, on_delete=models.CASCADE)
    college_average = models.FloatField()

    
    def __str__(self):
        return f'{self.college_numerical_summary_id} - {self.college_average}'

class college_feedback_total(models.Model):
    college_total_summary_id = models.CharField(primary_key=True,max_length=50)
    year_sem_id = models.ForeignKey(academic_yearsem, on_delete=models.CASCADE)
    department = models.ForeignKey(department, on_delete=models.CASCADE)
    total_feedbacks = models.IntegerField()
    total_positive = models.IntegerField()
    total_negative = models.IntegerField()
    total_neutral = models.IntegerField()

    def __str__(self):
        return f'{self.college_total_summary_id}'

class college_feedback_summary(models.Model):
    college_feedback_summary_id = models.CharField(primary_key=True,max_length=50)
    year_sem_id = models.ForeignKey(academic_yearsem, on_delete=models.CASCADE)
    department = models.ForeignKey(department, on_delete=models.CASCADE)
    feedback_question_id = models.ForeignKey(feedback_questions, on_delete=models.CASCADE)
    total_feedbacks = models.IntegerField()
    total_positive = models.IntegerField()
    total_negative = models.IntegerField()
    total_neutral = models.IntegerField()

    
    def __str__(self):
        return f'{self.college_feedback_summary_id}'

#Summaries in micro level - professor focus
class professor_numerical_total(models.Model):
    professor_numerical_total_id = models.CharField(primary_key=True, max_length=100)
    year_sem_id = models.ForeignKey(academic_yearsem, on_delete=models.CASCADE)
    prof_id = models.ForeignKey(professor_info, on_delete=models.CASCADE)
    total_average = models.FloatField()

    
    def __str__(self):
        return f'{self.professor_numerical_total_id} - {self.total_average}'

class professor_numerical_summary_category(models.Model):
    professor_numerical_summary_category_id = models.CharField(primary_key=True, max_length=50)
    category = models.ForeignKey(categories, on_delete=models.CASCADE)
    year_sem_id = models.ForeignKey(academic_yearsem, on_delete=models.CASCADE)
    prof_id = models.ForeignKey(professor_info, on_delete=models.CASCADE)
    category_average = models.FloatField()

    
    def __str__(self):
        return f'{self.professor_numerical_summary_category_id} - {self.category_average}'

class professor_numerical_summary_questions(models.Model):
    professor_numerical_summary_question_id = models.CharField(primary_key=True, max_length=50)
    numerical_question_id = models.ForeignKey(numerical_questions, on_delete=models.CASCADE)
    year_sem_id = models.ForeignKey(academic_yearsem, on_delete=models.CASCADE)
    prof_id = models.ForeignKey(professor_info, on_delete=models.CASCADE)
    question_average = models.FloatField()

    def __str__(self):
        return f'{self.professor_numerical_summary_question_id} - {self.question_average}'

class professor_feedback_total(models.Model):
    professor_feedback_total_id = models.CharField(primary_key=True,max_length=100)
    year_sem_id = models.ForeignKey(academic_yearsem, on_delete=models.CASCADE)
    prof_id = models.ForeignKey(professor_info, on_delete=models.CASCADE)
    total_feedbacks = models.IntegerField()
    total_positive = models.IntegerField()
    total_negative = models.IntegerField()
    total_neutral = models.IntegerField()

    def __str__(self):
        return f'{self.professor_feedback_total_id}'

class professor_feedback_summary(models.Model):
    professor_feedback_summary_id = models.CharField(primary_key=True,max_length=50)
    feedback_question_id = models.ForeignKey(feedback_questions, on_delete=models.CASCADE)
    year_sem_id = models.ForeignKey(academic_yearsem, on_delete=models.CASCADE)
    prof_id = models.ForeignKey(professor_info, on_delete=models.CASCADE)
    total_feedbacks = models.IntegerField()
    total_positive = models.IntegerField()
    total_negative = models.IntegerField()
    total_neutral = models.IntegerField()

    def __str__(self):
        return f'{self.professor_feedback_summary_id}'


  
    

