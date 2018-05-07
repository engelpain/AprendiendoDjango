# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

"""
Modelo Post:
Descripción del modelo:
  - Objeto para crear artículos en una aplicación para hacer post, al estilo de un blog
Atributos de la clase:
  - titulo = Título del artículo, type Char(250)
  - cuerpo = Texto del artículo, type Text
  - creado = Fecha de creación del artículo, type DateTime, es rellenado automáticamente
  - modificado = Fecha de creación del artículo, type DateTime, es rellenado automáticamente
Métodos de la clase:
    - __unicode__(self) = Método para asignar un dato como nombre del objeto al consultarlo
    Requiere el objeto que consulta y retorna el nombre del dato que se asigne, en este ejemplo
    devuelve el título.
"""
from django.db import models
 
class Articulo(models.Model):
    titulo = models.CharField(max_length=250)
    cuerpo = models.TextField()
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return self.titulo