# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from rest_framework import routers

from .views import BetListView, BetDetailView, BetCreateView, BetFormView, CounterBetFormView
from .api.views import DonationRecipientViewset


router = routers.SimpleRouter(trailing_slash=False)

router.register(r'donation-recipients', DonationRecipientViewset, base_name='donation-recipients')


urlpatterns = patterns('',
    url(r'^$', BetListView.as_view(), name='list'),
    url(r'^create/$', BetCreateView.as_view(), name='create'),
    url(r'^(?P<slug>[\w-]+)/$', BetDetailView.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', BetFormView.as_view(), name='edit'),
    url(r'^(?P<slug>[\w-]+)/counter/$', CounterBetFormView.as_view(), name='edit'),
) + router.urls
