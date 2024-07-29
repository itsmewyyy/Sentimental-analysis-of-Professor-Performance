from django.contrib import admin
from userLogin.models import student_info, student_acc, admin_acc

admin.site.register(student_info)
admin.site.register(student_acc)
admin.site.register(admin_acc)