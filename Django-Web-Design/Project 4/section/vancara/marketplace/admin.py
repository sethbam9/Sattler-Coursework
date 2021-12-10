from django.contrib import admin

# Register your models here.
from .models import Make, Type, Vehicle

admin.site.register(Make)
admin.site.register(Type)
admin.site.register(Vehicle)
