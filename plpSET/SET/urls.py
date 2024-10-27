from django.urls import path
from .views import CategoriesAndQuestionsView, FeedbackQuestionsView, CollegeListView, SectionStudentsView, SubmitRatingsView, EnrolledSubjsView



urlpatterns = [
    path('categories-and-questions/', CategoriesAndQuestionsView.as_view(), name='categories-and-questions'),
    path('feedback-questions/', FeedbackQuestionsView.as_view(), name='feedback-questions'),
    path('colleges/', CollegeListView.as_view(), name='college-list'),
    path('section/<str:section_id>/', SectionStudentsView.as_view(), name='section-students'),
    path('submit-ratings/', SubmitRatingsView.as_view(), name='submit-ratings'),
    path('enrolled_subjs/<str:student_id>/', EnrolledSubjsView.as_view(), name='enrolled-subjects'),

]