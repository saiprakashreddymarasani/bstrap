# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-22 01:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=25)),
                ('age', models.IntegerField(max_length=2)),
            ],
        ),
    ]
