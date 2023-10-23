from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from .models import ClassesModel, SchoolsModel
from .serializers import SchoolSerializer, ClassesSeializer


class SchoolInfoView(RetrieveAPIView):
    queryset = SchoolsModel.objects.all()
    serializer_class = SchoolSerializer


class ClassesCreate(CreateAPIView):
    queryset = ClassesModel.objects.all()
    serializer_class = ClassesSeializer

