# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-08 12:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20181108_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]
