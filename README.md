# Proyectos

##### Table of Contents

- [Proyectos](#proyectos)
        - [Table of Contents](#table-of-contents)
  - [Instalación](#instalación)
    - [Flet en Ambiente virtual (MacOS)](#flet-en-ambiente-virtual-macos)
    - [Crear proyecto en blanco](#crear-proyecto-en-blanco)
    - [Correr app web](#correr-app-web)
    - [Correr app Android](#correr-app-android)
    - [Correr app iOS](#correr-app-ios)

## Instalación

### Flet en Ambiente virtual (MacOS)


````shell
python3 -m venv venv
source venv/bin/activate
pip install flet
````

### Crear proyecto en blanco

````python
flet create --project-name NombreApp --description "Descripcion" --template minimal ./Carpeta

````

````
usage: flet create [-h] [-v] [--project-name PROJECT_NAME] [--description DESCRIPTION] [--template {minimal,counter}] output_directory

Create a new Flet app from a template.

positional arguments:
  output_directory      project output directory

options:
  -h, --help            show this help message and exit
  -v, --verbose         -v for detailed output and -vv for more detailed
  --project-name PROJECT_NAME
                        project name for the new Flet app
  --description DESCRIPTION
                        the description to use for the new Flet project
  --template {minimal,counter}
                        template to use for new Flet project
````

### Correr app web

````shell
flet run Carpeta --web --port 8550 --name APP_NAME
````

### Correr app Android

````shell
flet run Carpeta --android --name APP_NAME
````

### Correr app iOS

````shell
flet run Carpeta --ios
````

# Grupo Solana


