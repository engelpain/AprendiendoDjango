#### Listar posts del modelo

1. Crear un archivo dentro de `nombreaplicacion` que se llame `urls.py`, dentro escribir:
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

3. Agregar las url de la aplicación aquí, escribiendo `url(r'^', include('nombreapp.urls')),`:
```python
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('nombreapp.urls')),
]
```

4. Las url apuntan a una vista que no existe, hay que crearla. Para eso hay que incorporarla en

```python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
 
from django.shortcuts import render
 
from .models import Post
 
def index(request):
  context = {
    'posts': Post.objects.all().order_by('-id')
  }
  return render(request, 'index.html', context)