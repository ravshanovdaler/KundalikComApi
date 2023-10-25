from rest_framework.generics import CreateAPIView
from .serializers import SchoolAdminSerializer
from .models import UserModel
from rest_framework.response import Response


class SignSchoolAdminView(CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = SchoolAdminSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {'message': 'You have signed up successfully'}
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
