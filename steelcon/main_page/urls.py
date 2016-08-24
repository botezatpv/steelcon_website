#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

app_name = 'main_page'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(ur'^(?P<service_name>[^admin][\w\s]+)/$', views.service,
         name='service'),
    url(ur'^(?P<service_name>[\w\s]+)/(?P<item_name>[\w\s]+)$',
         views.items, name='items'),
]