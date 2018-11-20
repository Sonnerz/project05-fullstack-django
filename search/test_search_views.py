from django.test import TestCase
from search.views import *
from django.contrib.auth.models import User
from django.test.client import Client
from django.urls import resolve


# Create your tests here.


class TestViews(TestCase):
    def setUp(self):
        self.c = Client()
        self.user = User.objects.create_user(
            username="test", email="test@test.com", password="test")

    # HOME
    def test_get_search_page(self):
        self.c.login(username='test', password='test')
        response = self.c.get("/search/?q=lorem")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "results.html")

    # def test_pagination_is_six(self):
    #     self.c.login(username='test', password='test')
    #     response = self.c.get("/search/?q=lorem")
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTrue('is_paginated' in response.context)
    #     self.assertTrue(response.context['is_paginated'] == True)
    #     self.assertTrue(len(response.context['bugs']) == 6)
