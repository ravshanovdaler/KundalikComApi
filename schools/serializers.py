from rest_framework.serializers import ModelSerializer
from .models import SchoolsModel, ClassesModel


class ClassesSeializer(ModelSerializer):
    class Meta:
        model = ClassesModel
        fields = '__all__'


class SchoolSerializer(ModelSerializer):
    classes = ClassesSeializer(many=True, read_only=True)

    class Meta:
        model = SchoolsModel
        fields = '__all__'
