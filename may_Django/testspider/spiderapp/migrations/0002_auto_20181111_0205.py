# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-10 18:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('spiderapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='qiushipro',
            old_name='localImg',
            new_name='localImgPath',
        ),
        migrations.AddField(
            model_name='qiushipro',
            name='operator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]