from django.urls import path
from .views import CollegeRatingsSummary, ProfessorRatingsSummary, ProfessorFeedbacks


urlpatterns = [
    path('college-ratings-summary/', CollegeRatingsSummary.as_view()),
    path('professor-ratings-summary/', ProfessorRatingsSummary.as_view()),
    path('professor-feedbacks/', ProfessorFeedbacks.as_view()),
]