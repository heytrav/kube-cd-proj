from django.views import generic
from django.conf import settings
from django.core.urlresolvers import reverse_lazy

from .models import Meal, Ingredient, Measurement


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


class IngredientCreate(generic.edit.CreateView):
    model = Ingredient
    fields = ['name', 'stub', 'description']
    success_url = reverse_lazy('cookbook:ingredients')

    def get_context_data(self, **kwargs):
        """Return the context data

        :**kwargs: arguments
        :returns: context object for view

        """
        context = super(IngredientCreate, self).get_context_data(**kwargs)
        context['version'] = settings.VERSION
        return context


class IngredientUpdate(generic.edit.UpdateView):
    model = Ingredient
    fields = ['name', 'stub', 'description']
    success_url = reverse_lazy('cookbook:ingredients')

    def get_context_data(self, **kwargs):
        """Return the context data

        :**kwargs: arguments
        :returns: context object for view

        """
        context = super(IngredientUpdate, self).get_context_data(**kwargs)
        context['version'] = settings.VERSION
        return context


class IngredientDelete(generic.edit.DeleteView):
    model = Ingredient
    success_url = reverse_lazy('cookbook:ingredients')


class MeasurementView(generic.ListView):

    """Display measurement set"""

    template_name = "cookbook/measurements.html"

    def get_context_data(self, **kwargs):
        """Return the context data

        :**kwargs: arguments
        :returns: context object for view

        """
        context = super().get_context_data(**kwargs)
        context['version'] = settings.VERSION
        return context

    def get_queryset(self):
        """Return set of measurements.
        :returns: list of measurements

        """
        return Measurement.objects.all()



class MeasurementCreate(generic.edit.CreateView):

    """Create a measurement object."""
    model = Measurement
    fields = ['name', 'stub', 'description']
    success_url = reverse_lazy('cookbook:measurements')

    def get_context_data(self, **kwargs):
        """Return the context data

        :**kwargs: arguments
        :returns: context object for view

        """
        context = super().get_context_data(**kwargs)
        context['version'] = settings.VERSION
        return context



class MeasurementEdit(generic.edit.UpdateView):

    """Edit measurements"""
    model = Measurement
    fields = ['name', 'stub', 'description']
    success_url = reverse_lazy('cookbook:measurements')

    def get_context_data(self, **kwargs):
        """Return the context data

        :**kwargs: arguments
        :returns: context object for view

        """
        context = super().get_context_data(**kwargs)
        context['version'] = settings.VERSION
        return context



class MeasurementDelete(generic.edit.DeleteView):

    """Delete a measurement from list."""
    model = Measurement
    success_url = reverse_lazy('cookbook:measurements')


