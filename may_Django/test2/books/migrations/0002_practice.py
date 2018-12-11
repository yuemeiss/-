# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-09 09:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Practice',
            fields=[
                ('pId', models.IntegerField(primary_key=True, serialize=False)),
                ('pName', models.CharField(max_length=10)),
                ('pAge', models.IntegerField()),
                ('pGender', models.BooleanField(default=False)),
                ('pAddress', models.CharField(max_length=50)),
                ('pPhone', models.CharField(max_length=11, null=True)),
                ('pSalary', models.DecimalField(decimal_places=2, max_digits=8)),
                ('pSection', models.CharField(max_length=20)),
            ],
        ),
    ]
