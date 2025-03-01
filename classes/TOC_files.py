# -*- coding: utf-8 -*-
import os
import re
from Base.base import MarkdownBase

class MarkdownTOCFiles(MarkdownBase):
    def __init__(self, ruta_base, ignorar_directorios=None):
        """
        Inicializa la clase con el directorio base y la lista de directorios a ignorar.
        Definir inició i fin del bloque TOC dentro de ficheros

        :param ruta_base: Ruta base del directorio.
        :param ignorar_directorios: Lista de directorios a ignorar (opcional).
        """
        super().__init__(ruta_base, ignorar_directorios=ignorar_directorios)

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

    def actualizar_toc_en_archivo_markdown(self, ruta_archivo, toc):
        """
        Actualiza el TOC en un archivo Markdown, añadiéndolo o sustituyéndolo
        entre los delimitadores TOC_INICIO y TOC_FIN.

        Args:
            ruta_archivo (str): Ruta del archivo Markdown.
            toc (str): Contenido del TOC generado.
        """
        nuevo_contenido = ""
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()

        # Detectar si el archivo contiene la directiva de orden
        match = re.match(r'\[\/\/\]:\s*<>\s*\(order:(asc|desc)\)', contenido)
        if match:
            nuevo_contenido = match.group()
            contenido = contenido.split(match.group())[1]

        if self.TOC_INICIO in contenido and self.TOC_FIN in contenido:
            # Reemplazar TOC existente
            nuevo_contenido += contenido.split(self.TOC_INICIO)[0] + self.TOC_INICIO + "\n" + toc + "\n" + self.TOC_FIN + \
                              contenido.split(self.TOC_FIN)[1]
        else:
            # Añadir TOC al principio
            if match:
                nuevo_contenido += "\n\n"
            nuevo_contenido += self.TOC_INICIO + "\n" + toc + "\n" + self.TOC_FIN + "\n\n" + contenido

        # Escribir el contenido actualizado en el archivo
        with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
            archivo.write(nuevo_contenido)

    def procesar_archivos_markdown(self, ruta_base):
        """
        Procesa todos los archivos Markdown en el directorio, añadiendo o
        sustituyendo el TOC en cada uno de ellos.

        Args:
            ruta_base (str): Ruta base del directorio o archivo Markdown.
        """
        if os.path.isfile(ruta_base) and ruta_base.endswith('.md'):
            # Si es un archivo Markdown, procesar solo ese archivo
            toc = self.generar_toc_para_archivo(ruta_base)
            self.actualizar_toc_en_archivo_markdown(ruta_base, toc)
        elif os.path.isdir(ruta_base):
            # Si es un directorio, procesar todos los archivos Markdown en el directorio
            for directorio_actual, subdirectorios, archivos in os.walk(ruta_base):
                # Omitir directorios
                if self.es_parte_de_ruta_ignorada(directorio_actual):
                    continue

                for archivo in archivos:
                    # Generar TOC para archivos markdown si no estan en la lista de ignorados
                    if archivo.endswith('.md') and not self.es_archivo_ignorado(archivo):
                        ruta_archivo = os.path.join(directorio_actual, archivo)
                        toc = self.generar_toc_para_archivo(ruta_archivo)
                        self.actualizar_toc_en_archivo_markdown(ruta_archivo, toc)
        else:
            print(f"La ruta proporcionada no es un archivo .md válido o un directorio: {ruta_base}")
