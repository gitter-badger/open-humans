# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-25 16:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vcf_data', '0002_auto_20160720_0621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdata',
            name='genome_file',
        ),
    ]
