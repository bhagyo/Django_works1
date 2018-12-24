from django.urls import path

from . import views

urlpatterns = [
    path('divisions/', views.division_list, name='divisions'),
    path('districts/', views.district_list, name='districts'),
    path('districts/<int:div_id>', views.dists_of_division, name='dists_of_division'),
]
