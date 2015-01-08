from django.contrib import admin

# Register your models here.

from django.contrib import admin
from food.models import FoodStuff, FoodEntry, DayTotal, MonthTotal, YearTotal

admin.site.register(FoodEntry)
admin.site.register(FoodStuff)

admin.site.register(DayTotal)
admin.site.register(MonthTotal)
admin.site.register(YearTotal)
