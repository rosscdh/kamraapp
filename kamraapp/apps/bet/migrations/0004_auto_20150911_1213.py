# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bet', '0003_auto_20150908_1858'),
    ]

    operations = [
        migrations.AddField(
            model_name='donationrecipient',
            name='tag',
            field=models.CharField(max_length=64, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='bet',
            name='access_secret',
            field=models.CharField(default=b'b7e44c83-bab7-49f0-a73a-9f672d054c20', max_length=255),
        ),
        migrations.AlterField(
            model_name='bet',
            name='access_token',
            field=models.CharField(default=b'fe99c638-babc-4c95-b9cb-ba71a7ccce4f', max_length=255),
        ),
        migrations.AlterField(
            model_name='donationrecipient',
            name='uuid',
            field=models.CharField(default=b'd188e76b-c4a5-4dfb-9bcc-ab804aeb414d', max_length=255),
        ),
    ]
