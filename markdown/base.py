# -*- coding: utf-8 -*-
import os
import shutil


class MarkdownBase:
    def __init__(self, ruta_base, ruta_destino=None, ignorar_directorios=None):
        """
        Inicializa la clase con el directorio base y la lista de directorios a ignorar.

        :param ruta_base: Ruta base del directorio.
        :param ignorar_directorios: Lista de directorios a ignorar (opcional).
        """
        if ignorar_directorios is None:
            ignorar_directorios = []
        if ruta_destino is None:
            ruta_destino = ruta_base
        self.ruta_base = ruta_base
        self.ruta_destino = ruta_destino
        self.ignorar = ['README.md', '.DS_Store', '.gitignore', '.idea', 'books', 'exercices', 'footage', 'tools', 'planning', '*.log']
        self.ignorar += ignorar_directorios
        self.patrones_bloques = [
            r'```.*?```',
            r"'''.*?'''",
            r'""".*?"""',
            r"'[^']*'",
            r'"[^"]*"',
            r'<!--.*?-->'
        ]
        self.bloques_ignorados = []

    def es_archivo_ignorado(self, nombre):
        """Función para ignorar archivos ocultos o que están en la lista de ignorados."""
        return nombre.startswith('.') or nombre in self.ignorar

    def set_ruta_destino(self, ruta_destino=None):
        if ruta_destino is None:
            self.ruta_destino = self.ruta_base + '_copy'
        else:
            self.ruta_destino = ruta_destino

    def get_ruta_base(self):
        return self.ruta_base

    def get_ruta_destino(self):
        return self.ruta_destino

    def leer_markdown(self, nombre_archivo):
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            return archivo.read()

    def guardar_markdown(self, nombre_archivo, contenido):
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
            archivo.write(contenido)

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
                    print(f"{origen_item}: {destino_item}")
                    shutil.copy2(origen_item, destino_item)