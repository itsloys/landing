# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-07-22 10:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20180719_0115'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='page',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
