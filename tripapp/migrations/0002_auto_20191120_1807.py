# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-11-20 15:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tripapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entries',
            old_name='age',
            new_name='email',
        ),
        migrations.AddField(
            model_name='entries',
            name='platenbr',
            field=models.CharField(blank=True, null=True, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entries',
            name='user_id',
            field=models.CharField(blank=True, null=True, max_length=30),
            preserve_default=False,
        ),
    ]
