from django.test import TestCase, Client

# Create your tests here.
from django.urls import reverse
from .models import User
from .forms import RegisterForm


class RegisterViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('user:register')
        self.user_data = {
            'username': 'testuser',
            'first_name': 'test',
            'last_name': 'test',
            'email': 'testuser@example.com',
            'password1': 'testpass123',
            'password2': 'testpass123',
        }

    def test_register_view_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')
        self.assertIsInstance(response.context['form'], RegisterForm)

    def test_register_view_post_valid(self):
        response = self.client.post(self.url, data=self.user_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))
        self.assertEqual(User.objects.count(), 1)
        user = User.objects.first()
        self.assertEqual(user.username, self.user_data['username'])
        self.assertEqual(user.first_name, self.user_data['first_name'])
        self.assertEqual(user.last_name, self.user_data['last_name'])
        self.assertEqual(user.email, self.user_data['email'])

    def test_register_view_post_invalid(self):
        # Test case for submitting invalid data to the form
        invalid_data = self.user_data.copy()
        invalid_data['username'] = ''  # Make username field empty
        response = self.client.post(self.url, data=invalid_data)
        self.assertEqual(response.status_code, 200)
        user = User.objects.first()
        self.assertIsNone(user)
