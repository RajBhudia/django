from django.contrib import admin
from .models import  Customer, Product, Order, Tag

# Register your models here.
@admin.register(Customer)
class customeradmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'email', 'date_created')


@admin.register(Product)
class productadmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'description', 'date_created')


admin.site.register(Tag)

@admin.register(Order)
class orderadmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'product', 'date_created', 'status')



    