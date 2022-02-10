from django.contrib import admin
from .models import Hobby, Person

# Register your models here.
@admin.register(Person)
class personadmin(admin.ModelAdmin):
    list_display = ('name', 'password')

@admin.register(Hobby)
class hobbyadmin (admin.ModelAdmin):
    list_display = ('hobby1', 'hobby2', 'hobby3', 'person')