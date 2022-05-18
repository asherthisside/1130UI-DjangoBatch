from django.db import models

# Create your models here.

class Student(models.Model): 
    student_name = models.CharField(max_length=35)
    age = models.IntegerField()
    address = models.TextField()

    def __str__(self):
        return self.student_name + ", " + self.address

class Faculty(models.Model):
    faculty_name = models.CharField(max_length=40)
    qualification = models.CharField(max_length=20)
    salary = models.FloatField()

    def __str__(self):
        return self.faculty_name 

# Create a model(for a product) using following fields: id, name, price, discount, description