from django.contrib import admin
from userLogin.models import student_acc, admin_acc


admin.site.register(student_acc)
admin.site.register(admin_acc)
