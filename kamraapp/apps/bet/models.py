# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify

from . import SUB_BET_TYPE

import os
import uuid
import datetime


def temp_uuid_gen(*args, **kwargs):
    return str(uuid.uuid4())


def _default_expiry():
    return datetime.datetime.utcnow() + datetime.timedelta(weeks=2)


class Bet(models.Model):
    """
    Primary bet object, can ahve sub and counter bets
    """
    SUB_BET_TYPE = SUB_BET_TYPE

    slug = models.SlugField()
    user = models.ForeignKey('auth.User', null=True, blank=True)

    # oath2 style token and secret to encode keys used in the urls that are pasted
    access_token = models.CharField(default=temp_uuid_gen(), max_length=255)
    access_secret = models.CharField(default=temp_uuid_gen(), max_length=255)

    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    recipients = models.ManyToManyField('bet.DonationRecipient')
    proofs = models.ManyToManyField('bet.Proof')

    parent_bet = models.ForeignKey('bet.Bet', null=True, blank=True)
    sub_bet_type = models.CharField(max_length=24,
                                    choices=SUB_BET_TYPE.get_choices(),
                                    null=True,
                                    blank=True)

    expires_at = models.DateTimeField(default=_default_expiry)

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def is_sub_bet(self):
        return self.parent_bet is not None

    @property
    def status(self):
        if self.proofs.count() == 0:
            return 'No Proofs Uploaded'
        else:
            if all([p.is_validated is True for p in self.proofs.all()]) is True:
                return 'Validated'
            else:
                return 'Validation Pending'

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('bet:detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        # ugly make a signal handler
        if not self.slug:
            self.slug = slugify(self.name)

        return super(Bet, self).save(*args, **kwargs)


class DonationRecipient(models.Model):
    """
    Set of donation recipients, @TODO store in a spearate app?
    """
    slug = models.SlugField()
    uuid = models.CharField(default=temp_uuid_gen(), max_length=255)
    url = models.URLField()
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def save(self, *args, **kwargs):
        # ugly make a signal handler
        if not self.slug:
            self.slug = slugify(self.name)

        return super(DonationRecipient, self).save(*args, **kwargs)


def _storage_path(instance, filename):
    return os.path.join('proof',
                        '%s-%s.zip' % (instance.bet_set.all().first().pk, instance.pk))


class Proof(models.Model):
    """
    Proofs of payment upload of pdf/image of paymetn receipt
    """
    file = models.FileField(upload_to=_storage_path)
    is_validated = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
