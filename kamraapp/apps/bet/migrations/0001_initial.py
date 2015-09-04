# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import kamraapp.apps.bet.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField()),
                ('access_token', models.CharField(default=b'6fe7275a-db43-493d-89a0-6872f8d59d34', max_length=255)),
                ('access_secret', models.CharField(default=b'd9857f9f-91ef-46b4-ba85-abc08bd9d5b7', max_length=255)),
                ('name', models.CharField(max_length=255, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('sub_bet_type', models.CharField(blank=True, max_length=24, null=True, choices=[(b'parent', b'Parent'), (b'clone', b'Clone'), (b'bet_for', b'For'), (b'bet_against', b'Against')])),
                ('expires_at', models.DateTimeField(default=kamraapp.apps.bet.models._default_expiry)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('parent_bet', models.ForeignKey(blank=True, to='bet.Bet', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DonationRecipient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField()),
                ('uuid', models.CharField(default=b'6ad72929-acd9-4a9f-9c2d-01f60e93a8ec', max_length=255)),
                ('url', models.URLField()),
                ('name', models.CharField(max_length=255, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Proof',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.FileField(upload_to=kamraapp.apps.bet.models._storage_path)),
                ('is_validated', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='bet',
            name='proofs',
            field=models.ManyToManyField(to='bet.Proof'),
        ),
        migrations.AddField(
            model_name='bet',
            name='recipients',
            field=models.ManyToManyField(to='bet.DonationRecipient'),
        ),
        migrations.AddField(
            model_name='bet',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
