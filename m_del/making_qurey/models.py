from django.db import models
from datetime import date

# Create your models here.
class Subject (models.Model):
    sub_name = models.CharField(max_length=60)
    about = models.TextField()

    def __str__(self):
        return self.sub_name

class Teacher(models.Model):
    tech_name = models.CharField(max_length=100)
    tech_contact = models.IntegerField()

    def __str__(self):
        return self.tech_name

class Student(models.Model):
    stu_name = models.CharField(max_length=100)
    stu_id = models.IntegerField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    subject_tech = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.stu_name

    def teach_by(self):
     return ",".join([str(p) for p in self.subject_tech.all()])