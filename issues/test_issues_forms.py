from django.test import TestCase
from .forms import BugForm, FeatureForm, BugCommentForm


# Create your tests here.


class Setup_Class(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            email="user@user.com", username="user", password1="password",
            password2="password")


class TestBugForm(TestCase):
    # Valid Form Data
    def test_BugForm_valid(self):
        form = BugForm(
            data={'title': 'test title', 'details': 'test details'})
        self.assertTrue(form.is_valid())

    def test_correct_message_for_missing_required_field(self):
        form = BugForm({'title': '', 'details': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['title'], [u'This field is required.'])


class TestFeatureForm(TestCase):
    # Valid Form Data
    def test_FeatureForm_valid(self):
        form = FeatureForm(
            data={'title': 'test title', 'details': 'test details', 'cost_per_hour': '50.00'})
        self.assertTrue(form.is_valid())

    def test_correct_message_for_missing_required_field(self):
        form = FeatureForm({'title': '', 'details': '', 'cost_per_hour': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['title'], [u'This field is required.'])


class TestBugCommentFormForm(TestCase):
    # Valid Form Data
    def test_BugCommentForm_valid(self):
        form = BugCommentForm(
            data={'comment': 'test comment'})
        self.assertTrue(form.is_valid())

    def test_correct_message_for_missing_required_field(self):
        form = BugCommentForm({'comment': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['comment'], [u'This field is required.'])
