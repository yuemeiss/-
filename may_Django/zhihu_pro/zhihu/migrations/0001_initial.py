# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-09 17:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.CharField(max_length=80, primary_key=True, serialize=False)),
                ('content', models.TextField(blank=True, null=True)),
                ('pub_time', models.CharField(blank=True, max_length=80, null=True)),
                ('update_time', models.CharField(blank=True, max_length=80, null=True)),
                ('endorse', models.CharField(blank=True, max_length=50, null=True)),
                ('comment_num', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'answer',
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.CharField(max_length=80, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=80, null=True)),
                ('gender', models.CharField(blank=True, max_length=3, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('add_desc', models.TextField(blank=True, null=True)),
                ('headline', models.CharField(blank=True, max_length=255, null=True)),
                ('intro', models.CharField(blank=True, max_length=255, null=True)),
                ('school', models.CharField(blank=True, max_length=100, null=True)),
                ('jobname', models.CharField(blank=True, max_length=100, null=True)),
                ('answer_count', models.CharField(blank=True, max_length=50, null=True)),
                ('question_count', models.CharField(blank=True, max_length=50, null=True)),
                ('follower_count', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'author',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.CharField(max_length=80, primary_key=True, serialize=False)),
                ('author_name', models.CharField(blank=True, max_length=100, null=True)),
                ('pub_time', models.CharField(blank=True, max_length=50, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('like_num', models.CharField(blank=True, max_length=50, null=True)),
                ('child_comment_count', models.CharField(blank=True, max_length=50, null=True)),
                ('child_comments', models.TextField(blank=True, null=True)),
                ('aid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zhihu.Answer')),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zhihu.Author')),
            ],
            options={
                'db_table': 'comment',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.CharField(max_length=80, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=80, null=True)),
                ('pub_time', models.CharField(blank=True, max_length=80, null=True)),
                ('answer_count', models.CharField(blank=True, max_length=50, null=True)),
                ('follower_count', models.CharField(blank=True, max_length=50, null=True)),
                ('intro', models.CharField(blank=True, max_length=255, null=True)),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zhihu.Author')),
            ],
            options={
                'db_table': 'question',
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.CharField(max_length=80, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=80, null=True)),
                ('intro', models.TextField(blank=True, null=True)),
                ('tag_url', models.CharField(blank=True, max_length=255, null=True)),
                ('qtype', models.ManyToManyField(to='zhihu.Question')),
            ],
            options={
                'db_table': 'tags',
            },
        ),
        migrations.AddField(
            model_name='answer',
            name='ahthor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zhihu.Author'),
        ),
        migrations.AddField(
            model_name='answer',
            name='qid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zhihu.Question'),
        ),
    ]
