from argparse import _MutuallyExclusiveGroup
from tkinter import CASCADE
from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=50)
    password = models.IntegerField()

class Hobby(models.Model):
    #person = models.ForeignKey(Person, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.PROTECT)
    #person = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True)
    hobby1 = models.CharField(max_length=50)
    hobby2 = models.CharField(max_length=50)
    hobby3 = models.CharField(max_length=50)
    

