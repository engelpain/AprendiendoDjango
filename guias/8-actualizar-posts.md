### Modificar datos ingresados en el modelo

1. Crear la url para la vista que se utilizará para modificar datos, editando `nombreapp/urls.py`,
agregando la línea `url(r'^(?P<id>\d+)/edit$', views.edit, name='posts_edit'),` al código final:
```python
# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views
 
urlpatterns = [
    # URL principal, READ
    url(r'^$', views.index, name='articulos_index'),
    # URL para insertar datos
    url(r'^add/$', views.add, name='articulos_add'),
    # URL para modificar datos
    url(r'^(?P<id>\d+)/edit$', views.edit, name='articulos_edit'),
]
```

2. Agregar un enlace a la url recién creada en `nombreapp/templates/index.html`:

```html
{% extends "base.html" %}


{% block content %}
<a href="/add">+ Agregar registro</a>

  {% if consultaArticulos %}
    {% for post in consultaArticulos %}
      <!-- {{ post.titulo }} [BEGIN] -->
      <h3>{{ post.titulo }}</h3>
      <div>{{ post.cuerpo }}</div>
      <a href="{% url 'articulos_edit' id=articulo.id %}">Editar</a>
      <!-- {{ post.titulo }} [ENDED] -->
    {% endfor %}
  {% else %}
    <p>No posts</p>
  {% endif %}

{% endblock %}
```