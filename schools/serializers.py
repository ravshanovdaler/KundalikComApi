from rest_framework import serializers
from .models import SchoolsModel, ClassesModel
from users.serializers import StudentsSignupSerializer, SchoolAdminSerializer, TeacherSerializer


class ClassesSerializer(serializers.ModelSerializer):
    class_leader = TeacherSerializer(many=True, read_only=True)

    class Meta:
        model = ClassesModel
        fields = '__all__'


class SchoolSerializer(serializers.ModelSerializer):
    classes = ClassesSerializer(many=True, read_only=True)
    school_admin = SchoolAdminSerializer(many=True, read_only=True)
    students = StudentsSignupSerializer(many=True, read_only=True)

    class Meta:
        model = SchoolsModel
        fields = '__all__'
