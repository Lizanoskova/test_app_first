# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models

# Create your models here.

class Fruit(models.Model):
    
    name = models.CharField(max_length=255,verbose_name='Name')
    color = models.CharField(max_length=255,verbose_name='Color')
    produced_at = models.DateTimeField(auto_now_add=True)
    is_eaten = models.BooleanField(default=False)
