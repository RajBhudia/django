from django.contrib import admin
from .models import Product, Customer 

# Register your models here.
@admin.register(Customer)
class customeradmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'email', 'date_created')

@admin.register(Product)
class productadmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'description', 'price', 'date_created')