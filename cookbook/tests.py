from django.test import TestCase
from django.core.urlresolvers import reverse


class IngredientViewTests(TestCase):

    def test_index_view_with_no_ingredients(self):
        response = self.client.get(reverse('cookbook:ingredients'))
        self.assertContains(response, 'No ingredients available.')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['ingredient_list'], [])
