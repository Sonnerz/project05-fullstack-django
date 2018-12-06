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

    # GET ORDERS
    def test_get_order_details_page(self):
        page = self.client.get('/accounts/29/orders/')
        self.assertEqual(page.status_code, 302)
        self.client.login(username='test', password='test')
        page = self.client.get('/accounts/29/orders/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "orders.html")

    # HOME
    def test_get_home_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")

    # LOGIN
    def test_get_login_page(self):
        page = self.client.get(reverse("login"))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")

        # test for CSRF
        response = self.client.get(reverse('login'))
        self.assertContains(response, 'csrfmiddlewaretoken')

        self.client.login(username='test', password='test')
        # response = self.client.get(reverse('acc_index'))
        self.assertEqual(response.status_code, 200)

        self.assertTrue(self.client.login(username='test', password='test'))
        response = self.client.get(reverse('login'))

    # LOGOUT
    def test_logout(self):
        page = self.client.get(reverse('logout'), follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")

        response = self.client.get(reverse('logout'))
        # 302 error because @login_required
        self.assertEqual(response.status_code, 302)
        self.client.login(username='test', password='test')
        response = self.client.get(reverse('index'))
        # user redirected to index after logout
        self.assertEqual(response.status_code, 200)

    # USER PROFILE
    def test_Userprofile_page(self):
        response = self.client.get(reverse('user_profile'))
        # 302 error because @login_required
        self.assertEqual(response.status_code, 302)
        self.client.login(username='test', password='test')
        response = self.client.get(reverse('user_profile'))
        self.assertEqual(response.status_code, 200)

    def test_register_template_context(self):
        # create few blog entries
        User.objects.create(
            username='Test', email='Test@test.com', password='test')
        User.objects.create(
            username='Test1', email='Test@test.com', password='test')
        # test for form existance
        response = self.client.get(reverse('registration'))
        form = response.context['form']
        self.assertIsInstance(form, UserRegistrationForm)

        # test for CSRF
        response = self.client.get(reverse('registration'))
        self.assertContains(response, 'csrfmiddlewaretoken')

        self.assertTrue(self.client.login(username='test', password='test'))
        response = self.client.get(reverse('login'))


# https://simpleisbetterthancomplex.com/series/2017/09/25/a-complete-beginners-guide-to-django-part-4.html#testing-the-sign-up-view
class RegisterTests(TestCase):
    def setUp(self):
        url = reverse('registration')
        self.response = self.client.get(url)

    def test_signup_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_signup_url_resolves_signup_view(self):
        view = resolve('/accounts/register/')
        self.assertEquals(view.func, registration)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_contains_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, UserRegistrationForm)


class SuccessfulRegisterTests(TestCase):
    def setUp(self):
        url = reverse('registration')
        data = {
            'username': 'john',
            'password1': 'abcdef123456',
            'password2': 'abcdef123456'
        }
        self.response = self.client.post(url, data)
        self.home_url = reverse('index')
        self.profile_url = reverse('user_profile')

    def test_redirection(self):
        '''
        A valid form submission should redirect the user to the profile page
        '''
        self.assertRedirects(self.response, self.profile_url)

    def test_user_creation(self):
        self.assertTrue(User.objects.exists())

    def test_user_authentication(self):
        '''
        Create a new request to an arbitrary page.
        The resulting response should now have a `user` to its context,
        after a successful sign up.
        '''
        response = self.client.get(self.home_url)
        user = response.context.get('user')
        self.assertTrue(user.is_authenticated)


class InvalidRegisterTests(TestCase):
    def setUp(self):
        url = reverse('registration')
        self.response = self.client.post(url, {})  # submit an empty dictionary

    def test_signup_status_code(self):
        '''
        An invalid form submission should return to the same page
        '''
        self.assertEquals(self.response.status_code, 200)

    def test_form_errors(self):
        form = self.response.context.get('form')
        self.assertTrue(form.errors)

    def test_dont_create_user(self):
        self.assertFalse(User.objects.exists())
