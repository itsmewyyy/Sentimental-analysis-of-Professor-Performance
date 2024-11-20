from django.urls import path
from .views import RegisterView, LoginView, LoginAdmin, LogoutAdmin, LogoutView, StudentsCount, EditView, ProfRegisterView, LoginProf, LogoutProf
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', ProfRegisterView.as_view(), name='register'),
    path('profregister/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('adminLogin/', LoginAdmin.as_view()),
    path('adminLogout/', LogoutAdmin.as_view()),
    path('profLogin/', LoginProf.as_view()),
    path('profLogout/', LogoutProf.as_view()),
    path('studentLogout/', LogoutView.as_view()),
    path('students-summary/', StudentsCount.as_view()),
    path('student-acc/<str:student_id>/', EditView.as_view())
    
]
