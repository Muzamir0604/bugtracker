from django.db import models
from django.utils import timezone
import datetime
# Create your models here.


class Bug(models.Model):
    bug_title = models.CharField(max_length=200)
    bug_description = models.CharField(max_length=500)
    bug_states = models.CharField(max_length=50, default="new")
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.bug_description

    def was_published_recently(self):
        now = timezone.now()
        return now-datetime.timedelta(days=1) <= self.pub_date <= now
