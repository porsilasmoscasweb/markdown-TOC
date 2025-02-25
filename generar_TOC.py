# -*- coding: utf-8 -*-
import sys
import os
import argparse

# Agregar el directorio raíz del proyecto al sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from classes.TOC import MarkdownTOCGenerator
from classes.TOC_files import MarkdownTOCUpdater
from classes.TOC_sort import MarkdownOrdenador

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
        nargs='*',
        default=False,
        help="Crear un TOC por cada fichero marckdown que encuentra"
    )
    parser.add_argument(
        "--sort",
        nargs='*',
        default=False,
        help="Ordena los ficheros que contienen el regex apropiado"
    )
    parser.add_argument(
        "--html",
        nargs='*',
        default=False,
        help="Genera un fichero HTML"
    )

    args = parser.parse_args()

    ruta_directorio = args.ruta_directorio
    ignorar = args.ignorar
    sort = args.sort
    html = args.html

    generador = MarkdownTOCGenerator(ruta_directorio, ignorar)
    generador.crear_readme_toc()

    if args.files:
        updater = MarkdownTOCUpdater(ruta_directorio, ignorar, sort)
        updater.procesar_archivos_markdown(ruta_directorio)
        print("Archivos Markdown procesados con éxito.")
