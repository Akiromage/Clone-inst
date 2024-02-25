from django.db import models
from .abstr import Abstract
from .postt import Postt
from .comments import Commentary


class Like(Abstract):
    post = models.ForeignKey(Postt, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.ForeignKey(Commentary, on_delete=models.CASCADE, null=True, blank=True)