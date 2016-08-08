# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-27 21:38
from __future__ import unicode_literals

from django.db import migrations, models
import private_sharing.models


class Migration(migrations.Migration):

    dependencies = [
        ('private_sharing', '0033_auto_20160630_1936'),
    ]

    operations = [
        migrations.AddField(
            model_name='datarequestproject',
            name='token_expiration_date',
            field=models.DateTimeField(default=private_sharing.models.now_plus_24_hours),
        ),
        migrations.AddField(
            model_name='datarequestproject',
            name='token_expiration_disabled',
            field=models.BooleanField(default=False),
        ),
    ]