# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-22 16:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_import', '0002_auto_20160729_2012'),
    ]

    operations = [
        migrations.AddField(
            model_name='datafile',
            name='archived',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
