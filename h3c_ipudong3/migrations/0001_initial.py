# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apinform',
            fields=[
                ('ap_oid', models.CharField(max_length=60, serialize=False, primary_key=True)),
                ('ap_location', models.CharField(max_length=40, null=True, blank=True)),
                ('ap_warning', models.CharField(max_length=3, null=True, blank=True)),
                ('ap_remarks', models.CharField(max_length=50, null=True, blank=True)),
                ('ap_warnsw', models.CharField(max_length=3, null=True, blank=True)),
                ('mailed', models.CharField(max_length=3, null=True, blank=True)),
                ('ap_status', models.CharField(max_length=3, null=True, blank=True)),
            ],
            options={
                'db_table': 'Apinform',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Apname',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ap_oid', models.CharField(max_length=60, null=True, blank=True)),
                ('ap_name', models.CharField(max_length=40, null=True, blank=True)),
            ],
            options={
                'db_table': 'Apname',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ap_oid', models.CharField(max_length=60, null=True, blank=True)),
                ('ap_location', models.CharField(max_length=40, null=True, blank=True)),
            ],
            options={
                'db_table': 'Location',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ap_oid', models.CharField(max_length=60, null=True, blank=True)),
                ('ap_status', models.CharField(max_length=12, null=True, blank=True)),
                ('update_time', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'db_table': 'Status',
                'managed': False,
            },
        ),
    ]
