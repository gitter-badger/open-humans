# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-09 04:11
from __future__ import unicode_literals

import data_import.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('studies', '0014_auto_20160210_2328'),
        ('data_import', '0007_auto_20160111_0654'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(max_length=1024, upload_to=data_import.models.get_upload_path)),
                ('metadata', jsonfield.fields.JSONField(default={})),
                ('source', models.CharField(max_length=32)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='datafiles', to='data_import.DataRetrievalTask')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='datafiles', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='NewDataFileAccessLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('ip_address', models.GenericIPAddressField()),
                ('data_file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_import.DataFile')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='testdatafile',
            name='task',
        ),
        migrations.RemoveField(
            model_name='testdatafile',
            name='user_data',
        ),
        migrations.DeleteModel(
            name='TestDataFile',
        ),
    ]