from django.contrib import admin
from .models import Teacher, Student, Subject

# Register your models here.
@admin.register(Teacher)
class teacheradmin(admin.ModelAdmin):
    list_display = ('tech_name', 'tech_contact')

@admin.register(Subject)
class subjectadmin(admin.ModelAdmin):
    list_display = ('sub_name', 'about')

@admin.register(Student)
class studentadmin(admin.ModelAdmin):
    list_display = ('stu_name', 'stu_id', 'subject', 'subject_tech')