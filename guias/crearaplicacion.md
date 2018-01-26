## Guía para crear un proyecto básico con Django
Centro Nacional de Desarrollo e Investigación de Tecnologías Libres (CENDITEL) <br>
[CENDITEL](https://www.cenditel.gob.ve/), Mérida - Venezuela<br>
Dirección de Desarrollo<br>
Autor: [Ing. Angelo Osorio](https://twitter.com/Engel_PAIN)<br>
Fecha de Elaboración: 26-12-2017 (dd,mm,aaaa)

### Notas del autor
El símbolo al principio de una línea de comandos indica:
    `$ = hacer la sentencia como usuario`
    `# = hacer la sentencia como administrador`
    `~$ = indica que está en el home del usuario`
    `~/django$ = indica que está en un directorio llamado django`

### Pasos para crear un proyecto
1. [Construir un nuevo proyecto en Django](#construir-un-nuevo-proyecto-en-django)
2. [Crear una aplicación](#crear-una-aplicaci%C3%B3n-con-Django)
3. [Conectar el proyecto con una base de datos](#conectar-el-proyecto-con-una-base-de-datos)
3. [Correr el servidor local](#correr-el-servidor-local)

### Construir un nuevo proyecto en Django
Construir un nuevo proyecto:
    `~$ django-admin.py startproject nombredelproyecto`
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

### Crear una aplicación con Django
1. Crear el directorio donde estarán las aplicaciones, el nombre del directorio no tiene relevancia:
    `~/nombredelproyecto$ mkdir apps`

2. Entrar en el directorio y crear un archivo `__init__.py`, esto para hacerle saber a Django que es
un paquete o que hay paquetes dentro de él).
    `~/nombredelproyecto/apps$ touch __init__.py`

4. Crear una nueva aplicación:
    `~/nombredelproyecto/apps$ django-admin.py startapp nombreapp`

5. Agregar la aplicación al proyecto modificando el archivo `nombredelproyecto/settings.py`:
    `~/nombredelproyecto$ nano settings.py`

6. Allí hay que buscar la sección `INSTALLED_APPS` y agregar la nueva aplicación:
```
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

### Conectar el proyecto con una base de datos

1. Instalar el complemento que requiera Python para enlazar con el gestor de base de datos,
en este caso de PostgreSQL se llama Psycopg:
    
1.1. Instalar el complemento con aptitude o apt-get
    `# apt-get install python-psycopg2`
    
1.2. Instalar el complemento con Pip
    `$ pip install psycopg2`

1. Crear una base de datos para el proyecto, en un gestor de base de datos, en este caso PostgreSQL:
    `postgres=# CREATE DATABASE nombredelproyecto`

2. Abrir el archivo `nombredelproyecto/settings.py`:
    `~/nombredelproyecto$ nano settings.py`

3. Allí hay que buscar la sección `DATABASES` y agregar y reemplazar los datos, por defecto son:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase',
    }
}
```
3.1. La línea 'ENGINE' define el gestor de base de datos con el que se enlazará:



```
DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
```

### Correr el servidor local

1. Correr el servidor local de Django
    `$ python manage.py runserver`
2. Desde el navegador web se entra al servidor local de Django en la dirección _127.0.0.0:8000_ o
_localhost:8000_
3.
