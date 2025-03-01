# -*- coding: utf-8 -*-
import sys
import os
import argparse

# Agregar el directorio raíz del proyecto al sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from markdown.base import MarkdownBase
from markdown.TOC import MarkdownTOCGenerator
from markdown.TOC_files import MarkdownTOCFiles
from markdown.TOC_html import MarkdownConverter

def set_default_value(value):
    if not value:
        value = None
    else:
        value = value[0]
    return value

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generar TOC para archivos Markdown.")

    parser.add_argument(
        "input_dir",
        type=str,
        help="Ruta del directorio de entrada."
    )
    parser.add_argument(
        "--output_dir",
        type=str,
        nargs='*',
        default=None,
        help="Genera copia de todos los ficheros a una ruta destino esplicitat y trabaja sobre este directorio"
    )
    parser.add_argument(
        "--toc",
        action="store_true",
        help="Generar TOC."
    )
    parser.add_argument(
        "--toc_files",
        action="store_true",
        help="Generar TOC por cada fichero marckdown que encuentra."
    )
    parser.add_argument(
        "--ignorar",
        nargs='*',
        default=[],
        help="Lista de directorios a ignorar (separados por espacios)."
    )
    parser.add_argument(
        "--toc_sort",
        action="store_true",
        help="Ordena los ficheros que contienen el regex apropiado."
    )
    parser.add_argument(
        "--html",
        type=str,
        nargs='*',
        default=None,
        help="Genera un fichero HTML indicando la ruta de salida. Si no se especifica se generará la misma que entrada, añadiendo el sufijo '_html' al final de la ruta de entrada."
    )
    parser.add_argument(
        "--copy",
        type=str,
        nargs='*',
        default=None,
        help="Genera copia de todos los ficheros a una ruta destino esplicitat."
    )

    args = parser.parse_args()

    # First set COPY actions
    make_copy = False
    copy = args.copy

    # Obtenemos los directorios raíz y destino
    input_dir = args.input_dir
    output_dir = args.output_dir

    # Obtenemos los parametros para las acciones a realizar
    toc = args.toc
    ignorar = args.ignorar
    toc_files = args.toc_files
    toc_sort = args.toc_sort
    html = args.html

    # Check if the output directory is not None
    if output_dir is not None:
        output_dir = set_default_value(output_dir)

    # Check if the copy param is not None
    if copy is not None:
        copy = set_default_value(copy)
        make_copy = MarkdownBase(input_dir, ruta_destino=copy, ignorar_directorios=ignorar)
        make_copy.set_ruta_destino(copy)
        make_copy.copy()

    # If make_copy is not defined or is falsy
    if not make_copy:
        # Create a new MarkdownCopy instance for other copy operation
        make_other_copy = MarkdownBase(input_dir, ruta_destino=output_dir, ignorar_directorios=ignorar)
        make_other_copy.set_ruta_destino(output_dir)
        make_other_copy.copy()
        input_dir = make_other_copy.get_ruta_destino()
    else:
        make_other_copy = MarkdownBase(input_dir, ruta_destino=output_dir, ignorar_directorios=ignorar)
        make_other_copy.set_ruta_destino(output_dir)
        # If the path from make_copy does not match output_dir, proceed
        if make_copy.get_ruta_destino() == make_other_copy.get_ruta_destino():
            input_dir = make_copy.get_ruta_destino()
        else:
            make_other_copy.copy()
            input_dir = make_other_copy.get_ruta_destino()

    # Generamos el TOC segun el tree del la ruta absoluta proporcionada siendo este un directorio
    if toc:
        generador = MarkdownTOCGenerator(input_dir, ignorar)
        generador.crear_readme_toc()

    # Si se quiere realizar un TOC en cada uno de los ficheros .md sobre el contenido interno de estos
    # TODO Recorrer rde forma recursiva en caso de no tener parametre --files
    if toc_files or toc_sort:
        updater = MarkdownTOCFiles(input_dir, toc_files=toc_files, toc_sort=toc_sort, ignorar_directorios=ignorar)
        updater.procesar_archivos_markdown(input_dir)
        print("Archivos Markdown procesados con éxito.")

    # Si se quiere crear archivos HTML a partir de los .md.
    # TODO tener en cuenta el estilo del HTML y del TOC a demás de modificar el slug para HTML.
    if html is not None:
        html = None if not html else html
        output_html_dir = input_dir + html
        html_converter = MarkdownConverter(input_dir, output_html_dir=output_html_dir)
        html_converter.process_directory_recursively_with_images()
