from django.test import TestCase, Client, RequestFactory
from django.utils import timezone
from django.urls import reverse, reverse_lazy
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.models import AnonymousUser

from ..views import IndexView, BugCreate
from ..forms import BugForm, ImageFormSet
from ..models import Bug, Image
from ..constants import STATES
# Create your tests here.

from PIL import Image as im
from io import StringIO, BytesIO

from django.core.files.base import ContentFile

# https://realpython.com/testing-in-django-part-1-best-practices-and-examples/

class BugCreateTest(TestCase):

    def create_bug_image(self):
        image_file = BytesIO()
        im_x = im.new('RGBA', size=(50,50), color=(256,0,0))
        im_x.save(image_file, 'png')
        image_file.seek(0)
        django_friendly_file = ContentFile(image_file.read(), 'test.png')
        return django_friendly_file


    def setUp(self):
        self.factory = RequestFactory()
        self.credentials = {
        'username': 'test',
        'password': 'test123',
        'email':'test@gmail.com'
        }
        User = get_user_model()
        self.user = User.objects.create_user(**self.credentials)

    def test_valid_data_no_image(self):
        # print(STATES[1].get('Pending'))
        form = BugForm({
            'bug_title': "title of bug",
            'bug_description': "description of bug",
            'bug_status': 'Pending',
            'reported_by':self.user
        })
        # print(form.errors)
        self.assertTrue(form.is_valid())
        #
        bug = form.save()
        self.assertEqual(bug.bug_title, "title of bug")
        self.assertEqual(bug.bug_description, "description of bug")

    def test_blank_data(self):
        form = BugForm({})
        self.assertFalse(form.is_valid())
        self.assertTrue('bug_title' in form.errors)
        self.assertTrue('bug_description' in form.errors)
        self.assertTrue('bug_status' in form.errors)
