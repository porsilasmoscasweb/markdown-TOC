# -*- coding: utf-8 -*-
import sys
import os
import argparse

# Agregar el directorio raíz del proyecto al sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from classes.TOC import MarkdownTOCGenerator
from classes.TOC_files import MarkdownTOCUpdater
from classes.TOC_sort import MarkdownOrdenador
from classes.TOC_html import MarkdownConverter

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generar TOC para archivos Markdown.")
    parser.add_argument(
        "ruta_directorio",
        type=str,
        help="Ruta del directorio base"
    )
    parser.add_argument(
        "--ignorar",
        nargs='*',
        default=[],
        help="Lista de directorios a ignorar (separados por espacios)"
    )
    parser.add_argument(
        "--files",
        action="store_true",
        help="Crear un TOC por cada fichero marckdown que encuentra"
    )
    parser.add_argument(
        "--sort",
        action="store_true",
        help="Ordena los ficheros que contienen el regex apropiado"
    )
    parser.add_argument(
        "--html",
        type=str,
        default="_html",
        help="Genera un fichero HTML indicando ls ruta de salida. Si no se especifica se generará la misma que entrada, añadiendo '_html' al final del path"
    )

    args = parser.parse_args()

    ruta_directorio = args.ruta_directorio
    ignorar = args.ignorar
    sort = args.sort
    html = args.html

    # Generamos el TOC segun el tree de la ruta proporcionada
    generador = MarkdownTOCGenerator(ruta_directorio, ignorar)
    generador.crear_readme_toc()

    # Si se quiere realizar un TOC por cada uno de los ficheros .md
    if args.files:
        updater = MarkdownTOCUpdater(ruta_directorio, ignorar, sort)
        updater.procesar_archivos_markdown(ruta_directorio)
        print("Archivos Markdown procesados con éxito.")

    # Si se quiere realizar un TOC por cada uno de los ficheros .md
    if html:
        if html == '_html':
            html = ruta_directorio + html
        html_converter = MarkdownConverter(ruta_directorio, html)
        html_converter.process_directory_recursively_with_images()
