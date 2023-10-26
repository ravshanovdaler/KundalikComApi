from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from .serializers import SchoolAdminSerializer, TeacherSerializer, StudentsSignupSerializer
from .models import UserModel
from rest_framework.response import Response
from rest_framework import status


class SignSchoolAdminUpView(CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = SchoolAdminSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {'message': 'You have signed up successfully'}
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SignTeacherUpView(CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = TeacherSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {'message': 'You have signed up successfully'}
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentsSignupView(CreateAPIView):
    serializer_class = StudentsSignupSerializer  # Remove queryset, as it's not needed for file uploads

    def create(self, request, *args, **kwargs):
        file_serializer = StudentsSignupSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.create(file_serializer.validated_data)  # Call the create method to process the file
            response = {'message': 'Students have been signed up successfully'}
            return Response(data=response, status=status.HTTP_201_CREATED)
        else:
            return Response(data=file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)