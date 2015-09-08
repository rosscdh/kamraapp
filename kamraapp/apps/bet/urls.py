# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.views.generic import TemplateView, DetailView

from rest_framework import routers

from .views import BetListView, BetDetailView, BetCreateView, BetFormView, CloneBetFormView, CounterBetFormView
from .api.views import BetViewset, DonationRecipientViewset

from .models import DonationRecipient


router = routers.SimpleRouter(trailing_slash=False)

router.register(r'bets', BetViewset, base_name='bets')
router.register(r'donation-recipients', DonationRecipientViewset, base_name='donation-recipients')


urlpatterns = patterns('',
    url(r'^$', BetListView.as_view(), name='list'),

    url(r'^contact/$', TemplateView.as_view(template_name='public/contact.html'), name='contact'),

    url(r'^k/create/$', BetCreateView.as_view(), name='create'),
    url(r'^k/(?P<slug>[\w-]+)/$', BetDetailView.as_view(), name='detail'),
    url(r'^k/(?P<slug>[\w-]+)/edit/$', BetFormView.as_view(), name='edit'),
    url(r'^k/(?P<slug>[\w-]+)/clone/$', CloneBetFormView.as_view(), name='clone'),
    url(r'^k/(?P<slug>[\w-]+)/counter/$', CounterBetFormView.as_view(), name='edit'),

    url(r'^d/(?P<slug>[\w-]+)/$', DetailView.as_view(model=DonationRecipient, template_name='donationrecipient/donationrecipient_detail.html'), name='donationrecipient-detail'),
) + router.urls
