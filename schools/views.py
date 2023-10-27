from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from .models import ClassesModel, SchoolsModel
from .serializers import SchoolSerializer, ClassesSerializer
from users.permissions import IsSchoolAdmin


class SchoolInfoView(RetrieveAPIView):
    queryset = SchoolsModel.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = [IsSchoolAdmin, ]


class ClassesCreate(CreateAPIView):
    queryset = ClassesModel.objects.all()
    serializer_class = ClassesSerializer
    permission_classes = [IsSchoolAdmin, ]
