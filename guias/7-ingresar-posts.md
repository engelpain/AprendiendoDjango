#### Insertar datos al modelo

1. Crear la url para la vista que se utilizará para insertar datos, editando `nombreapp/urls.py`,
agregando la línea `url(r'^add/$', views.add, name='posts_add'),` al código final:

```python
# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views
 
urlpatterns = [
    # URL principal, READ
    url(r'^$', views.index, name='articulos_index'),
    # URL para insertar datos
    url(r'^add/$', views.add, name='articulos_add'),
]
```
2. Por convensión los formularios deben ir en un archivo que se los liste, a menos que se requieran
formulario más especializados. Para ello se debe crear un archivo `forms.py` en el directorio de la
aplicación `/nombreapp/forms.py`:
```python
# -*- coding: utf-8 -*-
from django import forms

# Se importa el modelo Artículo desde models.py
from .models import Articulo

# Se crea el Modelo tipo formulario del Modelo Artículo para rellenar los datos:
class ArticuloForm(forms.ModelForm):
    # La subclase Meta es heredada del modelo ModelForm
    class Meta:
        # Tabla de la base de datos donde se alojan los datos del modelo
        model = Articulo
        # Campos de la tabla que se llenaran en el formulario
        fields = ('titulo', 'cuerpo',)
```

3. Agregar el formulario a las views en `/nombreapp/views.py`:
```python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Se importa la dependencia HttpResponseRedirect
from django.shortcuts import render, HttpResponseRedirect

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
```

4. Se crea `add.html` en `/nombreapp/templates/add.html`
```python
{% extends "base.html" %}
 
{% block content %}
  <form action="" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Send">
  </form>
{% endblock %}
```

5. Crear un enlace a la nueva url agregada en `/nombreapp/templates/index.html`
```python
{% extends "base.html" %}


{% block content %}

<a href="/add">+ Agregar registro</a>

  {% if consultaArticulos %}
    {% for post in consultaArticulos %}
      <!-- {{ post.titulo }} [BEGIN] -->
      <h3>{{ post.titulo }}</h3>
      <div>{{ post.cuerpo }}</div>
      <!-- {{ post.titulo }} [ENDED] -->
    {% endfor %}
  {% else %}
    <p>No posts</p>
  {% endif %}

{% endblock %}
```