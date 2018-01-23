## Guía de Instalación de Django 1.11.9 (LTS)
Centro Nacional de Desarrollo e Investigación de Tecnologías Libres (CENDITEL) <br>
[CENDITEL](https://www.cenditel.gob.ve/), Mérida - Venezuela<br>
Dirección de Desarrollo<br>
Autor: [Ing. Angelo Osorio](https://twitter.com/Engel_PAIN)<br>
Fecha de Elaboración: 26-12-2017 (dd,mm,aaaa)


### Notas del autor
El símbolo al principio de una línea de comandos indica:

    $ = hacer la sentencia como usuario
    # = hacer la sentencia como administrador


### Requisitos de Instalación
Esta guía está realizada usando como sistema Anfitrión **Debian 9.3 Stretch**, sistema que trae por
defecto instalado **Python 2.7**.

La versión de Django utilizada para aprender en este tutorial es la **1.11.9 LTS** la última
soportada por **Python 2.7**


### Pip
Pip es un sistema de gestión de paquetes utilizado para instalar y administrar paquetes de software
escritos en Python

#### Gestionar Pip:

Instalar Pip:

    # apt-get install python-pip

Desinstalar Pip:

    # apt-get remove python-pip

#### Acciones con Pip:

Buscar un paquete

    $ pip search nombredelpaquete

Instalar un paquete usando Pip

    $ pip install nombredelpaquete

Instalar un paquete en una versión específica usando Pip

    $ pip install nombredelpaquete==version

Remover un paquete

    $ pip unistall nombredelpaquete

Listar los paquetes instalados:

    $ pip freeze

Obtener información detallada de un paquete:

    $ pip show nombredelpaquete

Verificar que estén instaladas las dependencias de un paquete:

    $ pip check nombredelpaquete

Ayuda

    $ pip help

#### Apuntar a un mirror pip:
 Para utilizar un mirror de Python en específico se modifica el archivo pip.conf
    $ nano ~/.pip/pip.conf
> Nota: En caso que el directorio .pip no exista, se debe crear, en caso que de que el archivo no
exista, se debe crear el archivo.

Dentro del archivo escribir la dirección del mirror, por ejemplo:

    [global]
    index-url = http://pypi.cenditel/simple/

Luego de guardar el archivo, se utiliza como mirror principal. En caso de ser un mirror no firmado
como confiable se utiliza la directiva --trusted-host nombremirror para que acceda, ejemplo:

    $ pip install package_name --trusted-host pypi.cenditel


### Instalando Django desde su comprimido
1. Descargar la versión 1.11.9 (LTS) de Django desde su [página oficial](https://www.djangoproject.com/download/1.11.9/tarball/)

2. Descomprimir el archivo:

    $ tar xzvf Django-1.11.9.tar.gz

3. Entrar en el directorio que se creó al descomprimir:
    
    $ cd Django-1.11.9

4. Ejecutar el instalador de Django:

    # python setup.py install

5. ¡Listo! ya se tiene instalado Django en el equipo


### Instalando Django desde pip

>Nota importante: Python y Django (por lo general) van de la mano con entornos virtuales, por ello
los permisos para instalar paquetes usando pip varían, desde la máquina anfitrión se requieren
permisos de superusuario, sin embargo para instalar desde un entorno virtual no.

* Instalar la versión más reciente de Django:

    $ pip install django

* Para solicitar la instalación de una versión en específico de Django, basta con agregar ==version
al final de la sentencia anterior. Por ejemplo, para instalar la versión 2.0:

    $ pip install Django==2.0

* Desinstalar Django:

    $ pip uninstall django