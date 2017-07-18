# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-18 00:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0006_auto_20170602_0925'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='appointment_date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='appointment',
            old_name='appointment_time',
            new_name='time',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='appointment_status',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='appointment_task',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='user',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
        migrations.AddField(
            model_name='appointment',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='status',
            field=models.CharField(max_length=38, null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='firstapp.User'),
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=38, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='dob',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=38),
        ),
    ]
