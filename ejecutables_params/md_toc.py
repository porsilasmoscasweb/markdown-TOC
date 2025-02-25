# -*- coding: utf-8 -*-
import sys
import os

# Agregar el directorio raíz del proyecto al sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from classes.TOC import MarkdownTOCGenerator
import argparse

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

    args = parser.parse_args()

    generador = MarkdownTOCGenerator(args.ruta_directorio, args.ignorar)
    generador.crear_readme_toc()
