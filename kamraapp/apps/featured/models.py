# -*- coding: utf-8 -*-
from django.db import models

from jsonfield import JSONField


class BaseFeaturedContent(models.Model):
    title = models.CharField(max_length=128)
    excerpt = models.CharField(max_length=256)
    description = models.TextField()

    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    data = JSONField(default={})

    class Meta:
        abstract = True


class FeaturedBet(BaseFeaturedContent):
    bet = models.ManyToManyField('bet.Bet', blank=True, null=True)


class FeaturedDonationRecipient(BaseFeaturedContent):
    donation_recipient = models.ManyToManyField('bet.DonationRecipient', blank=True, null=True)
