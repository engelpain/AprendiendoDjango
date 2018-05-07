# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views
 
urlpatterns = [
    # URL principal, READ
    url(r'^$', views.index, name='articulos_index'),
    # URL para insertar datos, CREATE
    url(r'^add/$', views.add, name='articulos_add'),
    # URL para modificar datos, UPDATE
    url(r'^(?P<id>\d+)/edit$', views.edit, name='articulos_edit'),
    # URL para eliminar datos, DELETE
    url(r'^(?P<id>\d+)/delete$', views.delete, name='articulos_delete'),
]