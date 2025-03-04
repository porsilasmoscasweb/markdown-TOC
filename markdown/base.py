# -*- coding: utf-8 -*-
import os
import re
import shutil


class MarkdownBase:
    def __init__(self, ruta_base, ruta_destino=None, ignorar_directorios=None):
        """
        Inicializa la clase con el directorio base y la lista de directorios a ignorar.

        :param ruta_base: Ruta base del directorio.
        :param ignorar_directorios: Lista de directorios a ignorar (opcional).
        """
        self.ruta_base = ruta_base

        # Ignorar
        self.ignorar = ['README.md', '.DS_Store', '.gitignore', '.idea', 'books', 'exercices', 'footage', 'tools',
                        'planning', '*.log']
        if ignorar_directorios is None:
            ignorar_directorios = []
        self.ignorar += ignorar_directorios

        # Ruta destino y crear directorio destino si es diferente de ruta_base
        if ruta_destino and ruta_destino != ruta_base:
            self.ruta_destino = ruta_destino
            self.copy()
        else:
            self.ruta_destino = ruta_base

        # Patrones
        self.patrones_bloques = [
            r'```.*?```',
            r"'''.*?'''",
            r'""".*?"""',
            r"'[^']*'",
            r'"[^"]*"',
            r'<!--.*?-->'
        ]
        self.bloques_ignorados = []

        print(f"Ruta base: {self.ruta_base}")
        print(f"Ruta destino: {self.ruta_destino}")
        print(f"Ignoramos: {self.ignorar}")

    def es_archivo_ignorado(self, nombre):
        """Función para ignorar archivos ocultos o que están en la lista de ignorados."""
        return nombre.startswith('.') or nombre in self.ignorar

    def leer_markdown(self, nombre_archivo):
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            return archivo.read()

    def guardar_markdown(self, nombre_archivo, contenido):
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
            archivo.write(contenido)

    def get_sort(self, contenido):
        orden = False
        primera_linea = contenido.readline().strip()
        nuevo_contenido = contenido.read().lstrip()

        # Detectar si el archivo contiene la directiva de orden
        match = re.match(r'\[\/\/\]:\s*<>\s*\(order:(asc|desc)\)', primera_linea)
        if match:
            orden = match.group(1)

        return orden, primera_linea, nuevo_contenido

    def copy(self):
        if not os.path.isdir(self.ruta_base):
            os.makedirs(os.path.dirname(self.ruta_destino), exist_ok=True)
            return

        if not os.path.exists(self.ruta_base):
            shutil.copytree(self.ruta_base, self.ruta_destino, ignore=shutil.ignore_patterns(*self.ignorar))
        else:
            for item in os.listdir(self.ruta_base):
                origen_item = os.path.join(self.ruta_base, item)
                destino_item = os.path.join(self.ruta_destino, item)

                if os.path.isdir(origen_item):
                    if item in self.ignorar:
                        print(f"[Ignorado]: {item}")
                        continue  # Ignorar directorio
                    shutil.copytree(origen_item, destino_item, dirs_exist_ok=True,
                                    ignore=shutil.ignore_patterns(*self.ignorar))
                else:
                    if any(shutil.fnmatch.fnmatch(item, pattern) for pattern in self.ignorar):
                        continue  # Ignorar archivo

                    # Ensure destination folder exists
                    os.makedirs(os.path.dirname(destino_item), exist_ok=True)
                    shutil.copy2(origen_item, destino_item)

    def ordenar(self, markdown, ascendente=True):
        bloques_pattern = re.compile('|'.join(self.patrones_bloques), re.DOTALL)

        def reemplazar_bloque(match):
            self.bloques_ignorados.append(match.group(0))
            return f"__BLOQUE_IGNORADO_{len(self.bloques_ignorados) - 1}__"

        markdown_sin_bloques = bloques_pattern.sub(reemplazar_bloque, markdown)

        pattern = re.compile(r'^(#+\s+.*?)(?=\n#+\s+|\Z)', re.MULTILINE | re.DOTALL)
        secciones = []

        for match in pattern.finditer(markdown_sin_bloques):
            encabezado_bloque = match.group(1).strip()
            nivel = len(re.match(r'^(#+)', encabezado_bloque).group(1))
            secciones.append({
                'nivel': nivel,
                'texto': encabezado_bloque,
                'hijos': []
            })

        estructura = []
        pila = []

        for seccion in secciones:
            while pila and pila[-1]['nivel'] >= seccion['nivel']:
                pila.pop()

            if pila:
                pila[-1]['hijos'].append(seccion)
            else:
                estructura.append(seccion)

            pila.append(seccion)

        # Ordenar según el parámetro ascendente o descendente
        def ordenar_nodos(nodos):
            nodos.sort(key=lambda x: x['texto'].lower(), reverse=not ascendente)
            for nodo in nodos:
                ordenar_nodos(nodo['hijos'])

        ordenar_nodos(estructura)

        def reconstruir_markdown(nodos):
            resultado = []
            for nodo in nodos:
                resultado.append(nodo['texto'])
                resultado.extend(reconstruir_markdown(nodo['hijos']))
            return resultado

        markdown_ordenado = '\n\n'.join(reconstruir_markdown(estructura))

        def restaurar_bloques(texto):
            for i, bloque in enumerate(self.bloques_ignorados):
                texto = texto.replace(f"__BLOQUE_IGNORADO_{i}__", bloque)
            return texto

        return restaurar_bloques(markdown_ordenado)
