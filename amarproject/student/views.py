from django.shortcuts import render
from .models import Students
# Create your views here.


def page1(request1):
    all_stu = Students.objects.all()
    return render(request1, 'another.html', {'all_stu_list': all_stu})
