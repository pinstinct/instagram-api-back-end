# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-17 08:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_auto_20170317_1723'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='name',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='relationships',
        ),
        migrations.RemoveField(
            model_name='relationship',
            name='type',
        ),
        migrations.AddField(
            model_name='myuser',
            name='relation',
            field=models.ManyToManyField(related_name='relation_user_set', through='member.Relationship', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='relationship',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='relationship',
            name='relation_type',
            field=models.CharField(choices=[('f', 'Following'), ('b', 'Blocked')], default='', max_length=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='relationship',
            name='from_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relations_from_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='to_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relations_to_user', to=settings.AUTH_USER_MODEL),
        ),
    ]