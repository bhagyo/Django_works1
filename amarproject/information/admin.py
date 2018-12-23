from django.contrib import admin
from .models import Divisions
from .models import Districts
# Register your models here.

admin.site.register(Divisions)


class DistrictAdmin(admin.ModelAdmin):
    list_display = ('name', 'division', 'visited', 'population_density')


admin.site.register(Districts, DistrictAdmin)
