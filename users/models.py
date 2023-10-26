from django.db import models
from django.contrib.auth.models import AbstractUser
from schools.subjects import SUBJECTS_LIST
from schools.models import ClassesModel, SchoolsModel


class UserModel(AbstractUser):
    USER_TYPE = [
        ('student', 'Student',),
        ('superadmin', 'Super admin'),
        ('school admin', 'Schooladmin'),
        ('teacher', 'Teacher'),
    ]
    user_type = models.CharField(max_length=256, choices=USER_TYPE)
    date_of_birth = models.DateField(null=True)
    phone_number = models.BigIntegerField(null=True)
    adress = models.CharField(max_length=200, null=True)

    # STUDENTS

    dads_first_name = models.CharField(max_length=50, blank=True, null=True)
    moms_first_name = models.CharField(max_length=50, blank=True, null=True)
    dads_last_name = models.CharField(max_length=50, blank=True, null=True)
    moms_last_name = models.CharField(max_length=50, blank=True, null=True)
    parents_phone_number = models.BigIntegerField(null=True, blank=True)
    classstudying = models.ForeignKey(ClassesModel, on_delete=models.SET_NULL, related_name='students', blank=True,
                                      null=True)
    # TEACHERS

    subject = models.CharField(max_length=50, choices=SUBJECTS_LIST, blank=True, null=True)
    class_leader = models.ForeignKey(ClassesModel, on_delete=models.SET_NULL, related_name='class_leader', blank=True,
                                     null=True, limit_choices_to={'school': models.F('school')}, )
    school = models.ForeignKey(SchoolsModel, on_delete=models.CASCADE, blank=True, null=True, related_name='teachers')
    classes = models.ManyToManyField(ClassesModel, related_query_name='teacher', blank=True,
                                     limit_choices_to={'school': models.F('school')}, )

    # school admins

    school = models.ForeignKey(SchoolsModel, on_delete=models.CASCADE, blank=True, null=True,
                               related_name='school_admin', )
