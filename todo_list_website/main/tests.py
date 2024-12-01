
from django.test import TestCase
from django.contrib.auth.models import User

class TestTasks(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')

    def test_index_authenticated(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
