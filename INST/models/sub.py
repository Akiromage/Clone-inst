from django.db import models
from .user import User


class Sub(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subscribe = models.ManyToManyField(User, related_name="subscribe")
    subscribers = models.ManyToManyField(User, related_name="subscribers")
    int_sub = models.IntegerField(default=0)