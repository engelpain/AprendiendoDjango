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

3. Agregar la vista de la nueva clase a `nombreapp/views.py`, importando también `get_object_or_404`
y `redirect`:
```python
...
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



# READ: View para consultar datos, predeterminada como índice de la página
def index(request):
    context = {
        # consultaArticulos es un diccionario que se le envia a la vista con los elementos de la
        # consulta que está solicitando. El mismo debe ser convocado en la vista para poder ser
        # utilizado. 
        'consultaArticulos': Articulo.objects.all().order_by('-id')
    }
    return render(request, 'index.html', context)

# CREATE: View para el formulario que guardará datos de entrada:
def add(request):
    if request.method == "POST":
        form = ArticuloForm(request.POST)
        # Revisa si los datos son válidos
        if form.is_valid():
            # Guarda los datos en la DB
            form.save()
            return HttpResponseRedirect(reverse('articulos_index'))
    else:
        # Muestra el formulario
        form = ArticuloForm()
    # Devuelve el contexto del formulario
    context = { 'form' : form }
    return render(request, 'add.html', context)

# UPDATE: View para el formulario que modificará datos de existentes en la DB:
def edit(request, id):
  post = get_object_or_404(Post, id=id)
  if request.method == "POST":
    # update DB
    form = ArticuloForm(request.POST, instance=post)
    if form.is_valid():
      post = form.save(commit=False)
      post.save()
      return redirect('articulos_index')
  else:
    # show the form
    form = ArticuloForm(instance=post)
    
  context = { 'form': form }
  return render(request, 'add.html', context)
```