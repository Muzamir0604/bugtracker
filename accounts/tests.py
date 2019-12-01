from django.test import TestCase, Client
from django.contrib.auth import get_user_model

# Create your tests here.
class LogInTest(TestCase):

    def setUp(self):
        self.credentials = {
        'username': 'test',
        'password': 'test123',
        'email':'test@gmail.com'
        }
        User = get_user_model()
        User.objects.create_user(**self.credentials)

    def test_login(self):
        # get login page
        User = get_user_model()
        self.client.login(username='test',password='temporary')
        response =  self.client.get('/admin/', follow=True)
        user = User.objects.get(username='test')
        self.assertEqual(user.email,'test@gmail.com')
