from django.db import models


class SchoolsModel(models.Model):
    CITY_CHOICES = [
        ('Andijan', 'Andijan'),
        ('Bukhar', 'Bukhar'),
        ('Fergana', 'Fergana'),
        ('Jizzakh', 'Jizzakh'),
        ('Karshi', 'Karshi'),
        ('Navoiy', 'Navoiy'),
        ('Namangan', 'Namangan'),
        ('Nukus', 'Nukus'),
        ('Samarkand', 'Samarkand'),
        ('Termez', 'Termez'),
        ('Urgench', 'Urgench'),
        ('Tashkent', 'Tashkent'),
    ]

    number = models.BigIntegerField()
    city = models.CharField(max_length=100, choices=CITY_CHOICES, null=True)
    location = models.CharField(max_length=200)
    director = models.CharField(max_length=100)
    opening_date = models.DateField()

    def __str__(self):
        return f"{self.number}-school"


class ClassesModel(models.Model):
    GRADES_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (8, '7'),
        (9, '8'),
        (10, '10'),
        (11, '11'),
    ]
    grade = models.PositiveIntegerField(choices=GRADES_CHOICES)
    name = models.CharField(max_length=1)
    school = models.ForeignKey(SchoolsModel, on_delete=models.CASCADE, null=True, related_name='classes')

    def __str__(self):
        return f"{self.grade}-{self.name}"
