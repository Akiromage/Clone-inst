from django.db import models
from .abstr import Abstract
from .user import User
from .postt import Postt


class Commentary(Abstract):
    post = models.ForeignKey(Postt, on_delete=models.CASCADE)
    text = models.TextField(max_length=400)
