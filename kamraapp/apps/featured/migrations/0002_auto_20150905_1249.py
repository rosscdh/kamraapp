# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('featured', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='featuredbet',
            name='slug',
            field=models.SlugField(default='test'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='featureddonationrecipient',
            name='slug',
            field=models.SlugField(default='test'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='featuredbet',
            name='bet',
            field=models.ManyToManyField(to='bet.Bet', blank=True),
        ),
        migrations.AlterField(
            model_name='featureddonationrecipient',
            name='donation_recipient',
            field=models.ManyToManyField(to='bet.DonationRecipient', blank=True),
        ),
    ]
