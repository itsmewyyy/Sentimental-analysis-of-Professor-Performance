from django.db import models


class student_info(models.Model):
    student_id = models.CharField(max_length=8, primary_key=True)
    surname = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    first_name = models.CharField(max_length=100)
    plp_email = models.CharField(max_length =100)
    course = models.CharField(max_length=100)
    section = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.student_id} - {self.surname} {self.first_name} {self.middle_name}'


class student_acc(models.Model): 
    student_acc_number = models.CharField(max_length=8, primary_key=True)
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.student_acc_number}'
    
class admin_acc(models.Model): 
    admin_acc_id = models.CharField(max_length=8, primary_key=True)
    admin_username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.admin_acc_id} - {self.admin_username}'

 