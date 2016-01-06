from django.conf.urls import *

from core.rest_views import TaskRestListView, TaskRestView, TaskListElementRestListView, TaskListElementRestView

urlpatterns = (
    url(r'^list/$', TaskRestListView.as_view(), name='tasks-list'),
    url(r'^list/(?P<pk>[0-9]+)/$', TaskRestView.as_view(), name='edit-task'),

    url(r'^list-elements/(?P<task_pk>[0-9]+)/$', TaskListElementRestListView.as_view(), name='task-element-list'),
    url(r'^list-elements/(?P<task_pk>[0-9]+)/(?P<pk>[0-9]+)/$', TaskListElementRestView.as_view(), name='edit-element-task'),
)

# from rest_framework.authtoken import views
# urlpatterns += [
#     url(r'^api-token-auth/', views.obtain_auth_token)
# ]
