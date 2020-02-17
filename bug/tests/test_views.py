from django.test import TestCase, Client, RequestFactory
from django.utils import timezone
from django.urls import reverse, reverse_lazy
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.models import AnonymousUser, Group
from django.shortcuts import get_object_or_404

from ..views import IndexView, BugCreate, DetailBug
from ..forms import BugForm, ImageFormSet
from ..models import Bug, Image
# Create your tests here.

from PIL import Image as im
from io import StringIO, BytesIO


from django.core.files.base import ContentFile


class BugIndexTest(TestCase):

    def test_index_loggedin(self):
        self.credentials = {
        'username': 'test',
        'password': 'test123',
        'email':'test@gmail.com'
        }
        User = get_user_model()
        self.user = User.objects.create_user(**self.credentials)
        # create group because could not be accessed from db
        Group.objects.create(name='Analysts')
        self.group = Group.objects.get(name="Analysts")
        # print(self.group
        self.user.groups.add(self.group)


        self.client.login(username=self.credentials['username'], password=self.credentials['password'])
        response = self.client.get(reverse('bug:index'))
        self.assertEqual(response.status_code,200)

    def test_index(self):
        response = self.client.get(reverse('bug:index'))
        self.assertRedirects(response,reverse('login')+'?next='+reverse('bug:index'), status_code=302, target_status_code=200,
        fetch_redirect_response=True)

class BugCreateTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.credentials = {
        'username': 'test',
        'password': 'test123',
        'email':'test@gmail.com'
        }
        User = get_user_model()
        self.user = User.objects.create_user(**self.credentials)

    def test_render(self):
        request = self.factory.get(reverse('bug:bug-form'))
        request.user = self.user

        response = BugCreate.as_view()(request)
        self.assertEqual(response.status_code,200)

    def test_render_anonymous(self):
        response = self.client.get(reverse('bug:bug-form'))
        self.assertRedirects(response, reverse('login')+'?next='+reverse('bug:bug-form'), status_code=302,target_status_code=200, fetch_redirect_response=True)

class BugDetailTest(TestCase):

    def create_bug_image(self):
        image_file = BytesIO()
        image = im.new('RGBA', size=(50,50), color=(256,0,0))
        image.save(image_file, 'png')
        image_file.seek(0)
        django_friendly_file = ContentFile(image_file.read(), 'test.png')
        return django_friendly_file

    def create_bug_no_image(self):
        return Bug.objects.create(**self.bug_entry)

    def setUp(self):
        self.factory = RequestFactory()
        self.credentials = {
        'username': 'test',
        'password': 'test123',
        'email':'test@gmail.com'
        }
        User = get_user_model()
        self.user = User.objects.create_user(**self.credentials)
        self.bug_entry = {
        'bug_title':'test title',
        'bug_description':'test description'
        }

        self.bug = self.create_bug_no_image()
        # print(dir(self.bug))
        self.bug.has_image.create(image= self.create_bug_image())


    def test_render(self):
        request = self.factory.get(reverse('bug:bug-detail',kwargs={'pk': self.bug.id}))
        request.user = self.user
        response = DetailBug.as_view()(request,pk=self.bug.id)
        self.assertEqual(response.status_code,200)
    #
    def test_render_anonymous(self):
        response = self.client.get(reverse('bug:bug-detail',kwargs={'pk': self.bug.id}))
        self.assertRedirects(response, reverse('login')+'?next='+reverse('bug:bug-detail',kwargs={'pk': self.bug.id}), status_code=302,target_status_code=200, fetch_redirect_response=True)
