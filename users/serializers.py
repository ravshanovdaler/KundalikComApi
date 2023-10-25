from rest_framework import serializers
from .models import UserModel
from rest_framework.validators import ValidationError
from rest_framework.authtoken.models import Token


class SchoolAdminSerializer(serializers.ModelSerializer):
    usertype = serializers.ChoiceField(choices=UserModel.USER_TYPE)
    password = serializers.CharField(min_length=8, write_only=True, style={'input_type': 'password'})
    password2 = serializers.CharField(min_length=8, write_only=True, style={'input_type': 'password'})

    class Meta:
        model = UserModel
        fields = (
            'password', 'password2', 'first_name', 'last_name', 'email', 'username', 'adress', 'school', 'phone_number',
            'usertype')

    def validate(self, attrs):
        user_exists = UserModel.objects.filter(username=attrs['username']).exists()
        if user_exists:
            raise ValidationError('User already exists')
        password = attrs.get('password')
        password2 = attrs.get('password2')

        if password != password2:
            raise ValidationError('Passwords do not match')

        return super().validate(attrs)

    def create(self, validated_data):
        password = validated_data.pop('password')
        password2 = validated_data.pop('password2')
        if password != password2:
            raise ValidationError('Passwords do not match')
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        Token.objects.create(user=user)
        return user
