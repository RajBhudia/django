from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import  Teacher, Student, Vehicle, Car

# Register your models here.

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['emp_no', 'name']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'teacher')

@admin.register(Vehicle)
class VechileAdmin(admin.ModelAdmin):
    list_display = ('reg_no', 'owner')

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['car_model', 'vehicle']