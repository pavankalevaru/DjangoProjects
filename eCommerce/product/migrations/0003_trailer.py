# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-09-24 05:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20180914_2157'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trailer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('demo', models.TextField()),
            ],
        ),
    ]
