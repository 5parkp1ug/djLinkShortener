from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    # Fields
    profile_pic = models.ImageField(upload_to="upload/images/")

    class Meta:
        pass

    def __str__(self):
        return self.get_full_name()
