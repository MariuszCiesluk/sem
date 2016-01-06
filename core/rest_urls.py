from django.conf.urls import *

from core.rest_views import TaskRestListView, TaskRestView


urlpatterns = (
    url(r'^list/$', TaskRestListView.as_view(), name='tasks-list'),
    url(r'^list/(?P<pk>[0-9]+)/$', TaskRestView.as_view(), name='edit-task'),
)
