from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class AuthenticationTests(TestCase):

    def test_registration(self):
        response = self.client.post(reverse('signup'), {'username': 'testuser', 'password1': 'testpassword', 'password2': 'testpassword'})
        self.assertEqual(response.status_code, 302) 

    def test_login(self):
        user = User.objects.create_user(username='testuser', password='testpassword')
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 302) 

    def test_logout(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 200) 