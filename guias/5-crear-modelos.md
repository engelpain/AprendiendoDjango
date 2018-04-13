### Crear modelos del app
Los modelos son objetos que utiliza Python para determinar el comportamiendo de una aplicación,
determinando los atributos y métodos de los objetos.
Los modelos de Django se escriben en el archivo `/nombreaplicacion/models.py `

1. Crear el modelo (para este ejemplo se creará un modelo que simulará un artículo de un blog):
```python

# Modelos Importados
from django.db import models
from django.utils import timezone

# Modelos del app
"""
Modelo Articulo:
Objeto para crear articulos en la aplicacion Blog

Nombre de la clase: Blog
Atributos de la clase:
  - author: Autor del articulo
  - title: Titulo del articulo
  - text: Texto del articulo
  - created_date: Fecha en la que fue creado el articulo
  - published_date: Fecha en la que fue publicado
Metodos de la clase:
    - publish: Agrega la fecha de publicacion al articulo
    - __str__: Muestra el titulo del articulo a la consulta de objetos
"""
class Articulo(models.Model):
    # Atributos
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    # Metodos
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.title

```
2. Luego de crear un modelo siempre hay que hacer las migraciones:
```shell
  /$ python manage.py makemigrations nombreapp
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