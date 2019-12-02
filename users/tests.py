# Create your tests here.
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.core import mail
from django.urls import reverse
from django.test import override_settings
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

class PasswordReset_ViewTest(TestCase):

    # def setUp(self):
    #     self.credentials = {
    #     'username': 'test',
    #     'password': 'test123',
    #     'email':'test@gmail.com'
    #     }
    #     User = get_user_model()
    #     User.objects.create_user(**self.credentials)
    # @override_settings(EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend')
    def test_password_reset(self):

        response = self.client.get(reverse('password_reset'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name, ['registration/password_reset_form.html'])

        # Then we post the response with our "email address"
        response = self.client.post(reverse('password_reset'),{'email':'mu-za-mir@hotmail.com'})
        self.assertEqual(response.status_code, 302)

        
        # # At this point the system will "send" us an email. We can "check" it thusly:
        # print(mail.outbox)
        # self.assertEqual(len(mail.outbox), 1)
        # self.assertEqual(mail.outbox[0].subject, 'Password reset on 127.0.0.1:8000')
        #
        # # Now, here's the kicker: we get the token and userid from the response
        # token = response.context[0]['tokenS']
        # uid = response.context[0]['uid']
        # # Now we can use the token to get the password change form
        # response = self.c.get(reverse('password_reset_confirm', kwargs={'token':token,'uidb64':uid}))
        # self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.template_name, ['registration/password_reset_confirm.html'])
        #
        # # Now we post to the same url with our new password:
        # response = self.client.post(reverse('password_reset_confirm',
        #     kwargs={'token':token,'uidb36':uid}), {'new_password1':'pass','new_password2':'pass'})
        # self.assertEqual(response.status_code, 302)
