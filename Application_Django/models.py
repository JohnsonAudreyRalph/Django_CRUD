from django.db import models

# Create your models here.
class Student(models.Model):
    Gender_choices = [
        ("Nam", "Nam"),
        ("Nữ", "Nữ"),
        ("Khác", "Khác")
    ]
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(choices=Gender_choices, max_length=10)