from __future__ import unicode_literals

from __future__ import unicode_literals

from django.db import models
from django.forms.extras import widgets

# Create your models here.


class Employee(models.Model):
    fname= models.CharField(max_length=100)
    lname= models.CharField(max_length=100)
    role=models.CharField(max_length=25)
    age=models.CharField( max_length=2)
    photo=models.CharField(max_length=200, null = True)
    zipcode=models.CharField(max_length=5)
    birth_date = models.DateField(null=True)

    def __str__(self):
         return self.fname, self.lname, self.zipcode, self.birth_date







