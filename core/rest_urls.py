from django.conf.urls import *

from core.rest_views import TaskRestListView, TaskRestView


urlpatterns = (
    url(r'^list/$', TaskRestListView.as_view(), name='tasks-list'),
    url(r'^create/(?P<pk>[0-9]+)/$', TaskRestView.as_view(), name='create-task'),
    url(r'^edit/(?P<pk>[0-9]+)/$', TaskRestView.as_view(), name='edit-task'),
    url(r'^delete/(?P<pk>[0-9]+)/$', TaskRestView.as_view(), name='delete-task'),
)
