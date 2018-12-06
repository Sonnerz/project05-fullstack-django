from django.test import TestCase
from .views import *
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.test.client import Client
from django.urls import resolve
import datetime


# Create your tests here.


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="test", email="test@test.com", password="test")

    # SUPER ADMIN PAGE
    def test_super_admin_blog_page(self):
        page = self.client.get('/blog/superadminblog/')
        self.assertEqual(page.status_code, 302)
        self.client.login(username='test', password='test')
        page = self.client.get('/blog/superadminblog/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "superadminblog.html")
