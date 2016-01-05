from django.contrib.auth.models import User
from django.db import models
from reversion import revisions as reversion

from core.constants import PRIORITIES


@reversion.register()
class Task(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=255)
    is_realized = models.NullBooleanField()
    priority = models.CharField(max_length=255, choices=PRIORITIES)
