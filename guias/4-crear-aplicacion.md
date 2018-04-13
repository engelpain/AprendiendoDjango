### Crear una aplicación con Django
1. Crear una nueva aplicación:
   * `/$ django-admin.py startapp nombreapp`
2. Agregar la aplicación al proyecto modificando el archivo `/nombredelproyecto/settings.py`.
3. Allí hay que buscar la sección `INSTALLED_APPS` y agregar la nueva aplicación:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'nombreapp',
]
```