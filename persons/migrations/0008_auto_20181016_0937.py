# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-16 08:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0007_auto_20181015_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='number_2',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
