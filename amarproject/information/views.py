from django.shortcuts import render
# Create your views here.
from .models import Districts
from .models import Divisions


def district_list(request):
    districts = Districts.objects.all()
    context = {'districts': districts}
    return render(request, 'information/districts.html', context)


def division_list(request):
    divisions = Divisions.objects.all()
    context = {'divisions': divisions}
    return render(request, 'information/division_list.html', context)


def dists_of_division(request, div_id):
    divisions = Divisions.objects.get(pk=div_id)
    districts = Districts.objects.filter(division=divisions)
    context = {'divisions': divisions, 'districts': districts}
    return render(request, 'information/dists_of_division.html', context)
