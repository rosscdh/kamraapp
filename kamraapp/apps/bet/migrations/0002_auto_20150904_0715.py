# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bet',
            name='access_secret',
            field=models.CharField(default=b'b4f19bef-3743-4117-b648-c9483a1faaa8', max_length=255),
        ),
        migrations.AlterField(
            model_name='bet',
            name='access_token',
            field=models.CharField(default=b'221e9d16-fc70-4553-b8bf-a7c4a7037150', max_length=255),
        ),
        migrations.AlterField(
            model_name='donationrecipient',
            name='uuid',
            field=models.CharField(default=b'c6d21394-d318-4eed-8f5e-803ec629ff87', max_length=255),
        ),
    ]
