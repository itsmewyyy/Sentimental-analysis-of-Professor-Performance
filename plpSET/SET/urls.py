from django.urls import path
from .views import CategoriesAndQuestionsView, FeedbackQuestionsView, CollegeListView, SectionStudentsView, SubmitRatingsView, EnrolledSubjsView, AdminListView, ProfessorListView, DepartmentListView, ProgramListView, SectionListView, SubjectListView, NumericalCategoryView, NumericalQuestionsView


urlpatterns = [
    path('categories-and-questions/', CategoriesAndQuestionsView.as_view(), name='categories-and-questions'),
    path('feedback-questions/', FeedbackQuestionsView.as_view(), name='feedback-questions'),
    path('colleges/', CollegeListView.as_view(), name='college-list'),
    path('section/<str:section_id>/', SectionStudentsView.as_view(), name='section-students'),
    path('submit-ratings/', SubmitRatingsView.as_view(), name='submit-ratings'),
    path('enrolled_subjs/<str:student_id>/', EnrolledSubjsView.as_view(), name='enrolled-subjects'),
    path('admin-list/', AdminListView.as_view(), name='admin-list'),
    path('professor-list/', ProfessorListView.as_view(), name='professor-list'),
    path('department-list/', DepartmentListView.as_view(), name='department-list'),
    path('program-list/', ProgramListView.as_view(), name='program-list'),
    path('section-list/', SectionListView.as_view(), name='section-list'),
    path('subject-list/', SubjectListView.as_view(), name='subject-list'),
    path('numerical-categories/', NumericalCategoryView.as_view(), name='category-list'),
    path('numerical-questions/', NumericalQuestionsView.as_view(), name='numerical-questions'),
]