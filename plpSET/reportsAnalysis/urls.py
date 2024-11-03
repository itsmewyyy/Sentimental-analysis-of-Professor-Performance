from django.urls import path
from .views import CollegeRatingsSummaryView, ProfessorRatingsSummaryView, ProfessorFeedbacks, professorPhrases, collegePhrases


urlpatterns = [
    path('college-ratings-summary/', CollegeRatingsSummaryView.as_view()),
    path('professor-ratings-summary/', ProfessorRatingsSummaryView.as_view()),
    path('professor-feedbacks/', ProfessorFeedbacks.as_view()),
    path('recurring-phrases/', professorPhrases.as_view()),
    path('recurring-college-phrases/', collegePhrases.as_view()),
]