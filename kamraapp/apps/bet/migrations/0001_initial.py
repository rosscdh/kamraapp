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
                ('access_token', models.CharField(default=b'3b2c8855-e597-4773-81c4-06bebdd31966', max_length=255)),
                ('access_secret', models.CharField(default=b'a511caa3-5a95-4b95-8559-3541d9e10416', max_length=255)),
                ('name', models.CharField(max_length=255, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('sub_bet_type', models.CharField(blank=True, max_length=24, null=True, choices=[(b'parent', b'Parent'), (b'clone', b'Clone'), (b'bet_for', b'For'), (b'bet_against', b'Against')])),
                ('data', jsonfield.fields.JSONField(default={})),
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
                ('uuid', models.CharField(default=b'd00c822a-8e5e-4a53-a3fa-9d3c0db52ca0', max_length=255)),
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
