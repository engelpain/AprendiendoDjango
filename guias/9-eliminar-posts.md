### Eliminar información

1. Crear la url modificando `/nombreapp/urls.py`:
```python
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
```

2. Añadir un enlace a la url en el template principal `/nombreapp/index.html`:

```html
{% extends "base.html" %}


{% block content %}
<a href="/add">+ Agregar registro</a>

  {% if consultaArticulos %}
    {% for post in consultaArticulos %}
      <!-- {{ post.titulo }} [BEGIN] -->
      <h3>{{ post.titulo }}</h3>
      <div>{{ post.cuerpo }}</div>
      <a href="{% url 'articulos_edit' id=post.id %}">Editar</a> 
      <a href="{% url 'articulos_delete' id=post.id %}">Eliminar</a>
      <!-- {{ post.titulo }} [ENDED] -->
    {% endfor %}
  {% else %}
    <p>No hay artículos</p>
  {% endif %}

{% endblock %}
```

3. Crear la vista en `/nombreapp/views.py`:
```python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Se importa la dependencia render
# Se importa la dependencia HttpResponseRedirect
# Se importa la dependencia get_object_or_404
# Se importa la dependencia redirect
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, redirect

# Se importa el modelo Articulo para poder consultarlo en la DB
from .models import Articulo

# Se importa el formulario ArticuloForm para poder consultarlo
from .forms import ArticuloForm

# Se importa la dependencia reverse desde django.urls
from django.urls import reverse





"""
# READ
  - Nombre del método: index
  - Descripción: View para consultar datos, predeterminada como índice de la página.
  - Requiere: 1 argumento (request)
    - request: la solicitud de la url de entrar a este método
  - Retorna: 1 función con 3 argumentos:
    - render: Renderiza la información de los 3 argumentos en el navegador
      - request: la solicitud de la url de entrar a este método
      - index.html: el template que llenará
      - context: los datos que se mostrarán
        - Dentro del context se realizará una consulta a la base de datos llamada consultaArticulos:
          consultaArticulos es un diccionario que se le envia a la vista con los elementos de la
          consulta que está solicitando, en este caso, todos los objetos "Articulo" ordenados de
          mayor a menor por el id.
"""
def index(request):
    context = {
        'consultaArticulos': Articulo.objects.all().order_by('-id')
    }
    return render(request, 'index.html', context)





"""
# CREATE:
  - Nombre del método: add
  - Descripción: View para el formulario que guardará datos de entrada.
  - Requiere: 1 argumento (request)
    - request: la solicitud de la url de entrar a este método
  - Condición:
    - Si hay un request por método POST, es decir, si se enviaron datos desde el formulario:
      - Validar los datos, en caso de ser válidos, guardarlos en la base de datos y volver al índice
    - Caso contrario: Volver al formulario
  - Retorna: 1 función con 3 argumentos:
    - render: Renderiza la información de los 3 argumentos en el navegador
      - request: la solicitud de la url de entrar a este método
      - add.html: el template que llenará
      - context: Se llenará con el formulario ArticuloForm, definido de /nombreapp/forms.py
"""
def add(request):
    if request.method == "POST":
        form = ArticuloForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('articulos_index'))
    else:
        form = ArticuloForm()
    context = { 'form' : form }
    return render(request, 'add.html', context)





"""
# UPDATE:
  - Nombre del método: edit
  - Descripción: View para el formulario que modificará datos de existentes en la DB.
  - Requiere: 2 argumentos (request, id)
    - request: la solicitud de la url de entrar a este método.
    - id: ID del artículo que se modificará.
  - Instanciación:
    - consulta instancia el modelo Articulo donde el id sea igual al solicitado. 
  - Condición:
    - Si hay un request por método POST, es decir, si se enviaron datos desde el formulario:
      - Validar los datos, en caso de ser válidos, guardarlos en la base de datos y volver al índice
    - Caso contrario: Volver al formulario.
  - Retorna: 1 función con 3 argumentos:
    - render: Renderiza la información de los 3 argumentos en el navegador.
      - request: la solicitud de la url de entrar a este método.
      - add.html: el template con el formulario usado en add, pero relleno con los datos.
      - context: Se llenará con el formulario ArticuloForm, definido de /nombreapp/forms.py
"""
def edit(request, id):
    consulta = get_object_or_404(Articulo, id=id)
    if request.method == "POST":
        form = ArticuloForm(request.POST, instance=consulta)
        if form.is_valid():
            consulta = form.save(commit=False)
            consulta.save()
            return redirect('articulos_index')
    else:
        form = ArticuloForm(instance=consulta)
        context = { 'form': form }
    return render(request, 'add.html', context)





"""
# DELETE:
  - Nombre del método: delete
  - Descripción: View para eliminar datos existentes en la DB.
  - Requiere: 2 argumentos (request, id)
    - request: la solicitud de la url de entrar a este método.
    - id: ID del artículo que se eliminará.
  - Instanciación:
    - post instancia el modelo Articulo por id.
  - Función: En caso de encontrar el artículo especificado con el id, eliminarlo.
  - Retorna: 1 función con 1 argumento:
    - redirect: Redirecciona a una url
      - articulos_index: url a la que será redireccionada en caso de haberse elimiado con éxito
"""
def delete(request, id):
    post = get_object_or_404(Articulo, id=id)
    post.delete()
    return redirect('articulos_index')
```