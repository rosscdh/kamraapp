# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bet',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 31, 15, 47, 17, 595534), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bet',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 31, 15, 47, 25, 147671), auto_now=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bet',
            name='uuid',
            field=models.CharField(default=b'abbbbb75-3f52-43be-93c6-cada61d7cec9', max_length=255),
        ),
    ]
