from django import forms
from .models import (
    # Recipe,
    Ingredient,
    # Measurement,
    # Meal
)


class IngredientForm(forms.ModelForm):

    """Manage ingredients."""

    class Meta:
        model = Ingredient
        fields = ['name', 'stub', 'description']
