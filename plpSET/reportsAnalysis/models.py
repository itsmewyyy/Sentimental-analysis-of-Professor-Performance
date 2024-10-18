from django.db import models
from SET.models import feedbacks, feedback_questions, numerical_questions, professor_info, academic_yearsem
from datetime import datetime


class training_data(models.Model):
    training_data_id = models.AutoField(primary_key=True)
    sample_feedback = models.CharField(max_length=255)
    label = models.IntegerField()

class processed_feedbacks(models.Model):
    feedback_id = models.ForeignKey(feedbacks, on_delete=models.CASCADE)
    processed_text = models.TextField() 
    processed_date = models.DateTimeField(default=datetime.now) 

    def __str__(self):
        return f'{self.feedback_id}'

class filtered_feedbacks(models.Model):
    sentiment_id = models.AutoField(primary_key=True)
    feedback_id = models.ForeignKey(feedbacks, on_delete=models.CASCADE, related_name='filtered_feedbacks')
    sentiment_rating = models.IntegerField()
    sentiment_label = models.CharField(max_length=12)
    analysis_date = models.DateField(null=True)

    def __str__(self):
        return f'{self.feedback_id} - {self.sentiment_label}'

class feedback_summary(models.Model):
    feedback_summary_id = models.CharField(primary_key=True,max_length=50)
    feedback_question_id = models.ForeignKey(feedback_questions, on_delete=models.CASCADE)
    year_sem_id = models.ForeignKey(academic_yearsem, on_delete=models.CASCADE)
    prof_id = models.ForeignKey(professor_info, on_delete=models.CASCADE)
    total_feedbacks = models.IntegerField()
    total_positive = models.IntegerField()
    total_negative = models.IntegerField()
    total_neutral = models.IntegerField()

class numerical_summary(models.Model):
    numerical_summary_id = models.CharField(primary_key=True, max_length=50)
    numerical_questions_id = models.ForeignKey(numerical_questions, on_delete=models.CASCADE)
    year_sem_id = models.ForeignKey(academic_yearsem, on_delete=models.CASCADE)
    prof_id = models.ForeignKey(professor_info, on_delete=models.CASCADE)
    average = models.FloatField()
    

