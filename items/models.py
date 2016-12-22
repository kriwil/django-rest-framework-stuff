# -*- coding: utf-8 -*-

from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=255)
    number = models.IntegerField()

