# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify

import uuid


def temp_uuid_gen(*args, **kwargs):
    return str(uuid.uuid4())


class Bet(models.Model):
    slug = models.SlugField()
    uuid = models.CharField(default=temp_uuid_gen(), max_length=255)
    name = models.CharField(max_length=255)
    description = models.TextField()
    recipient = models.URLField()  # multiple?
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('bet:detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        # ugly make a signal handler
        if not self.slug:
            self.slug = slugify(self.name)

        if not self.uuid:
            self.uuid = temp_uuid_gen()

        return super(Bet, self).save(*args, **kwargs)
