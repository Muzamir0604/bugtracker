# Create your tests here.
from django.test import TestCase, Client, RequestFactory
from django.contrib.auth import get_user_model
from django.core import mail
from django.urls import reverse
from django.test import override_settings
from .forms import CustomUserCreationForm
from django.utils.html import escape
# Create your tests here.

# https://django-inspectional-registration.readthedocs.io/en/latest/_modules/registration/tests/test_views.html

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

class ViewSignUpTest(TestCase):

    def test_render(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code,200)
        self.failUnless(isinstance(response.context['form'],CustomUserCreationForm))

    def test_view_post_success(self):
        response = self.client.post(reverse('signup'), data={'username':'test','email':'test@gmail.com','password1':'terribleidea','password2':'terribleidea'})
        self.assertRedirects(response,reverse('home'), status_code=302, target_status_code=200, fetch_redirect_response=True)
        user = get_user_model()
        self.assertEqual(user.objects.count(),1)

    def test_view_post_failure(self):

        response = self.client.post(reverse('signup'),
                                    data={'username': 'bob','email':'bob@gmail.com',
                                    'password1':'password1',
                                    'password2':'password2'})
        self.assertEqual(response.status_code, 200)
        self.failIf(response.context['form'].is_valid())
        expected_error = escape("The two password fields didn't match.")
        ## TODO: create a detection for expectod error
        print(response.context['form'].non_field_errors())
        # self.assertContains(response.context['form'].error_messages, expected_error)
        # self.assertContains(response.context['form'].non_field_errors(),expected_error)
        # self.assertFormError(response, 'form', field=response.context['form'].non_field_errors,errors=expected_error)

class ViewPasswordResetTest(TestCase):

    def setUp(self):
        self.credentials = {
        'username': 'test',
        'password': 'test123',
        'email':'test@gmail.com'
        }
        User = get_user_model()
        User.objects.create_user(**self.credentials)


    def test_password_reset(self):
        response = self.client.get(reverse('password_reset'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name, ['registration/password_reset_form.html'])

    @override_settings(EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend')
    def test_post_password_reset(self):
        # Then we post the response with our "email address"
        response = self.client.post(reverse('password_reset'),{'email':'test@gmail.com'})
        self.assertRedirects(response, reverse('password_reset_done'), status_code=302,target_status_code=200, fetch_redirect_response=True)

        # # At this point the system will "send" us an email. We can "check" it thusly:
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Password reset on testserver')
        #
        # # Now, here's the kicker: we get the token and userid from the response
        token = response.context[0]['token']
        uid = response.context[0]['uid']
        # # Now we can use the token to get the password change form
        response = self.client.get(reverse('password_reset_confirm', kwargs={'token':token,'uidb64':uid}))
        self.assertEqual(response.status_code, 302)

        # # Now we post to the same url with our new password:
        response = self.client.post(reverse('password_reset_confirm',
            kwargs={'token':token,'uidb64':uid}),{'new_password1':'pass','new_password2':'pass'})

        self.assertRedirects(response, '/users/reset/MQ/set-password/', status_code=302,target_status_code=200, fetch_redirect_response=True)

class ViewProfileTest(TestCase):
    def setUp(self):
        self.credentials = {
        'username': 'test',
        'password': 'test123',
        'email':'test@gmail.com'
        }
        User = get_user_model()
        self.user = User.objects.create_user(**self.credentials)

    def test_render(self):
        self.client.login(username=self.credentials['username'], password=self.credentials['password'])
        response = self.client.get(reverse('profile',kwargs={'pk':self.user.id}))
        self.assertEqual(response.status_code, 200)

class ViewEditProfileTest(TestCase):
    def setUp(self):
        self.credentials = {
        'username': 'test',
        'password': 'test123',
        'email':'test@gmail.com'
        }
        User = get_user_model()
        self.user = User.objects.create_user(**self.credentials)

    def test_render(self):
        self.client.login(username=self.credentials['username'], password=self.credentials['password'])
        response = self.client.get(reverse('profile',kwargs={'pk':self.user.id}))
