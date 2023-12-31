# Generated by Django 4.2.6 on 2023-10-26 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0004_alter_classesmodel_grade_alter_classesmodel_school'),
        ('users', '0003_alter_usermodel_adress_alter_usermodel_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='classstudying',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='students', to='schools.classesmodel'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='user_type',
            field=models.CharField(choices=[('student', 'Student'), ('superadmin', 'Super admin'), ('school admin', 'Schooladmin'), ('teacher', 'Teacher')], max_length=256),
        ),
    ]
