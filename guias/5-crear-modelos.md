### Crear modelos del app
Los modelos son objetos que utiliza Python para determinar el comportamiendo de una aplicación,
determinando los atributos y métodos de los objetos.
Los modelos de Django se escriben en el archivo `/nombreaplicacion/models.py`

1. Crear el modelo (para este ejemplo se creará un modelo que simulará un artículo de un blog):
```python
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
```
2. Luego de crear un modelo siempre hay que hacer las migraciones:
```shell
  /$ python manage.py makemigrations
  Migrations for 'nombreapp':
    0001_initial.py:
    - Create model Articulo
```
3. Migrar las migraciones hechas:
```shell
  /$ python manage.py migrate blog
  Operations to perform:
    Apply all migrations: blog
  Running migrations:
    Applying blog.0001_initial... OK
```
4. Para poder utilizar este modelo desde el admin de Django hay que agregarlo al archivo `/nombreaplicacion/admin.py`
```python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Articulo
 
class ArticuloAdmin(admin.ModelAdmin):
  ordering = ('-id',)
  search_fields = ('titulo', 'cuerpo',)
 
admin.site.register(Articulo, ArticuloAdmin)
```