# Generated by Django 4.2.6 on 2023-10-23 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0002_alter_classesmodel_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='classesmodel',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='schools.schoolsmodel'),
        ),
        migrations.AddField(
            model_name='schoolsmodel',
            name='city',
            field=models.CharField(choices=[('Andijan', 'Andijan'), ('Bukhar', 'Bukhar'), ('Fergana', 'Fergana'), ('Jizzakh', 'Jizzakh'), ('Karshi', 'Karshi'), ('Navoiy', 'Navoiy'), ('Namangan', 'Namangan'), ('Nukus', 'Nukus'), ('Samarkand', 'Samarkand'), ('Termez', 'Termez'), ('Urgench', 'Urgench'), ('Tashkent', 'Tashkent')], max_length=100, null=True),
        ),
    ]
