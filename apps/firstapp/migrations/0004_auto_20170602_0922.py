# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-02 14:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0003_auto_20170602_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dob',
            field=models.DateField(default=20, max_length=8),
        ),
    ]
