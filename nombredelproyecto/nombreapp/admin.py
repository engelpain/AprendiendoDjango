# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Articulo
 
class ArticuloAdmin(admin.ModelAdmin):
  ordering = ('-id',)
  search_fields = ('titulo', 'cuerpo',)
 
admin.site.register(Articulo, ArticuloAdmin)