from django.contrib.auth.models import User

from django import template

register = template.Library()


@register.simple_tag
def get_username(user_pk):
    try:
        user = User.objects.get(pk=user_pk)
    except User.DoesNotExist:
        return ''
    return user.get_username()
