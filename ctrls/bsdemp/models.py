from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Employee(models.Model):
    name= models.CharField(max_length=100)
    role=models.CharField(max_length=25)
    age=models.IntegerField( max_length=2)
    photo=models.CharField(max_length=200)

    def __str__(self):
         return self.name



