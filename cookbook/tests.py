from django.test import TestCase
from django.core.urlresolvers import reverse

from .models import Ingredient

def create_ingredient(name, stub, description):
    """Create basic ingredient

    """
    return Ingredient.objects.create(name=name,
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
