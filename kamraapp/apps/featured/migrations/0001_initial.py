# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('bet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeaturedBet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('excerpt', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('is_published', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('data', jsonfield.fields.JSONField(default={})),
                ('bet', models.ManyToManyField(to='bet.Bet', null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FeaturedDonationRecipient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('excerpt', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('is_published', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('data', jsonfield.fields.JSONField(default={})),
                ('donation_recipient', models.ManyToManyField(to='bet.DonationRecipient', null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
