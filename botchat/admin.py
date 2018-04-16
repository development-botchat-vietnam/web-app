# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(CheckLove)
admin.site.register(JoinGame )
admin.site.register(Question)
admin.site.register(RankLastMonth)
admin.site.register(Score)
admin.site.register(User)



