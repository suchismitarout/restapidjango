from django.db import models


# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.name
