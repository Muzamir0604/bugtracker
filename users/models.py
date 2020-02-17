from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import Group

# Create your models here.
# https://thecodinginterface.com/blog/django-auth-part1/    -- useful tips here

class CustomUser(AbstractUser):
    # pass
    # add additional fields here
    # group =  models.CharField(max_length=50, default="Developer")
    address = models.CharField(max_length=500, blank=True)
    postal = models.PositiveIntegerField(default=0,blank=True,validators=[MaxValueValidator(1000)])
    contact = PhoneNumberField(blank=True)

    def __str__(self):
        return self.username
