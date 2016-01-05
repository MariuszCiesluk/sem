from django.conf.urls import *

from core.views import MainView, LoginView, LogoutView, RegistrationView, TaskCreateView, TaskListView, TaskUpdateView, \
    TaskDeleteView

urlpatterns = patterns('',
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^registration/$', RegistrationView.as_view(), name='registration'),

    url(r'^task-update/(?P<pk>[0-9]+)/$', TaskUpdateView.as_view(), name='task_update'),
    url(r'^task-list/$', TaskListView.as_view(), name='task_list'),
    url(r'^task-create/$', TaskCreateView.as_view(), name='task_create'),
    url(r'^task-delete/(?P<pk>[0-9]+)/$', TaskDeleteView.as_view(), name='task_delete'),

    url(r'^$', MainView.as_view(), name='mainpage'),
)
