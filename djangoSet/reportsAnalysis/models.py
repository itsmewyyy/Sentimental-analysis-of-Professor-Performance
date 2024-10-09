from django.db import models
from SET.models import feedbacks


class training_data(models.Model):
    training_data_id = models.AutoField(primary_key=True)
    sample_feedback = models.CharField(max_length=255)
    label = models.IntegerField()

class filtered_feedbacks(models.Model):
    sentiment_id = models.AutoField(primary_key=True)
    feedback_id = models.ForeignKey(feedbacks, on_delete=models.CASCADE, related_name='filtered_feedbacks')
    sentiment_rating = models.IntegerField()
    sentiment_label = models.CharField(max_length=12)
    analysis_date = models.DateField(null=True)

    def __str__(self):
        return f'{self.feedback_id} - {self.sentiment_label}'
