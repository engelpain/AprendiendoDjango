## Guía para crear un proyecto básico con Django
Centro Nacional de Desarrollo e Investigación de Tecnologías Libres (CENDITEL) <br>
[CENDITEL](https://www.cenditel.gob.ve/), Mérida - Venezuela<br>
Dirección de Desarrollo<br>
Autor: [Ing. Angelo Osorio](https://twitter.com/Engel_PAIN)<br>
Fecha de Elaboración: 24-01-2018 (dd,mm,aaaa)

### Notas del autor
El símbolo al principio de una línea de comandos indica:
    `$ = hacer la sentencia como usuario`
    `# = hacer la sentencia como administrador`

### Virtual Environments

* Instalar: 
    `# apt-get install python-virtualenv`

* Remover:
    `# apt-get remove python-virtualenv`

* Crear un entorno virtual
    `$ virtualenv nombredelentorno`

* Activar el entorno virtual
    `$ source nombredelentorno/bin/activate`

* Desactivar el entorno virtual
    `$ deactivate`

* Elegir la versión de python del entorno
    `$ virtualenv -p versióndepython nombreentorno` <br>
Ejemplo:
    `$ virtualenv -p python3.5 EntornoPythonTres`