# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Fruit


@admin.register(Fruit)
class FruitAdmin(admin.ModelAdmin):

 	pass




# Register your models here.
