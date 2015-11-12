from django.db import models
from django.core.urlresolvers import reverse


class Meal(models.Model):

    name = models.CharField(max_length=500)
    stub = models.CharField(max_length=500)
    instructions = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Ingredient(models.Model):

    name = models.CharField(max_length=500)
    stub = models.CharField(max_length=500)
    description = models.TextField(blank=True)

    def get_absolute_url(self):
        return reverse('cookbook:edit_ingredient', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class Measurement(models.Model):
    name = models.CharField(max_length=500)
    stub = models.CharField(max_length=500)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    meal = models.ForeignKey(Meal)
    ingredient = models.ForeignKey(Ingredient)
    quantity = models.FloatField()
    measurement = models.ForeignKey(Measurement)
