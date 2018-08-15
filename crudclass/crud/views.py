# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)

from django.core.urlresolvers import reverse_lazy
from .models import Course

# Listar cursos
class CourseList(ListView):
    model = Course

# Detalles del curso
class CourseDetail(DetailView):
    model = Course

# Crear un curso
class CourseCreation(CreateView):
    model = Course
    success_url = reverse_lazy('crud:list')
    fields = ['name', 'start_date', 'end_date']

# Actualizar un curso
class CourseUpdate(UpdateView):
    model = Course
    success_url = reverse_lazy('crud:list')
    fields = ['name', 'start_date', 'end_date']

# Eliminar un curso
class CourseDelete(DeleteView):
    model = Course
    success_url = reverse_lazy('crud:list')