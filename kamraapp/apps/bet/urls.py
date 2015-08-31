# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from .views import BetListView, BetDetailView, BetCreateView, BetFormView


urlpatterns = patterns('',
    url(r'^$', BetListView.as_view(), name='list'),
    url(r'^create/$', BetCreateView.as_view(), name='create'),
    url(r'^(?P<slug>[\w-]+)/$', BetDetailView.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', BetFormView.as_view(), name='edit'),
)
