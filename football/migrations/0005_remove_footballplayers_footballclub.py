# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-07 10:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0004_footballplayers_footballclub'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='footballplayers',
            name='footballclub',
        ),
    ]