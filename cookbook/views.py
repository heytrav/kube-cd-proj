from django.views import generic
from django.conf import settings

from .models import Meal, Ingredient
from .forms import IngredientForm


class IndexView(generic.ListView):

    template_name = 'cookbook/index.html'
    context_object_name = 'meal_list'

    def get_context_data(self, **kwargs):
        """Return the context data

        :**kwargs: arguments
        :returns: context object for view

        """
        context = super(IndexView, self).get_context_data(**kwargs)
        context['version'] = settings.VERSION
        return context

    def get_queryset(self):
        return Meal.objects.all()


class IngredientsView(generic.ListView):
    template_name = 'cookbook/ingredients.html'

    def get_context_data(self, **kwargs):
        """Return the context data

        :**kwargs: arguments
        :returns: context object for view

        """
        context = super(IngredientsView, self).get_context_data(**kwargs)
        context['version'] = settings.VERSION
        return context

    def get_queryset(self):
        return Ingredient.objects.all()




class IngredientEditView(generic.edit.FormView):
    template_name = 'cookbook/ingredients.html'
    form_class = IngredientForm
    success_url = '/success/'
