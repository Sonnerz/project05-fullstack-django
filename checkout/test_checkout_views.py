from django.test import TestCase
from .views import *
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.test.client import Client
from django.urls import resolve

# Create your tests here.


class TestViews(TestCase):
    def setUp(self):
        self.c = Client()
        self.user = User.objects.create_user(
            username="test", email="test@test.com", password="test")
        url = reverse('checkout')
        self.response = self.client.get(url)

    # CHECKOUT PAGE
    def test_get_checkout_page(self):
        response = self.c.get(reverse('checkout'))
        # 302 error because @login_required
        self.assertEqual(response.status_code, 302)
        # fake login
        self.c.login(username='test', password='test')
        # 200 error because logged in
        response = self.c.get(reverse('checkout'))
        self.assertEqual(response.status_code, 200)

    def test_form_has_csrf(self):
        self.c.login(username='test', password='test')
        response = self.c.get(reverse('checkout'))
        self.assertContains(response, 'csrfmiddlewaretoken')

    def test_page_contains_form(self):
        self.c.login(username='test', password='test')
        response = self.c.get(reverse('checkout'))
        orderform = response.context.get('order_form')
        paymentform = response.context.get('payment_form')
        self.assertIsInstance(paymentform, MakePaymentForm)
        self.assertIsInstance(orderform, OrderForm)
