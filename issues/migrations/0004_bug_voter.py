# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-03 16:36
from __future__ import unicode_literals

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0003_auto_20181103_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='bug',
            name='voter',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name=django.contrib.auth.models.User),
        ),
    ]