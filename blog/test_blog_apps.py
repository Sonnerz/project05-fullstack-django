from django.apps import apps
from django.test import TestCase
from .apps import PostsConfig


class TestPostsConfig(TestCase):
    def test_app(self):
        self.assertEqual("posts", PostsConfig.name)
        self.assertEqual("accounts", apps.get_app_config("accounts").name)
