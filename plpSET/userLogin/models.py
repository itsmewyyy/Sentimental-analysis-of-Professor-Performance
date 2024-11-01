from django.db import models
from SET.models import department

class student_acc(models.Model): 
    student_acc_number = models.CharField(max_length=8, primary_key=True)
    plp_email = models.EmailField(default='example_example@plpasig.edu.ph')
    date_of_birth = models.DateField(null=True)
    password = models.CharField(max_length=100)
    is_counted = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.student_acc_number}'
    
class admin_acc(models.Model): 
    admin_acc_id = models.CharField(max_length=8, primary_key=True)
    admin_username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    is_mis = models.BooleanField(default=False)
    dept_id = models.ForeignKey(department, on_delete=models.CASCADE, null=True, blank = True)
    is_dean = models.BooleanField(default=False)
    is_secretary = models.BooleanField(default=False)
   

    def __str__(self):
        return f'{self.admin_acc_id} - {self.admin_username}'

