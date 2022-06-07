from django.db import models


# Create your models here.
class Room(models.Model):
    roomNo = models.IntegerField() 

    def __str__(self) -> str:
        return str(self.roomNo)

class Guest(models.Model):
    name = models.CharField(max_length=40)
    room = models.OneToOneField(Room, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self) -> str:
        return self.name

class Framework(models.Model):
    name = models.CharField(max_length=25)
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.name

