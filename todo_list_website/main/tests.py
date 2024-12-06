
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Task

class TestTasks(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')

    def test_index_authenticated(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

class TestTasksBD(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='user1', password='password123')
        Task.objects.create(user=user, title="qwe", description="aszx", complete=False)

    def test_Task(self):
        task = Task.objects.get(title="qwe")
        self.assertEqual(str(task), "qwe")

