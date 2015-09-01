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
                ('access_token', models.CharField(default=b'bec09c4e-01e4-40e2-94a4-b703d2cbe155', max_length=255)),
                ('access_secret', models.CharField(default=b'22c68107-ffdf-44c5-b819-7b642b282f2b', max_length=255)),
                ('name', models.CharField(max_length=255, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
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
                ('uuid', models.CharField(default=b'cc8a6f52-c902-4e50-8910-3dcf7ac30ed5', max_length=255)),
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
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
