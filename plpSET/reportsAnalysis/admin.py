from django.contrib import admin
from reportsAnalysis.models import filtered_feedbacks, training_data, processed_feedbacks, feedback_summary, numerical_summary

admin.site.register(filtered_feedbacks)
admin.site.register(training_data)
admin.site.register(processed_feedbacks)
admin.site.register(feedback_summary)
admin.site.register(numerical_summary)