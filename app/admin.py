from django.contrib import admin
from .models import Employee , Person , Profile,Address , CarModel , FuelType
# Register your models here.

admin.site.register([Employee , Person , Profile,Address , CarModel , FuelType])
