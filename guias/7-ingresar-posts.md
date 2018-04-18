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
        # add to the DB
        form = ArticuloForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('articulos_index'))
 
    else:
        # show the form
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