from django.test import TestCase
from cart.views import *
from cart.models import *
from issues.models import Bug
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.test.client import Client
from django.urls import resolve
from django.urls import reverse

# Create your tests here.


class TestViews(TestCase):
    def setUp(self):
        self.c = Client()
        self.user = User.objects.create_user(
            username="test", email="test@test.com", password="test")

    # VIEW CART
    def test_view_cart_page(self):
        response = self.c.get(reverse('view_cart'))
        # 302 error because @login_required
        self.assertEqual(response.status_code, 302)
        # mock login
        self.c.login(username='test', password='test')
        response = self.c.get(reverse('view_cart'))
        # 200 because we are logged in
        self.assertEqual(response.status_code, 200)


    # # ADD TO CART
    # def test_add_cart_page(self):
    #     bug = Bug.objects.create(bug=bug)
    #     # response = self.client.post('/AdminUnit/job/', {'event': event.id, ...})

    #     response = self.c.post('/cart/add_to_cart', {'id': bug.id})

    #     # 302 error because @login_required
    #     self.assertEqual(response.status_code, 302)
    #     # mock login
    #     self.c.login(username='test', password='test')
    #     response = self.c.get(reverse('add_to_cart'))
    #     # 200 because we are logged in
    #     self.assertEqual(response.status_code, 200)

    # # ADJUST CART
    # def test_adjust_cart_page(self):
    #     response = self.c.get(reverse('adjust_cart', id))
    #     # 302 error because @login_required
    #     self.assertEqual(response.status_code, 302)
    #     # mock login
    #     self.c.login(username='test', password='test')
    #     response = self.c.get(reverse('adjust_cart'))
    #     # 200 because we are logged in
    #     self.assertEqual(response.status_code, 200)
