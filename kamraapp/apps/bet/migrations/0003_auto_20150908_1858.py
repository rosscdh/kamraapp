# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bet', '0002_auto_20150905_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bet',
            name='access_secret',
            field=models.CharField(default=b'64c0c942-8922-4eb9-9193-dbbcd22892ba', max_length=255),
        ),
        migrations.AlterField(
            model_name='bet',
            name='access_token',
            field=models.CharField(default=b'c21e0af1-ac0b-4d0d-bc2c-7998fe6033d9', max_length=255),
        ),
        migrations.AlterField(
            model_name='bet',
            name='amount',
            field=models.DecimalField(default=5.0, null=True, max_digits=7, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='bet',
            name='proofs',
            field=models.ManyToManyField(to='bet.Proof', blank=True),
        ),
        migrations.AlterField(
            model_name='bet',
            name='slug',
            field=models.SlugField(unique=True, blank=True),
        ),
        migrations.AlterField(
            model_name='donationrecipient',
            name='slug',
            field=models.SlugField(unique=True, blank=True),
        ),
        migrations.AlterField(
            model_name='donationrecipient',
            name='uuid',
            field=models.CharField(default=b'103ea7fc-c94d-47e2-a356-92355b127d4a', max_length=255),
        ),
    ]
