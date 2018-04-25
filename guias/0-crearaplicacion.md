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
   /$ = indica que está en la raíz del proyecto desde la consola
   /directorio$ = indica que está en un directorio del proyecto desde la consola
   / = En una url significará en la raíz del proyecto
```
> Nota Importante: Django utiliza 4 espacios de identación, es importante que en todos los archivos
siga esta directiva, en caso de omitirla puede que el proyecto de errores.

> Nota Importante 2: Django no admite utilizar ñ o letras acentuadas antes de la versión 1.11.3,
incluso en comentarios del código. Se debe tomar en consideración ésto a la hora de realizar otros
tutoriales con el Framework. Para poder comentar y utilizar esas letras se debe comentar en el
inicio del código: `# -*- coding: utf-8 -*-`

> La versión de Django utilizada para esta guía es Django 1.11.3.

### Pasos para crear un proyecto
1. [Construir un nuevo proyecto en Django](1-construir-proyecto.md)
2. [Conectar el proyecto con una base de datos](2-conectar-django.md)
3. [Correr el servidor local por primera vez](3-localhost.md)
4. [Crear una aplicación](4-crear-aplicacion.md)
5. [Crear modelos del app](5-crear-modelos.md)
6. [Listar posts del modelo](6-listar-posts.md)
7. [Agregar posts en la base de datos](7-ingresar-posts.md)
8. [Modificar posts en la base de datos](8-actualizar-posts.md)

Para crear este proyecto se siguío [este ejemplo](https://www.groloop.com/django-1-11-3-crear-crud/).