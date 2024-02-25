from django.db import models
from .abstr import Abstract
from .postt import Postt


class SavePosts(Abstract):
    saves_posts = models.ManyToManyField(Postt, related_name="save")
