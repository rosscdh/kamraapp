# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from django.views.generic import DetailView
from .models import FeaturedBet, FeaturedDonationRecipient


urlpatterns = patterns('',
    url(r'^(?P<slug>[\w-]+)/$', DetailView.as_view(model=FeaturedDonationRecipient), name='donation_recipient-detail'),
    url(r'^(?P<slug>[\w-]+)/$', DetailView.as_view(model=FeaturedBet), name='bet-detail'),
)
