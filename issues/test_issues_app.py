from django.apps import apps
from django.test import TestCase
from .apps import IssuesConfig


class TestIssuesConfig(TestCase):
    def test_app(self):
        self.assertEqual("issues", IssuesConfig.name)
        self.assertEqual("issues", apps.get_app_config("issues").name)
