# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-11 06:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spiderapp', '0002_auto_20181111_0205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qiushipro',
            name='operator',
        ),
        migrations.AlterField(
            model_name='qiushipro',
            name='comment_list',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='qiushipro',
            name='comment_num',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='qiushipro',
            name='content',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='qiushipro',
            name='funny_num',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='qiushipro',
            name='img_url',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='qiushipro',
            name='localImgPath',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='qiushipro',
            name='title',
            field=models.CharField(max_length=188, null=True),
        ),
    ]