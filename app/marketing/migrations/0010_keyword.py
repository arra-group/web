# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-02 07:32
from __future__ import unicode_literals

from django.db import migrations, models
import economy.models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0009_auto_20171128_1915'),
    ]

    operations = [
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('keyword', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
