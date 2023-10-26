from rest_framework import serializers
from .models import UserModel
from rest_framework.validators import ValidationError
from rest_framework.authtoken.models import Token
from schools.models import ClassesModel
import pandas as pd
from datetime import datetime
import random
import string
from .password import generate_password

class SchoolAdminSerializer(serializers.ModelSerializer):
    user_type = serializers.ChoiceField(choices=UserModel.USER_TYPE)
    password = serializers.CharField(min_length=8, write_only=True, style={'input_type': 'password'})
    password2 = serializers.CharField(min_length=8, write_only=True, style={'input_type': 'password'})

    class Meta:
        model = UserModel
        fields = (
            'password', 'password2', 'first_name', 'last_name', 'email', 'username', 'adress', 'school', 'phone_number',
            'user_type')

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


class TeacherSerializer(serializers.ModelSerializer):
    user_type = serializers.ChoiceField(choices=UserModel.USER_TYPE)
    password = serializers.CharField(min_length=8, write_only=True, style={'input_type': 'password'})
    password2 = serializers.CharField(min_length=8, write_only=True, style={'input_type': 'password'})

    # Define custom fields for 'classes' and 'class_leader'
    classes = serializers.PrimaryKeyRelatedField(
        queryset=ClassesModel.objects.all(),  # Initially include all classes
        required=False  # Make the field optional
    )
    class_leader = serializers.PrimaryKeyRelatedField(
        queryset=UserModel.objects.filter(user_type='teacher'),
        required=False
    )

    class Meta:
        model = UserModel
        fields = (
            'password', 'password2', 'first_name', 'last_name', 'email', 'username', 'adress', 'school', 'phone_number',
            'user_type', 'subject', 'class_leader', 'classes')
        extra_kwargs = {
            'class_leader': {'required': False},
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customize the 'classes' queryset based on the user's school
        if 'request' in self.context and self.context['request'].user.school:
            self.fields['classes'].queryset = ClassesModel.objects.filter(school=self.context['request'].user.school)

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


class StudentsSignupSerializer(serializers.Serializer):
    file = serializers.FileField()

    class Meta:
        fields = "__all__"

    def create(self, validated_data):
        excel = validated_data['file']  # Access the 'file' field from validated_data

        # Read data from the Excel file using pandas
        df = pd.read_excel(excel, usecols=['first name', 'date of birth', 'last name', 'phone number', 'adress',
                                           'dads first name', 'dads last name', 'moms first name', 'moms last name',
                                           'parents phone number', 'grade', 'class'])

        for index, row in df.iterrows():
            # Extract data from the Excel file
            student_data = {
                'first_name': row['first name'],
                'last_name': row['last name'],
                'phone_number': row['phone number'],
                'adress': row['adress'],
                'dads_first_name': row['dads first name'],
                'dads_last_name': row['dads last name'],
                'moms_first_name': row['moms first name'],
                'moms_last_name': row['moms last name'],
                'parents_phone_number': row['parents phone number'],
            }

            # Handle the date format conversion from 'YYYY.MM.DD' to 'YYYY-MM-DD'
            date_of_birth = row['date of birth']
            try:
                date_of_birth = datetime.strptime(date_of_birth, '%Y.%m.%d').strftime('%Y-%m-%d')
            except ValueError:
                raise ValidationError(f"Invalid date format for '{date_of_birth}'. It must be in 'YYYY.MM.DD' format.")
                continue  # Move to the next row

            student_data['date_of_birth'] = date_of_birth

            # Extract class details
            grade = row['grade']
            name = row['class']

            try:
                class_instance = ClassesModel.objects.get(name=name, grade=grade)
            except ClassesModel.DoesNotExist:
                raise ValidationError(f"Class '{grade}-{name}' does not exist.")
                continue

            student_data['classstudying'] = class_instance

            def generate_random_string(length=6):
                characters = string.ascii_letters + string.digits
                return ''.join(random.choice(characters) for _ in range(length))
            username = row['first name'] + row['last name'] + generate_random_string()
            password = generate_password()
            while UserModel.objects.filter(username=username).exists():
                username = row['first name'] + row['last name'] + generate_random_string()

            user = UserModel(username=username, **student_data, password=password)
            user.save()
            return user