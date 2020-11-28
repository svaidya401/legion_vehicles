from django.contrib import admin
from bikes_app.models import Bikes,BikeManufacturers,BikeDetails
# Register your models here.

admin.site.register(Bikes)
admin.site.register(BikeManufacturers)
admin.site.register(BikeDetails)
