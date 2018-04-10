## Guía para crear un proyecto básico con Django
Centro Nacional de Desarrollo e Investigación de Tecnologías Libres (CENDITEL) <br>
[CENDITEL](https://www.cenditel.gob.ve/), Mérida - Venezuela<br>
Dirección de Desarrollo<br>
Autor: [Ing. Angelo Osorio](https://twitter.com/Engel_PAIN)<br>
Fecha de Elaboración: 26-12-2017 (dd,mm,aaaa)

### Notas del autor
El símbolo al principio de una línea de comandos indica:
```
  $ = hacer la sentencia como usuario
  # = hacer la sentencia como administrador
  ~$ = indica que está en el home del usuario
  ~/django$ = indica que está en un directorio llamado django
```

### Pasos para crear un proyecto
1. [Construir un nuevo proyecto en Django](#construir-un-nuevo-proyecto-en-django)
2. [Conectar el proyecto con una base de datos](#conectar-el-proyecto-con-una-base-de-datos)
3. [Correr el servidor local](#correr-el-servidor-local)
4. [Crear una aplicación](#crear-una-aplicaci%C3%B3n-con-Django)
5. [Crear modelos](#crear-modelos-del-app)
5. [Crear URLS](#urls)


### Construir un nuevo proyecto en Django
Construir un nuevo proyecto:
```
  ~$ django-admin.py startproject nombredelproyecto
```
Django crea el siguiente esquema de archivos:
```
nombredelproyecto/
  manage.py
  nombredelproyecto/
    __init__.py
    settings.py
    urls.py
    wsgi.py
```

### Conectar el proyecto con una base de datos
>Nota: En caso de querer utilizar la base de datos que trae por defecto Django, saltarse este paso

1. Instalar el complemento que requiera Python para enlazar con el gestor de base de datos:
  - **MySQL**:
```shell
    # apt-get install python-mysqldb
```

  - **PostgreSQL**:
```shell
    $ aptitude install python-psycopg2
```

2. Crear una base de datos para el proyecto, en un gestor de base de datos, en este caso PostgreSQL:
```shell
    postgres=# CREATE DATABASE nombredelproyecto
```

3. Abrir el archivo `nombredelproyecto/settings.py` dentro de nombredelproyecto:
```shell
    ~/nombredelproyecto/nombredelproyecto$ nano settings.py
```

4. Allí hay que buscar la sección `DATABASES` y agregar y reemplazar los datos, por defecto son:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase',
    }
}
```
  4.1. La línea `'ENGINE'` define el gestor de base de datos con el que se enlazará. Por defecto
  está enlazado con **sqlite**, pero se puede cambiar a otros gestores de base de datos.
    - Mysql: `'ENGINE': 'django.db.backends.mysql',`
    - PostgreSQL: `'ENGINE': 'django.db.backends.postgresql_psycopg2',`

  4.2. La `'NAME'` define el nombre de la base de datos: `'NAME': 'nombrebasededatos',`

  4.3. Agregar la tupla `'USER'` para agregar el usuario que tiene acceso a esa base de datos:
  `'USER': 'usuario',`
  
  4.4. Agregar la tupla `'PASSWORD'` para agregar la contraseña del usuario que tiene acceso a esa
  base de datos: `'PASSWORD': 'clave',`
  
  4.5. Agregar la tupla `'HOST'` para asignar la dirección a donde apuntará la conexión:
  `'HOST': 'localhost',`
  
  4.6. Agregar la tupla `'PORT'` para : `'PORT': '5432',`

Debería quedar así:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'nombrebasededatos',
        'USER': 'usuario',
        'PASSWORD': 'clave',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

5. Ahora solo usar el comando:
```
    ~/nombredelproyecto$ python manage.py migrate
```

### Correr el servidor local

1. Correr el servidor local de Django
```
  ~/nombredelproyecto$ python manage.py runserver
```
2. Desde el navegador web se entra al servidor local de Django en la dirección _127.0.0.0:8000_ o
_localhost:8000_

>Para poder otorgar acceso a otros equipos que estén dentro de la misma red para utilizar el
servidor local: `~/nombredelproyecto$ python manage.py runserver 0.0.0.0:8000`


### Crear una aplicación con Django
1. Crear el directorio donde estarán las aplicaciones, el nombre del directorio no tiene relevancia:
```
  ~/nombredelproyecto$ mkdir apps
```

2. Entrar en el directorio y crear un archivo `__init__.py`, esto para hacerle saber a Django que es
un paquete o que hay paquetes dentro de él).
```
  ~/nombredelproyecto/apps$ touch __init__.py
```

3. Crear una nueva aplicación:
```
  ~/nombredelproyecto/apps$ django-admin.py startapp nombreapp
```

4. Agregar la aplicación al proyecto modificando el archivo `nombredelproyecto/nombredelproyecto/settings.py`:
```
  ~/nombredelproyecto/nombredelproyecto$ nano settings.py
```

5. Allí hay que buscar la sección `INSTALLED_APPS` y agregar la nueva aplicación:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.nombreapp',
]
```

### Crear modelos del app

Los modelos son objetos que utiliza Django para determinar el comportamiendo de una aplicación.
Los modelos de Django se escriben en el archivo `nombredelproyecto/apps/nombreaplicacion/models.py `

1. Crear el modelo, para este ejemplo se creará un modelo que simulará un artículo de un blog.
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
2. Hacer las migraciones:
```shell
  ~/nombredelproyecto$ python manage.py makemigrations nombreapp
  Migrations for 'nombreapp':
    0001_initial.py:
    - Create model Articulo
```
3. Migrar las migraciones hechas:
```shell
  ~/nombredelproyecto$ python manage.py migrate blog
  Operations to perform:
    Apply all migrations: blog
  Running migrations:
    Applying blog.0001_initial... OK
```

###URLS

1. Abrir el archivo `nombredelproyecto/nombredelproyecto/urls.py`

```shell
  ~/nombredelproyecto$ python manage.py migrate blog
  Operations to perform:
    Apply all migrations: blog
  Running migrations:
    Applying blog.0001_initial... OK
```