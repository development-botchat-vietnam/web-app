# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import *

class Question2Admin(admin.ModelAdmin):
    list_display = ('question', 'a', 'b', 'c','d', 'anwser')
    exclude = ('active',)


admin.site.register(Question2, Question2Admin)