from django.db import models

class Student(models.Model):
    student_number = models.CharField(max_length=7, primary_key=True)
    surname = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    first_name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    section = models.CharField(max_length=10)