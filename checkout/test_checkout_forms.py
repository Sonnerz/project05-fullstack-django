from .forms import MakePaymentForm, OrderForm
from django.test import TestCase
from django.utils import timezone
from issues.models import Feature

# Create your tests here.


class TestOrderForm(TestCase):
    # Valid Form Data
    def test_OrderForm_valid(self):
        form = OrderForm(
            data={'full_name': 'name', 'phone_number': 'number',
                  'country': 'ireland', 'postcode': '123',
                  'town_or_city': 'Dublin', 'street_address1': 'street1',
                  'street_address2': 'street2', 'county': 'dublin'})
        self.assertTrue(form.is_valid())

    # Invalid Form Data
    def test_OrderForm_invalid(self):
        form = OrderForm(
            data={'full_name': ""})
        self.assertFalse(form.is_valid())
