
from django.db import models
# Create your models here.



#2 fields
class Teacher(models.Model): 
    emp_no =models.IntegerField()
    name = models.CharField(max_length=30)
  

class Student(models.Model):
    teacher = models.OneToOneField(Teacher,
         on_delete = models.CASCADE, primary_key = True)
    student_name = models.CharField(max_length= 40)
    des = models.TextField(blank=True, null=True)
  


class Vehicle(models.Model):
	reg_no = models.IntegerField()
	owner = models.CharField(max_length = 100)

class Car(models.Model):
	vehicle = models.OneToOneField(Vehicle,
		on_delete = models.CASCADE, primary_key = True)
	car_model = models.CharField(max_length = 100)



