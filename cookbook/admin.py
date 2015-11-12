from django.contrib import admin

from .models import Meal, Ingredient, Measurement, Recipe


admin.site.register(Meal)
admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(Measurement)
