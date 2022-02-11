from concurrent.futures.process import _threads_wakeups
from curses.ascii import alt
from sre_constants import CATEGORY
from traceback import print_exception
from unicodedata import category
from django.db import models


# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField(blank=False)
    email = models.CharField(max_length=100, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)


class Product(models.Model):
    CATEGORY = (
                ('Indor', 'Indor'), 
                ('Outdoor', 'Outdoor')
    
                )
    name = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.CharField(max_length=100, choices=CATEGORY)
    description = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)




