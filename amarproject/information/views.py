from django.shortcuts import render
# Create your views here.
from .models import Districts


def district_list(request):
    districts = Districts.objects.all()
    context = {'districts': districts}
    return render(request, 'information/districts.html', context)
