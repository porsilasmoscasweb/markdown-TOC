# -*- coding: utf-8 -*-
import os
import re
from md.base import MarkdownBase

class MarkdownTOCFiles(MarkdownBase):
    def __init__(self,
                 ruta_base,
                 ruta_destino=None,
                 toc_files=False,
                 rm_toc_files=False,
                 toc_sort=False,
                 ignorar_directorios=None):
        """
        Inicializa la clase con el directorio base y la lista de directorios a ignorar.
        Definir inició i fin del bloque TOC dentro de ficheros

        :param ruta_base: Ruta base del directorio.
        :param ignorar_directorios: Lista de directorios a ignorar (opcional).
        """
        super().__init__(ruta_base,
                         ruta_destino=ruta_destino,
                         ignorar_directorios=ignorar_directorios)

        self.toc_files = toc_files
        self.rm_toc_files = rm_toc_files
        self.toc_sort = toc_sort
        self.TOC_INICIO = "<!-- TOC INICIO -->"
        self.TOC_FIN = "<!-- TOC FIN -->"

    def es_archivo_ignorado(self, nombre):
        return super().es_archivo_ignorado(nombre)

    def es_parte_de_ruta_ignorada(self, nombre):
        """Función para ignorar directorios que están en la lista de ignorados."""
        ignorar = [s for s in self.ignorar if s in nombre]
        return ignorar

    def generar_slug(self, heading):
        """
        Convierte un encabezado en una ancla de markdown compatible.
        Reemplaza espacios por guiones, elimina caracteres especiales y convierte a minúsculas.
        """
        slug = heading.strip().lower()
        slug = re.sub(r'[^\w\s-]', '', slug)  # Eliminar caracteres especiales
        slug = slug.replace(' ', '-')  # Reemplazar espacios por guiones
        return slug

    def generar_toc_para_archivo(self, ruta_archivo):
        """
        Genera el TOC basado en los encabezados dentro de un archivo Markdown,
        ignorando aquellos que estén dentro de bloques de código.

        Args:
            ruta_archivo (str): Ruta del archivo Markdown.

        Returns:
            str: TOC en formato markdown.
        """
        toc = []
        dentro_bloque_codigo = False  # Estado para saber si estamos dentro de un bloque de código

        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                # Detectar inicio o fin de un bloque de código con ```
                if linea.strip().startswith("```"):
                    dentro_bloque_codigo = not dentro_bloque_codigo
                    continue  # Ignorar la línea que contiene ``` ya que no es un encabezado

                if dentro_bloque_codigo:
                    continue  # Ignorar cualquier línea dentro de un bloque de código

                # Buscar líneas que comiencen con uno o más `#` para detectar encabezados
                if linea.startswith('#'):
                    nivel = linea.count('#')  # El nivel se define por el número de `#`
                    encabezado_texto = linea.strip('#').strip()
                    slug = self.generar_slug(encabezado_texto)  # Generar el ancla
                    toc.append(f"{'  ' * (nivel - 1)}- [{encabezado_texto}](#{slug})")  # Crear la línea del TOC

        return "\n".join(toc)

    def actualizar_toc_en_archivo_markdown(self,
                                           ruta_archivo,
                                           toc):
        """
        Actualiza el TOC en un archivo Markdown, añadiéndolo o sustituyéndolo
        entre los delimitadores TOC_INICIO y TOC_FIN.

        Args:
            ruta_archivo (str): Ruta del archivo Markdown.
            toc (str): Contenido del TOC generado.
        """
        nuevo_contenido = ""
        contenido = self.leer_markdown(ruta_archivo)

        # Detectar si el archivo contiene la directiva de orden
        match = re.match(r'\[\/\/\]:\s*<>\s*\(order:(asc|desc)\)', contenido)
        if match:
            nuevo_contenido = match.group() + "\n\n"
            contenido = contenido.split(match.group())[1]

        if self.TOC_INICIO in contenido and self.TOC_FIN in contenido:
            # Reemplazar TOC existente
            nuevo_contenido += contenido.split(self.TOC_INICIO)[0].strip() + self.TOC_INICIO + "\n" + toc + "\n" + self.TOC_FIN + \
                              "\n\n" + contenido.split(self.TOC_FIN)[1].strip()
        else:
            # Añadir TOC al principio
            nuevo_contenido += self.TOC_INICIO + "\n" + toc + "\n" + self.TOC_FIN + contenido

        self.guardar_markdown(ruta_archivo, nuevo_contenido)

    def eliminar_toc_en_archivo_markdown(self, ruta_archivo):
        """
        Eliminar el TOC en un archivo Markdown.

        Args:
            ruta_archivo (str): Ruta del archivo Markdown.
        """
        nuevo_contenido = ""
        contenido = self.leer_markdown(ruta_archivo)

        # Detectar si el archivo contiene la directiva de orden
        match = re.match(r'\[\/\/\]:\s*<>\s*\(order:(asc|desc)\)', contenido)
        if match:
            nuevo_contenido = match.group() + "\n\n"
            contenido = contenido.split(match.group())[1]

        if self.TOC_INICIO in contenido and self.TOC_FIN in contenido:
            # Reemplazar TOC existente
            nuevo_contenido += contenido.split(self.TOC_INICIO)[0].strip() + contenido.split(self.TOC_FIN)[1].strip()
            self.guardar_markdown(ruta_archivo, nuevo_contenido)

    def procesar_archivos_markdown(self, ruta_destino=None):
        """
        Procesa todos los archivos Markdown en el directorio, añadiendo o
        sustituyendo el TOC en cada uno de ellos.

        Args:
            ruta_destino (str): Ruta ruta_destino del directorio o archivo Markdown.
        """
        if ruta_destino is None:
            ruta_destino = self.ruta_destino

        if os.path.isfile(ruta_destino) and ruta_destino.endswith('.md'):
            # Si es un archivo Markdown, procesar solo ese archivo
            if self.rm_toc_files:
                self.eliminar_toc_en_archivo_markdown(ruta_destino)
            if self.toc_files:
                self.generar_actualizar_toc(ruta_destino)
        elif os.path.isdir(ruta_destino):
            # Si es un directorio, procesar todos los archivos Markdown en el directorio
            for directorio_actual, subdirectorios, archivos in os.walk(ruta_destino):
                # Omitir directorios
                if self.es_parte_de_ruta_ignorada(directorio_actual):
                    continue

                for archivo in archivos:
                    # Generar TOC para archivos markdown si no estan en la lista de ignorados
                    if archivo.endswith('.md') and not self.es_archivo_ignorado(archivo):
                        ruta_archivo = os.path.join(directorio_actual, archivo)
                        if self.rm_toc_files:
                            self.eliminar_toc_en_archivo_markdown(str(ruta_archivo))
                        if self.toc_files:
                            self.generar_actualizar_toc(str(ruta_archivo))
        else:
            print(f"La ruta proporcionada no es un archivo .md válido o un directorio: {ruta_destino}")

    def generar_actualizar_toc(self, ruta_destino):
        toc = self.generar_toc_para_archivo(ruta_destino)
        self.actualizar_toc_en_archivo_markdown(ruta_destino, toc)
