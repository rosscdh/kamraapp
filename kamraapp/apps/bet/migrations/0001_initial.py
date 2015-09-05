# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields
import kamraapp.apps.bet.models
from django.conf import settings


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
                ('access_token', models.CharField(default=b'443e2899-fe15-4c55-90f2-a94164ea12fa', max_length=255)),
                ('access_secret', models.CharField(default=b'8bfaf660-f488-484c-8208-9ebad098e383', max_length=255)),
                ('name', models.CharField(max_length=255, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('amount', models.IntegerField(default=5.0, null=True, blank=True)),
                ('sub_bet_type', models.CharField(blank=True, max_length=24, null=True, choices=[(b'parent', b'Parent'), (b'clone', b'Clone'), (b'bet_for', b'For'), (b'bet_against', b'Against')])),
                ('data', jsonfield.fields.JSONField(default={})),
                ('expires_at', models.DateTimeField(default=kamraapp.apps.bet.models._default_expiry)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('parent_bet', models.ForeignKey(blank=True, to='bet.Bet', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DonationRecipient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField()),
                ('uuid', models.CharField(default=b'1c8a5fa0-8f88-4ca6-98bc-b2dfaf74ab79', max_length=255)),
                ('url', models.URLField()),
                ('name', models.CharField(max_length=255, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('weight', models.IntegerField(default=0)),
                ('data', jsonfield.fields.JSONField(default={})),
            ],
        ),
        migrations.CreateModel(
            name='Proof',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.FileField(upload_to=kamraapp.apps.bet.models._storage_path)),
                ('is_validated', models.BooleanField(default=False)),
                ('data', jsonfield.fields.JSONField(default={})),
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
