from django.db import models
from .user import User


class Abstract(models.Model):
    day = models.DateTimeField(auto_now_add=True)
    day_mod = models.DateTimeField(auto_now=True)
    user_s = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True