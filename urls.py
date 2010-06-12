from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic.simple import direct_to_template
from django.http import HttpResponseRedirect

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^groupbuy1/', include('groupbuy1.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^$', lambda r: HttpResponseRedirect(r.path+'index.html')),
    (r'^(.*)/$', lambda r, x: HttpResponseRedirect(r.path+'index.html')),
    (r'^(?P<template_name>.+\.html)$', lambda r,template_name: direct_to_template(r, template_name)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'', include('staticfiles.urls')),
    )
