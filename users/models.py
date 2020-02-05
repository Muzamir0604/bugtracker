from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.

class CustomUser(AbstractUser):
    # pass
    # add additional fields here
    address = models.CharField(max_length=500, blank=True)
    

    def __str__(self):
        return self.username
