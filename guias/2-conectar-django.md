### Conectar el proyecto con una base de datos
Django es capáz de conectar con una cantidad amplia de base de datos. En este tutorial se explica
cómo conectarlo tres de las más usadas: MySQL, PostgreSQL y SQLite.


#### SQLite + Django
Django (al momento de inicializar un proyecto) trae una conexión por defecto con SQLite3.
Se puede verificar esto en `/nombreProyecto/settings.py` en el apartado `# Database`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```
El diccionario `'default'` contiene 2 elementos:
* `'ENGINE': 'django.db.backends.sqlite3'`: Que determina que se conectará con una base de datos
SQLite3.
* `'NAME': os.path.join(BASE_DIR, 'db.sqlite3')`: Indíca dónde está alojada la base de datos y cómo
se llama, en este particular caso se creará la base de datos en caso de no existir en la raíz del
proyecto con el nombre de db.sqlite3


#### PostgreSQL + Django
1. Para conectar Django con PostgreSQL primero se debe instalar el plugin Psycopg2.
   * Instalar el complemento con apt-get: `apt-get install python-psycopg2`
   * Instalar el complemento con pip: `pip install psycopg2`
2. Crear una base de datos en PostgreSQL
   * `postgres=# CREATE DATABASE nombredelproyecto`
3. Abrir el archivo `/nombreProyecto/settings.py`
4. Cambiar la conexión en el apartado `# Database`:
   * `'ENGINE': 'django.db.backends.postgresql_psycopg2',`
   * `'NAME': 'nombrebasededatos',`
   * `'USER': 'usuario',`
   * `'PASSWORD': 'clave',`
   * `'HOST': 'localhost',`
   * `'PORT': '5432',`
5. Resultado final:
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


#### MySQL + Django
1. Para conectar Django con MySQL primero se debe instalar el plugin python-mysqldb.
   * Instalar el complemento con apt-get: `apt-get install python-mysqldb`
2. Crear una base de datos en MySQL
   * `> CREATE DATABASE nombredelproyecto;`
3. Abrir el archivo `/nombreProyecto/settings.py`
4. Cambiar la conexión en el apartado `# Database`:
   * `'ENGINE': 'django.db.backends.mysql',`
   * `'NAME': 'nombrebasededatos',`
   * `'USER': 'usuario',`
   * `'PASSWORD': 'clave',`
   * `'HOST': 'localhost',`
   * `'PORT': '3306',`
5. Resultado final:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'nombrebasededatos',
        'USER': 'usuario',
        'PASSWORD': 'clave',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

#### Migrar los modelos a la base de datos
Luego de realizar la configuración hay que migrar los modelos para comprobar que se realizó la
conexión con éxito:
* `/$ python manage.py migrate`

[Documentación oficial](https://docs.djangoproject.com/en/1.11/ref/settings/#databases)
