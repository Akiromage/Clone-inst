from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(upload_to="media/img", default="media/img/def.png")
    status = models.TextField(null=True, blank=True)
    my_web = models.TextField(null=True, blank=True)