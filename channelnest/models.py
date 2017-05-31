# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Type(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "type"


class Video(models.Model):
    id = models.CharField(max_length=32, primary_key=True)
    title = models.CharField(max_length=256)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    date_created = models.DateTimeField('date published')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "video"

