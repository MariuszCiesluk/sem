from django.contrib.auth.models import User
from django.db import models
from reversion import revisions as reversion

from core.constants import PRIORITIES

# from django.conf import settings
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from rest_framework.authtoken.models import Token


@reversion.register()
class Task(models.Model):
    """
    basic model for Task, priorities are django choices. Defined in constants file
    """
    user = models.ForeignKey(User)
    name = models.CharField(max_length=255)
    is_realized = models.NullBooleanField()
    priority = models.CharField(max_length=255, choices=PRIORITIES)

    def __str__(self):
        return 'task: {}'.format(self.name)


class TaskListElement(models.Model):
    """
    Nested item of bigger Task
    """
    task = models.ForeignKey(Task, related_name='items')
    checked = models.NullBooleanField()
    description = models.CharField(max_length=255)

    def __str__(self):
        return '{}, item: {}'.format(self.task, self.description)


# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)
