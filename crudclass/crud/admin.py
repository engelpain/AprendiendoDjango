# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Course

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
  ordering = ('-id',)
  search_fields = ('name', 'start_date', 'end_date', )
 
admin.site.register(Course, CourseAdmin)