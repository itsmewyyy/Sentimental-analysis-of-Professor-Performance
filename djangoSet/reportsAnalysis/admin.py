from django.contrib import admin
from reportsAnalysis.models import filtered_feedbacks, training_data, processed_feedbacks

admin.site.register(filtered_feedbacks)
admin.site.register(training_data)
admin.site.register(processed_feedbacks)