from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=40)
    std = models.IntegerField()
    gender = models.CharField(max_length=10)
    address = models.TextField()