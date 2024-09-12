from django.contrib import admin
from SET.models import student_info, year_level, student_status, academic_year, subjects, department, professor_status, professor_info, professor_current_subjs, student_enrolled_subjs, programs, categories, feedback_questions, feedbacks, filtered_feedbacks, numerical_questions, numerical_ratings

admin.site.register(student_info)
admin.site.register(programs)
admin.site.register(year_level)
admin.site.register(student_status)
admin.site.register(academic_year)
admin.site.register(subjects)
admin.site.register(department)
admin.site.register(professor_status)
admin.site.register(professor_info)
admin.site.register(professor_current_subjs)
admin.site.register(student_enrolled_subjs)
admin.site.register(categories)
admin.site.register(numerical_questions)
admin.site.register(numerical_ratings)
admin.site.register(feedback_questions)
admin.site.register(feedbacks)
admin.site.register(filtered_feedbacks)

