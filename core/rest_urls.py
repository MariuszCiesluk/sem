from django.conf.urls import *

from core.rest_views import TaskRestListView
from core.views import MainView, LoginView, LogoutView, RegistrationView

urlpatterns = patterns('',
    url(r'^list/$', TaskRestListView.as_view(), name='tasks-list'),
    # url(r'^create/$', LogoutView.as_view(), name='logout'),
    # url(r'^edit/$', RegistrationView.as_view(), name='registration'),
    # url(r'^$', MainView.as_view(), name='mainpage'),
)
