from django.test import TestCase, Client
from django.utils import timezone
from .models import Bug, Images
from django.urls import reverse
from django.contrib.auth import get_user_model
# Create your tests here.


class BugModelTest(TestCase):
    def test_model_ok(self):
        time = timezone.now()
        bug_entry= Bug(pub_date=time)
        self.assertIs(bug_entry.was_published_recently(),True)

    def test_states_default(self):
        bug_entry = Bug(bug_title="Error404", bug_description="no image found")
        self.assertIs(bug_entry.bug_states, "new")

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
            reported_by=user)
        # print(dir(bug_entry.reported_by))
        self.assertEqual(bug_entry.reported_by.username,"test")

@staticmethod
def get_image_file(name, ext='png', size=(50, 50), color=(256, 0, 0)):
    file_obj = BytesIO()
    image = Image.new("RGBA", size=size, color=color)
    image.save(file_obj, ext)
    file_obj.seek(0)
    return File(file_obj, name=name)

    def test_image_upload(self):
        image1 = self.get_image('image.png')
        image2 = self.get_image('image2.png')
        bug_entry = Bug(bug_title="random errors", bug_description="image found")
        bug_entry.images_set.create(image= image1)
        bug_entry.images_set.create(image= image2)
        self.assertEqual(images.objects.filter(bug=bug_entry.id).exists(),True)


class BugViewTest(TestCase):
    def test_no_bugs(self):
        response = self.client.get(reverse('bug:index'))

        self.assertEqual(response.status_code,200)
        self.assertContains(response, "No bugs")
