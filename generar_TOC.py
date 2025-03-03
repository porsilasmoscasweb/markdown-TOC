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

def set_default_value(value, ruta_base, default=''):
    if value is not None:
        value = value[0] if value else ruta_base + default
    return value

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generar TOC para archivos Markdown.")

    # Args obligatorio :str
    parser.add_argument(
        "input_dir",
        type=str,
        help="Ruta del directorio de entrada."
    )

    # Args opcional :boolean
    parser.add_argument(
        "-tf",
        "--toc_files",
        action="store_true",
        help="Generar TOC por cada fichero markdown que encuentra dentro de la ruta de entrada."
    )
    parser.add_argument(
        "-ts",
        "--toc_sort",
        action="store_true",
        help="Ordena los ficheros '.md' con cabecera '...(order:asc|desc)...'."
    )

    # Args opcions :list
    parser.add_argument(
        "-i",
        "--ignorar",
        nargs='*',
        default=[],
        help="Lista de directorios (Sin ruta absoluta) a ignorar (separados por espacios)."
    )

    # Args opcional :(None/list).
    # Estos argumentos pueden:
    #   No ester definidos.
    #   Declararse vacios: en cual caso se le assignará un valor por defecto a posteriori.
    #   Declararse con un valor: Este vendra en formato lista, en ese caso solo usaremos el primer elemento.
    parser.add_argument(
        "-t",
        "--toc",
        type=str,
        nargs='*',
        default=None,
        help="Generar TOC del directorio de entrada."
             "Si le pasamos una ruta. Genera una copia de todos los ficheros y trabaja sobre este directorio.\n"
             "No copiará los directorios archivos ignorados."
    )
    parser.add_argument(
        "--html",
        type=str,
        nargs='*',
        default=None,
        help="Genera una copia de todos los ficheros a la ruta destino especificada o por defector '_html' y trabaja sobre este directorio.\n"
             "Convierte los archivos .md en ficheros HTML indicando."
    )
    parser.add_argument(
        "-c",
        "--copy",
        type=str,
        nargs='*',
        default=None,
        help="Genera una copia de todos los ficheros a la ruta destino especificada o por defector '_copy'.\n"
             "No copiará los directorios archivos ignorados."
    )

    args = parser.parse_args()

    # Obtenemos los directorios raíz [OBLIGATORIO]
    input_dir = args.input_dir

    # Set los posibles argumentos que pueden no estar, estar vacios o llegar con un parametro (List) obteniendo su primer valor
    copy = set_default_value(args.copy, input_dir, '_copy')
    toc = set_default_value(args.toc, input_dir)
    html = set_default_value(args.html, input_dir, '_html')

    # Obtenemos los parametros para las acciones a realizar. Campos boleanos
    ignorar = args.ignorar # Directorios o archivos a ignorar
    toc_files = args.toc_files # Genera el TOC en cada archivo .md
    toc_sort = args.toc_sort # Ordena el contenido del los archivos .md con cabecera `...(order:asc|desc)...`

    # Check if the copy param is not None
    if copy:
        make_copy = MarkdownBase(input_dir, ruta_destino=copy, ignorar_directorios=ignorar)
        make_copy.copy()

    # If make_copy is not defined or is falsy
    # if not make_copy:
    #     # Create a new MarkdownCopy instance for other copy operation
    #     make_other_copy = MarkdownBase(input_dir, ruta_destino=output_dir, ignorar_directorios=ignorar)
    #     make_other_copy.set_ruta_destino(output_dir)
    #     make_other_copy.copy()
    #     input_dir = make_other_copy.get_ruta_destino()
    # else:
    #     make_other_copy = MarkdownBase(input_dir, ruta_destino=output_dir, ignorar_directorios=ignorar)
    #     make_other_copy.set_ruta_destino(output_dir)
    #     # If the path from make_copy does not match output_dir, proceed
    #     if make_copy.get_ruta_destino() == make_other_copy.get_ruta_destino():
    #         input_dir = make_copy.get_ruta_destino()
    #     else:
    #         make_other_copy.copy()
    #         input_dir = make_other_copy.get_ruta_destino()

    # Generamos el TOC segun el tree del la ruta absoluta proporcionada siendo este un directorio
    if toc:
        generador = MarkdownTOCGenerator(input_dir, toc, ignorar)
        generador.crear_readme_toc()
    #
    # # Si se quiere realizar un TOC en cada uno de los ficheros .md sobre el contenido interno de estos
    # # TODO Recorrer rde forma recursiva en caso de no tener parametre --files
    # if toc_files or toc_sort:
    #     updater = MarkdownTOCFiles(input_dir, toc_files=toc_files, toc_sort=toc_sort, ignorar_directorios=ignorar)
    #     updater.procesar_archivos_markdown(input_dir)
    #     print("Archivos Markdown procesados con éxito.")
    #
    # # Si se quiere crear archivos HTML a partir de los .md.
    # # TODO tener en cuenta el estilo del HTML y del TOC a demás de modificar el slug para HTML.
    # if html is not None:
    #     html = None if not html else html
    #     output_html_dir = input_dir + html
    #     html_converter = MarkdownConverter(input_dir, output_html_dir=output_html_dir)
    #     html_converter.process_directory_recursively_with_images()
