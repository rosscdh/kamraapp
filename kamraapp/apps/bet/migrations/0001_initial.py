# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField()),
                ('uuid', models.CharField(default=b'38014477-ea66-4170-af95-2b9b09fb67d9', max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('recipient', models.URLField()),
            ],
        ),
    ]
