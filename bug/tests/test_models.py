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





class BugTest(TestCase):

    def test_bug_default(self):
        time = timezone.now()
        bug_entry= Bug(pub_date=time)
        self.assertIs(bug_entry.was_published_recently(),True)

    def test_states_default(self):
        bug_entry = Bug(bug_title="Error404", bug_description="no image found", bug_status=STATES[1])
        self.assertIs(bug_entry.bug_status, STATES[1])

    def test_reported_by(self):
        self.credentials = {
        'username': 'test',
        'password': 'test123',
        'email':'test@gmail.com'
        }
        User = get_user_model()
        User.objects.create_user(**self.credentials)
        user = User.objects.get(username='test')
        bug_entry = Bug(
            bug_title="Some issue",
            bug_description="no image found",
            bug_status = STATES[1],
            reported_by=user)
        self.assertEqual(bug_entry.reported_by.username,"test")

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
        self.bug_entry = {
        'bug_title':'test title',
        'bug_description':'test description',
        'bug_status':STATES[1],
        'reported_by':self.user
        }

    def create_bug_no_image(self):
        return Bug.objects.create(**self.bug_entry)

    def create_bug_image(self):
        image_file = BytesIO()
        im_x = im.new('RGBA', size=(50,50), color=(256,0,0))
        im_x.save(image_file, 'png')
        image_file.seek(0)
        django_friendly_file = ContentFile(image_file.read(), 'test.png')
        return django_friendly_file

    def test_bug_create_no_image(self):
        bug =  self.create_bug_no_image()
        self.assertTrue(isinstance(bug, Bug))
        self.assertEqual(Bug.objects.filter(reported_by = self.user).exists(),True)

    def test_bug_create_one_image(self):
        bug = self.create_bug_no_image()
        bug.has_image.create(image= self.create_bug_image())
        self.assertEqual(Image.objects.filter(bug=bug.id).exists(),True)
        self.assertEqual(Image.objects.filter(bug=bug.id).count(),1)

    def test_bug_create_multiple_image(self):
        bug = self.create_bug_no_image()
        bug.has_image.create(image= self.create_bug_image())
        bug.has_image.create(image= self.create_bug_image())
        self.assertEqual(Image.objects.filter(bug=bug.id).exists(),True)
        self.assertEqual(Image.objects.filter(bug=bug.id).count(),2)
