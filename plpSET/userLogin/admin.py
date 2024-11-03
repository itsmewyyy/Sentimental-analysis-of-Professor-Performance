from django.contrib import admin
from userLogin.models import student_acc, admin_acc
from django.contrib.sessions.models import Session


admin.site.register(student_acc)
admin.site.register(admin_acc)

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ['session_key', 'session_data', 'expire_date']