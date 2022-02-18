from django.db import models


# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField(blank=False)
    email = models.CharField(max_length=100, null= True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name




class Product(models.Model):
    CATEGORIES =(
        ('Indor', 'Indor'),
        ('Outdor', 'Outdor'),
    )
    name = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.CharField(max_length=100, choices=CATEGORIES, default='')
    description = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name
        


class Order(models.Model):
    STATUS =(
        ('Pending', 'Pending'),
        ('out for delivery', 'Out for Delivery'),
        ('Deliverd', 'Deliverd'),
    )
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, choices=STATUS, default='')


    def __str__(self):
        return self.product.name









