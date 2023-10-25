from django.urls import path
from .views import SignSchoolAdminView

urlpatterns = [
    path('', SignSchoolAdminView.as_view())
]