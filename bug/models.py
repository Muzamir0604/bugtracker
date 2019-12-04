from django.db import models
from django.utils import timezone
import datetime
# from django.conf import settings
from django.contrib.auth import get_user_model
# Create your models here.


class Bug(models.Model):
    bug_title = models.CharField(max_length=200)
    bug_description = models.CharField(max_length=500)
    bug_states = models.CharField(max_length=50, default="new")
    pub_date = models.DateTimeField('date published')
    reported_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.bug_description

    def was_published_recently(self):
        now = timezone.now()
        return now-datetime.timedelta(days=1) <= self.pub_date <= now

def get_image_filename(instance, filename):
    title = instance.post.title
    slug = slugify(title)
    return "post_images/%s-%s" % (slug, filename)


class Images(models.Model):
        bug= models.ForeignKey(Bug, default=None, on_delete = models.CASCADE)
        image = models.ImageField(upload_to=get_image_filename,
                              verbose_name='Image')

# class Snippet(models.Model):
#     name =  models.CharField(max_length=100)
#     body =  models.TextField()
#
#     def __str__(self):
#         return self.name
