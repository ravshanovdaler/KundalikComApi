from django.urls import path
from .views import SchoolInfoView, ClassesCreate

urlpatterns = [
    path('<int:pk>/', SchoolInfoView.as_view()),
    path('createclass/', ClassesCreate.as_view()),
]
