# -*- coding: utf-8 -*-
import os
import re
import shutil

class MarkdownCopy:
    def __init__(self, ruta_base, ruta_destino=None, ignorar_directorios=None):
        """
        Inicializa la clase con el directorio base y la lista de directorios a ignorar.

        :param ruta_base: Ruta base del directorio.
        :param ignorar_directorios: Lista de directorios a ignorar (opcional).
        """
        if ignorar_directorios is None:
            ignorar_directorios = []
        if ruta_destino is None:
            ruta_destino = ruta_base + "_copy"
        self.ruta_base = ruta_base
        self.ruta_destino = ruta_destino
        self.ignorar = ['README.md', '.DS_Store', '.gitignore', '.idea', '*.log']
        self.ignorar += ignorar_directorios

    def get_path(self):
        return self.ruta_destino

    def copy(self):
        if not os.path.exists(self.ruta_base):
            shutil.copytree(self.ruta_base, self.ruta_destino, ignore=shutil.ignore_patterns(*self.ignorar))
        else:
            for item in os.listdir(self.ruta_base):
                origen_item = os.path.join(self.ruta_base, item)
                destino_item = os.path.join(self.ruta_destino, item)

                if os.path.isdir(origen_item):
                    if item in self.ignorar:
                        continue  # Ignorar directorio
                    shutil.copytree(origen_item, destino_item, dirs_exist_ok=True,
                                    ignore=shutil.ignore_patterns(*self.ignorar))
                else:
                    if any(shutil.fnmatch.fnmatch(item, pattern) for pattern in self.ignorar):
                        continue  # Ignorar archivo

                    # Ensure destination folder exists
                    os.makedirs(os.path.dirname(destino_item), exist_ok=True)
                    shutil.copy2(origen_item, destino_item)
