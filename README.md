# Bienvenidos al repositorio oficial de Green Pack Services | Desarrollador: Sebastian Alejandro Araya Torres

Este proyecto inicio desde el año 2022:

# Instaladores

##### 1) Compilador

- [Python3](https://www.python.org/downloads/release/python-396/ "Python3")

##### 2) IDE

- [Visual Studio Code](https://code.visualstudio.com/ "Visual Studio Code")
- [Sublime Text](https://www.sublimetext.com/ "Sublime Text")
- [Pycharm](https://www.jetbrains.com/es-es/pycharm/download/#section=windows "Pycharm")

##### 3) Motor de base de datos

- [Sqlite Studio](https://github.com/pawelsalawa/sqlitestudio/releases "Sqlite Studio")
- [PostgreSQL](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads "PostgreSQL")
- [MySQL](https://www.apachefriends.org/es/index.html "MySQL")

##### 4) Repositorios

<!-- - [Git](https://git-scm.com/ "Git") -->

# Instalación

##### 1) Clonar o descargar el proyecto del repositorio

<!-- `git clone https://gitlab.com/wdavilav/apolo.git` -->

##### 2) Crear un entorno virtual para posteriormente instalar las librerias del proyecto

- `python3 -m venv venv` (Windows)

##### 3) Instalar el complemento de [weasyprint](https://weasyprint.org/ "weasyprint")

- Si estas usando Windows debe descargar el complemento de [GTK3 installer](https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases "GTK3 installer"). En algunas ocaciones se debe colocar en las variables de entorno como primera para que funcione y se debe reiniciar el computador.

##### 4) Activar el entorno virtual de nuestro proyecto

- `cd venv\Scripts\activate.bat` (Windows)

##### 5) Instalar todas las librerias del proyecto que se encuentran en la carpeta deploy

- `pip install -r deploy/requirements.txt`

##### 6) Crear la base de datos con las migraciones y el superuser para iniciar sesión

- `python manage.py makemigrations`
- `python manage.py migrate`

##### 7) Insertar información inicial en la base de datos

- `python manage.py shell --command='from core.utilities import *'`
------------


***Green Pack Serices | Crecimiento profesional como programador 🤓.***


