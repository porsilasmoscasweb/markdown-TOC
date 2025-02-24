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


## md_toc_in_files_sort.py

Por cada fichero markdown que encuentre con la cabecera `[//]: <> (order:asc)` este será ordenado de la forma indicada.

Importaremos TOC_sort.py y su Classe `MarkdownOrdenador`, que será la encargada de ordenar el fichero y crear el TOC del mismo.

Basicamente es lo mismo que el fichero anterior, pero le añadimos la nueva funcionalidad
 
## md_toc_in_files_orderBy.py [IN PROCESS]

Por cada fichero markdown que encuentre con la cabecera `[//]: <> (order:asc)` este será ordenado de la forma indicada


## APP

* Install
```bash
pip install Flask
```

```bash
cd app
python app.py 
```
