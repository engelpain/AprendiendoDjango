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