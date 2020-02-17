from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
from django.forms.models import inlineformset_factory
from django.db.models.signals import post_delete



class Bug(models.Model):
    bug_title = models.CharField(max_length=200)
    bug_description = models.TextField(max_length=1000)
    bug_status = models.CharField(max_length=50, default="Pending")
    pub_date = models.DateTimeField('date published', editable=False)
    update_date = models.DateTimeField('date updated')
    reported_by = models.ForeignKey(get_user_model(),related_name="bugs", on_delete=models.CASCADE,null=True)
    severity = models.CharField(max_length=50, default="Low")
    supervisor = models.ForeignKey(get_user_model(),related_name="has_supervisor", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.bug_title

    def save(self,*args,**kwargs):
        if not self.id:
            self.pub_date = timezone.now()
        self.update_date = timezone.now()
        return super(Bug, self).save(*args, **kwargs)

    def was_published_recently(self):
        now = timezone.now()
        return now-datetime.timedelta(days=1) <= self.pub_date <= now
    def get_pub_date(self):
        return self.pub_date.date()
    def get_update_date(self):
        return self.update_date.date()

    def get_pub_date(self):
        return self.pub_date.date()

    def get_update_date(self):
        return self.update_date.date()

def get_image_filename(instance, filename):
    title = instance.bug.bug_title
    slug = slugify(title)
    return "post_images/%s-%s" % (slug, filename)


class Image(models.Model):
        bug= models.ForeignKey(Bug, default=None, related_name="has_image", on_delete = models.CASCADE)
        image = models.ImageField(upload_to=get_image_filename,
                              verbose_name='Image')

class Team(models.Model):
    bug = models.ForeignKey(Bug, related_name="has_team", on_delete = models.CASCADE)
    members = models.ForeignKey(get_user_model(),related_name ="member",on_delete = models.CASCADE, blank=True)
    assigned_by = models.ForeignKey(get_user_model(),related_name="assigner",on_delete = models.CASCADE, blank=True)

class Request(models.Model):
    owner = models.ForeignKey(get_user_model(),related_name ="owner", on_delete = models.CASCADE)
    bug = models.ForeignKey(Bug, on_delete= models.CASCADE)
    type = models.CharField(max_length=50, default=None) # can be pendingReview, Assignment,Request for more data
    receiver = models.ForeignKey(get_user_model(),related_name="receiver", on_delete=models.CASCADE)
