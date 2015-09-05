# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import FeaturedBet, FeaturedDonationRecipient


admin.site.register([FeaturedBet, FeaturedDonationRecipient])
