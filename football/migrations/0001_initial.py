# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-04 11:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='footballClub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clubName', models.CharField(max_length=200)),
                ('clubJersey', models.CharField(max_length=50)),
                ('clubLeague', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='footballPlayers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playerName', models.CharField(max_length=100)),
                ('playernationality', models.CharField(max_length=50)),
            ],
        ),
    ]
