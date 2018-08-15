# -*- coding: utf-8 -*-
"""!
* @software Aprendiendo Django 1.11
* @version 1.0 - 2018
* @author Ing. Angelo D. Osorio U.
* @license Fundación CENDITEL (2018)
* @file crud/urls.py
* @brief Rutas del módulo crud
"""

# Importa la función url desde Django
from django.conf.urls import url

# Importa las vistas creadas en crud/views.py
from .views import (
    CourseList,
    CourseDetail,
    CourseCreation,
    CourseUpdate,
    CourseDelete
)

urlpatterns = [
    # Lista los cursos creados
    url(r'^$', CourseList.as_view(), name='list'),
    
    # Edita el curso cuyo id sea igual al solicitado en la url
    url(r'^(?P<pk>\d+)$', CourseDetail.as_view(), name='detail'),

    # Envía al formulario para crear un nuevo curso
    url(r'^nuevo$', CourseCreation.as_view(), name='new'),
    
    # Edita un curso que se haya guardado con anterioridad
    url(r'^editar/(?P<pk>\d+)$', CourseUpdate.as_view(), name='edit'),

    # Solicita eliminar un curso
    url(r'^borrar/(?P<pk>\d+)$', CourseDelete.as_view(), name='delete'),
]
