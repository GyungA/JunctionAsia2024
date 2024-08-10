from django import forms
from .models import Food, Ingredient

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['name', 'ingredients', 'kcal']

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'potential_risk', 'attract_reason']
