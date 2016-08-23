#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(ur'^(?P<service_name>[\w\s]+)/$', views.Service, name='Service'),
    url(ur'^(?P<service_name>[\w\s]+)/(?P<item_name>[\w\s]+)$', views.Items, name='Items'),
]