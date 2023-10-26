from django.urls import path
from .views import SignSchoolAdminUpView, SignTeacherUpView, StudentsSignupView

urlpatterns = [
    path('signup/schooladmin/', SignSchoolAdminUpView.as_view()),
    path('signup/teacher/', SignTeacherUpView.as_view()),
    path('signup/students/', StudentsSignupView.as_view()),
]
