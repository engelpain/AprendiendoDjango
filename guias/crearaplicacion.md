# Guía de Intalación de Django 1.11.8 (LTS)
<p> Centro Nacional de Desarrollo e Investigación de Tecnologías Libres (CENDITEL)</p>
<p> <a href="https://www.cenditel.gob.ve/">CENDITEL</a>, Mérida - Venezuela </p>
<p> Dirección de Desarrollo </p>
<p> Autor: <a href="https://twitter.com/Engel_PAIN">Ing. Angelo Osorio</a> </p>
<p> Fecha de Elaboración: 26-12-2017 (dd,mm,aaaa)</p><br>

<h2> Crear una aplicación con Django </h2>

<ol>
  <li>
    <p> Construir el directorio del nuevo proyecto que se llamará <i>primerproyecto</i>, usando el comando: </p>
    <p> <code> $ django-admin.py startproject primerproyecto </code> </p>
    <p><strong> Django </strong> creará automáticamente los archivos que requiere para funcionar</p>
  </li>
  <li>
    <p> Entrar en el directorio que se creó:</p>
    <p> <code> $ cd primerproyecto </code> </p>
    <p> En él se encontrarán los archivos que crea <strong>Django</strong> para hacer funcionar la
      aplicación, en este caso, un archivo (<i>manage.py</i>) y un directorio homónimo al nombre del
      proyecto (<i>primerproyecto</i>), que contiene cuatro archivos: <i> __init__.py </i>,
      <i> settings.py </i>, <i> urls.py </i> y <i> wsgi.py </i>
    </p>
  </li>
  <li>
    <p> Crear una nueva aplicación, que se llamará <i>primerapp</i> usando el comando: </p>
    <p> <code> $ django-admin.py startapp primerapp </code> </p>
    <p> Esto creará un directorio (<i> primerapp </i>) que contendrá los archivos que se requieren
    para crear una aplicación con Django.
    </p>
  </li>
  <li>
    <p>Agregar la aplicación al proyecto</p>
    <ul>
      <li>
        <p> Para ello hay que modificar el archivo <i> settings.py </i> que está en el directorio
          del proyecto (<i>primerproyecto</i>).  Aquí hay que buscar la sección <b>INSTALLED_APPS</b>
          y agregar la nueva aplicación escribiendo <code>'primerapp',</code>
        </p>
        <p>Tal como se muestra en la siguiente imagen:</p>
        <p>
          <img src="img/imagen1.png" alt="Agregar aplicación">
        </p>
      </li>
    </ul>
  </li>
  <li>
    <p>Correr la aplicación</p>
    <ul>
      <li>
        <p> Se levanta el servidor de Django usando el comando: </p>
        <p>$ ./manage.py runserver </p>
      </li>
      <li>
        <p> Desde el navegador web se entra al servidor local de Django en la dirección <i>127.0.0.0:8000</i>
        que trae por defecto configurada</p>
        <p>
          <img src="img/imagen2.png" alt="Run server">
        </p>
      </li>
    </ul>
  </li>
</ol>

<p> Ya se tiene creado el esqueleto de una aplicación usando Django.</p>