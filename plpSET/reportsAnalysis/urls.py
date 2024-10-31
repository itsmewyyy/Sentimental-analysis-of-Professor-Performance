from django.urls import path
from .views import CollegeRatingsSummary, ProfessorRatingsSummary, ProfessorFeedbacks, recurringPhrases, collegePhrases


urlpatterns = [
    path('college-ratings-summary/', CollegeRatingsSummary.as_view()),
    path('professor-ratings-summary/', ProfessorRatingsSummary.as_view()),
    path('professor-feedbacks/', ProfessorFeedbacks.as_view()),
    path('recurring-phrases/', recurringPhrases.as_view()),
    path('recurring-college-phrases/', collegePhrases.as_view()),
]