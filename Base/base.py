# -*- coding: utf-8 -*-
import os
import re


class MarkdownBase:
    def __init__(self, ruta_base, ignorar_directorios=None):
        """
        Inicializa la clase con el directorio base y la lista de directorios a ignorar.

        :param ruta_base: Ruta base del directorio.
        :param ignorar_directorios: Lista de directorios a ignorar (opcional).
        """
        if ignorar_directorios is None:
            ignorar_directorios = []
        self.ruta_base = ruta_base
        # self.ignorar = ['README.md', '.DS_Store', '.gitignore', '.idea', 'books', 'exercices', 'footage', 'tools', 'planning', '*.log']
        self.ignorar = ['README.md', '.DS_Store', '.gitignore', '.idea', 'books', 'exercices', 'footage', 'tools', '*.log']
        self.ignorar += ignorar_directorios

    def es_archivo_ignorado(self, nombre):
        """Función para ignorar archivos ocultos o que están en la lista de ignorados."""
        return nombre.startswith('.') or nombre in self.ignorar
