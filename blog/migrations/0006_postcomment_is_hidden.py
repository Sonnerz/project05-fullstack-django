# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-15 17:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_postcomment_is_reported'),
    ]

    operations = [
        migrations.AddField(
            model_name='postcomment',
            name='is_hidden',
            field=models.BooleanField(default=False),
        ),
    ]
