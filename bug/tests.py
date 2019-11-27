from django.test import TestCase
from django.utils import timezone
from .models import Bug
from django.urls import reverse
# Create your tests here.


class BugModelTest(TestCase):
    def test_model_ok(self):
        time = timezone.now()
        bug_entry= Bug(pub_date=time)
        self.assertIs(bug_entry.was_published_recently(),True)

    def test_states_default(self):
        bug_entry = Bug(bug_title="Error404", bug_description="no image found")
        self.assertIs(bug_entry.bug_states, "new")

class BugViewTest(TestCase):
    def test_no_bugs(self):
        response = self.client.get(reverse('bug:index'))

        self.assertEqual(response.status_code,200)
        self.assertContains(response, "No bugs")
