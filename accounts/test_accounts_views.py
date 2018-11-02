from django.test import TestCase
from .views import *
from django.contrib.auth.models import User

# Create your tests here.


class TestViews(TestCase):
    def test_get_home_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")

    def test_get_login_page(self):
        page = self.client.get("/accounts/login/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")

    def test_new_registration_page(self):
        user = User.objects.create_user(
            email="user@user.com",
            username="user",
            password="password")

        page = self.client.get("/accounts/register/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "registration.html")
