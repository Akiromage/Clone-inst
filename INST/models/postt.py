from django.db import models
from .abstr import Abstract


class Postt(Abstract):
    text = models.TextField(max_length=1000)
    img = models.ImageField(upload_to="media/post_img")
