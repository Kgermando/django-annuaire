# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-16 09:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0009_auto_20181016_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='number_1',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='post',
            name='number_2',
            field=models.CharField(blank=True, max_length=25),
        ),
    ]
