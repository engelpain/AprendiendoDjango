# Guía para conectar Python con PostgreSQL
Centro Nacional de Desarrollo e Investigación de Tecnologías Libres (CENDITEL)
[CENDITEL](https://www.cenditel.gob.ve/), Mérida - Venezuela
Dirección de Desarrollo
Autor: [Ing. Angelo Osorio](https://twitter.com/Engel_PAIN)
Fecha de Elaboración: 27-12-2017 (dd,mm,aaaa)



## Conectar con PostgreSQL








2. Abrir el fichero de configuración del proyecto proyecto/proyecto/settings.py con un editor de
texto como sublime text, vim, nano, etc...

3. Buscar el apartado:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

Por defecto trae sqlite3, hay que cambiarlo a PostgreSQL escribiendo:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase',
        'USER': 'mydatabaseuser',
        'PASSWORD': 'mypassword',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

Nota: para versiones anteriores a Django 1.9 el ENGINE cambia ligeramente a:

        'ENGINE': 'django.db.backends.postgresql_psycopg2',

Ésta directiva también es aceptada en versiones más recientes de Django.


// ------------------------------- Conectar con PostgreSQL [ENDED] ------------------------------ //



// --------------------- Importar las migraciones a la base de datos [BEGIN] -------------------- //

Una vez conectado Django con PostgreSQL, la creación de las tablas requeridas por Django se hacen
con la directiva:
  $ ./manage.py migrate

// --------------------- Importar las migraciones a la base de datos [ENDED] -------------------- //