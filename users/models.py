from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    pass
    # add additional fields here

    def __str__(self):
        return self.username
