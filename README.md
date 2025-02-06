# TOC MARKDOWN

```python
python3 md_toc.py
```

## md_toc.py

Desde una ruta entrada por el usuario.

El programa creará un índice en formato markdown en un fichero `README.md`.

Este se genera recorriendo en formato `tree` los ficheros de la ruta introducida.

Este seguira las siguientes ordenes:

* Ordenar de forma alfabética los directorios raíz
* Igonrar los archivos ocultos y un listado de directorios y ficheros insertados por el usuario.
* Enumerara em formato `TOC` de markdown cada índice y subíndice que se vaya encontrando.
* Escrivirá los nombre de los directorios raíz en mayúsculas. Los demás en `capitalizae`.
* Formateará los archivos:
  * Remobiendo su extención.
  * Reemplazando '_' por '-'.
* Generará el enlace hacia el directorio/fichero.

Requisitos:
Generar un listado de directorios y subdirectorios con sus archivos.
Los elementos deben estar enumerados en el formato de un TOC de markdown.
Ordenar alfabéticamente los archivos y directorios raíz.
Ignorar archivos ocultos y un listado predefinido.
El archivo generado debe llamarse README.md.

## md_toc_in_files.py

Por cada fichero markdown que encuentre:

* Creará un tag de inició y fin de TOC.
  * Dentro de este generarà el TOC del fichero
  * Añadirá el enlace al tag interno del fichero


## APP

* Install
```bash
pip install Flask
```

```bash
cd app
python app.py 
```
