# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-17 05:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20170313_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='postphoto',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]