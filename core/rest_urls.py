from django.conf.urls import *

from core.rest_views import TaskRestListView, TaskRestView, TaskListElementRestListView, TaskListElementRestView

urlpatterns = (
    url(r'^v1/list/$', TaskRestListView.as_view(), name='tasks-list'),
    url(r'^v1/list/(?P<pk>[0-9]+)/$', TaskRestView.as_view(), name='edit-task'),

    url(r'^v1/list-elements/(?P<task_pk>[0-9]+)/$', TaskListElementRestListView.as_view(), name='task-element-list'),
    url(r'^v1/list-elements/(?P<task_pk>[0-9]+)/(?P<pk>[0-9]+)/$', TaskListElementRestView.as_view(), name='edit-element-task'),
)

# from rest_framework.authtoken import views
# urlpatterns += [
#     url(r'^api-token-auth/', views.obtain_auth_token)
# ]
