from django.db import models
from django.urls import reverse
# Create your models here.

class Product(models.Model):
    title =  models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price =  models.DecimalField(decimal_places=2, max_digits=10000)
    summary =  models.TextField(blank=False,null=False)
    featured = models.BooleanField(default=False)
    email = models.EmailField(null=True)

class Article(models.Model):
    title =  models.CharField(max_length=120)
    content = models.TextField()
    active = models.BooleanField(default=True)

    # def get_absolute_url(self):
    #     return reverse("product:product-list", kwargs={"id":self.id})
