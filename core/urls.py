from django.conf.urls import *

from core.views import TestView


urlpatterns = patterns('',
    url(r'test-view$', TestView, name='test-view'),
    )