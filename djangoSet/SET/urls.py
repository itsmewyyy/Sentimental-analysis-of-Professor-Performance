from django.urls import path
from .views import CategoriesAndQuestionsView, FeedbackQuestionsView, CollegeListView



urlpatterns = [
    path('categories-and-questions/', CategoriesAndQuestionsView.as_view(), name='categories-and-questions'),
    path('feedback-questions/', FeedbackQuestionsView.as_view(), name='feedback-questions'),
    path('colleges/', CollegeListView.as_view(), name='college-list'),
]