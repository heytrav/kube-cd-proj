from django.test import TestCase
from django.core.urlresolvers import reverse

from .models import Ingredient, Measurement

def create_ingredient(name, stub, description):
    return Ingredient.objects.create(name=name,
                                     stub=stub,
                                     description=description)

def create_measurement(name, stub, description):
    return Measurement.objects.create(name=name,
                                      stub=stub,
                                      description=description)



class IngredientViewTests(TestCase):

    def test_index_view_with_no_ingredients(self):
        response = self.client.get(reverse('cookbook:ingredients'))
        self.assertContains(response, 'No ingredients available.')
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['ingredient_list'], [])

    def test_ingredient_list_view_with_results(self):
        create_ingredient('Onion', 'onion', 'Onions')
        create_ingredient('Garlic', 'garlic', 'Goes with everything.')
        response = self.client.get(reverse('cookbook:ingredients'))
        self.assertContains(response, 'Goes with everything.')
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['ingredient_list'].order_by('stub'),
                                 ['<Ingredient: Garlic>',
                                  '<Ingredient: Onion>'])


class IngredientCreate(TestCase):

    """Test creating ingredients"""

    def test_create_ingredient(self):
        response = self.client.post(reverse('cookbook:create_ingredient'),
                                    {'name': 'Parsely',
                                     'stub': 'parsely',
                                     'description': 'Green stuff'})
        # Should redirect to ingredients page
        self.assertEqual(response.status_code, 302)


class MeasurementViewList(TestCase):

    """Test display of measurements"""

    def test_measurement_list_no_results(self):
        response = self.client.get(reverse('cookbook:measurements'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No measurements available.')
        self.assertQuerysetEqual(response.context['measurement_list'],
                                 [])

    def test_measurement_list(self):
        create_measurement('Fluid Ounce', 'floz', 'Fluid ounce is stupid.')
        create_measurement('Ounce', 'oz', 'Yey, an ounce!')
        response = self.client.get(reverse('cookbook:measurements'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Fluid ounce is stupid.')
        self.assertQuerysetEqual(
            response.context['measurement_list'].order_by('stub'),
            ['<Measurement: Fluid Ounce>',
             '<Measurement: Ounce>']
        )


class MeasurementCreate(TestCase):

    """Test creating measurements"""

    def test_create_measurement(self):
        response = self.client.post(reverse('cookbook:create_measurement'),
                                    {'name': 'Fluid Ounce',
                                     'stub': 'floz',
                                     'description': 'Fluid ounce is stupid.'})
        self.assertEqual(response.status_code, 302)


