# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-03 16:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0002_bugvotes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bugvotes',
            name='bug',
        ),
        migrations.RemoveField(
            model_name='bugvotes',
            name='voter',
        ),
        migrations.DeleteModel(
            name='BugVotes',
        ),
    ]
