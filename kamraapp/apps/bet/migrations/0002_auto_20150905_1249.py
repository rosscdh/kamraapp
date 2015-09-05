# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bet', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bet',
            options={'ordering': ['-created_at', 'name']},
        ),
        migrations.AlterModelOptions(
            name='donationrecipient',
            options={'ordering': ['-weight', 'name']},
        ),
        migrations.AlterField(
            model_name='bet',
            name='access_secret',
            field=models.CharField(default=b'525f2367-47e6-41df-aa1e-233a4af30b91', max_length=255),
        ),
        migrations.AlterField(
            model_name='bet',
            name='access_token',
            field=models.CharField(default=b'afda14ff-ec5d-4344-b753-4de0d022da9d', max_length=255),
        ),
        migrations.AlterField(
            model_name='donationrecipient',
            name='uuid',
            field=models.CharField(default=b'de731a2f-008f-4b90-a4c3-5979eadf6931', max_length=255),
        ),
    ]
