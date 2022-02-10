from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import Student, Subject, Teacher
from django.db.models import F

# Create your views here.
def new_sub(request):
    s = Subject(sub_name= 'Art', about='Vision that artist put on Paper.')
    s.save()

# if you want to solve value error in browser just add
#return HttpResponse('<h1>Subject Created<h1>')

def update(request):
    s = Subject.objects.get(id=4)
    print(s)
    s.sub_name = "Artit"
    s.save()
  # error.


def modify(request):
    student = Student.objects.get(id=1)
    print(student)
    s = Subject.objects.get(sub_name="physical")
    print(s)
    #print(student.subject)
    student.subject = s
    student.save()
    #student = Student.objects.get(id=1)
    #print(student.subject)
    #  student.subject = s
    # student.save()

all_name = Student.objects.all()
print(all_name)

all = Subject.objects.all().filter(sub_name='Art')
print(all)

ex = Subject.objects.all().exclude(sub_name='physical')
print(ex)

limit= Subject.objects.all()[1:3]
print(limit)


#negative indexing is not supported
#negative_limit = Subject.objects.all()[:-1]
#print(negative_limit)



sit = Subject.objects.filter(sub_name__iexact="art")
print(sit)


sat= Subject.objects.filter(sub_name__exact='physical')
print(sat)


check =Subject.objects.filter(student__subject__sub_name__isnull=True)
print(check)


identify = Student.objects.filter(stu_name__gt=F('subject'))
print(identify)


#exa =Student.objects.filter(stu_name__gt=Min('subject'))


#pk lookup is useful with primary key

look = Subject.objects.get(pk=4)
print(look)


show = Teacher.objects.get(tech_name='Raj')
print('output of teacher=',show)

c = Student.objects.all().filter(subject_tech__tech_name='Raj')
print('output', c)

