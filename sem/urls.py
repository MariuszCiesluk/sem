from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = (
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tasks/', include('core.rest_urls')),
    url(r'^', include('core.urls')),
)
