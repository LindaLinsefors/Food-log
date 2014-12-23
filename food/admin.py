from django.contrib import admin

# Register your models here.

from django.contrib import admin
from food.models import FoodStuff, FoodEntry

admin.site.register(FoodEntry)
admin.site.register(FoodStuff)
