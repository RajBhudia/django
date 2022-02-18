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
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
	CATEGORY = (
			('Indoor', 'Indoor'),
			('Out Door', 'Out Door'),
			) 

	name = models.CharField(max_length=200, null=True)
	price = models.FloatField(null=True)
	category = models.CharField(max_length=200, null=True, choices=CATEGORY)
	description = models.CharField(max_length=200, null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	tags = models.ManyToManyField(Tag)

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
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=100, choices=STATUS, default='')
    note = models.CharField(max_length=1000, null=True)


    def __str__(self):
        return self.product.name









	







