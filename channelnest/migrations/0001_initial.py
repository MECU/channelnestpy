# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-25 20:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'db_table': 'type',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=256)),
                ('date_created', models.DateTimeField(verbose_name='date published')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='channelnest.Type')),
            ],
            options={
                'db_table': 'video',
            },
        ),
    ]