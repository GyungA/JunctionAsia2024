from django.contrib import admin
from .models import Ingredient, Food, PotentialRisk

admin.site.register(Ingredient)
admin.site.register(Food)
admin.site.register(PotentialRisk)
