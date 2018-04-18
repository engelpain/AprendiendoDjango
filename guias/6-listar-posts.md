#### Listar posts del modelo

1. Crear un archivo dentro de `nombreapp` que se llame `urls.py`, dentro escribir:
```python
from django.conf.urls import url
 
from . import views
 
urlpatterns = [
  url(r'^$', views.index, name='articulos_index'),
]
```

2. Abrir el archivo `/nombredelproyecto/urls.py`, debería aparecer algo similar a esto:
```python
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]
```

3. Agregar las url de la aplicación aquí, escribiendo `url(r'^', include('nombreapp.urls')),` e
importar `include` desde `django.conf.urls`:
```python
# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    # Url para entrar al admin
    url(r'^admin/', admin.site.urls),

    # Urls de la aplicación nombreapp
    url(r'^', include('nombreapp.urls')),
]
```

4. Las url apuntan a una vista que no existe, hay que crearla. Para eso hay que incorporarla en
`/nombreapp/views.py`:

```python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

# Se importa el modelo Articulo para poder consultarlo en la DB
from .models import Articulo

# READ: View para consultar datos, predeterminada como índice de la página
def index(request):
    context = {
        # consultaArticulos es un diccionario que se le envia a la vista con los elementos de la
        # consulta que está solicitando. El mismo debe ser convocado en la vista para poder ser
        # utilizado. 
        'consultaArticulos': Articulo.objects.all().order_by('-id')
    }
    return render(request, 'index.html', context)
```
5. Crear un directorio donde estarán las templates del sistema llamado `templates`:
```shell
   $ mkdir nombreapp/templates
```

6. Dentro de `templates` hay que crear un archivo que servirá de base para todas las vistas llamado
`base.html`:
```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Blog</title>
</head>
<body>
  <h2>Blog header</h2>
  {% block content %}
  {% endblock %}
</body>
</html>
```

7. La view creada en el paso 4 apunta a un archivo que no existe llamado `index.html`, ésta estará
en el directorio `templates` y heredará todo el código que está en `base.html`:
```html
{% extends "base.html" %}
 
{% block content %}
  {% if consultaArticulos %}
    {% for post in consultaArticulos %}
      
      <!-- Título del post -->
      <h3>{{ post.titulo }}</h3>
      
      <!-- Cuerpo del post -->
      <div>{{ post.cuerpo }}</div>

    {% endfor %}
  {% else %}
    <p>No posts</p>
  {% endif %}
{% endblock %}
```