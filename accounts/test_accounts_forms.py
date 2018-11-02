from django.test import TestCase
from .forms import UserLoginForm, UserRegistrationForm

# Create your tests here.


class Setup_Class(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            email="user@user.com", username="user", password1="password",
            password2="password")


class TestUserLoginForm(TestCase):
    # Valid Form Data
    def test_UserLoginForm_valid(self):
        form = UserLoginForm(data={'username': 'user', 'password': 'password'})
        self.assertTrue(form.is_valid())

    def test_correct_message_for_missing_required_field(self):
        form = UserLoginForm({'username': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'], [u'This field is required.'])


class TestUserRegistrationForm(TestCase):
    # Valid Form Data
    def test_UserRegistrationForm_valid(self):
        form = UserRegistrationForm(
            data={'email': "user@user.com", 'username': "user",
                  'password1': "password", 'password2': "password"})
        self.assertTrue(form.is_valid())

    # Invalid Form Data
    def test_UserRegistrationForm_invalid(self):
        form = UserRegistrationForm(
            data={'email': "", 'username': "u",
                  'password1': "p", 'password2': "pa"})
        self.assertFalse(form.is_valid())
