# -*- coding: utf-8 -*-
import os
import re
from unidecode import unidecode
from mdTOC.core import MdToc

class MarkdownTOCFiles(MdToc):
    def __init__(self, root_path, destination_path=None, ignore=None, output_toc_filename="TOC", toc_files=False, rm_toc_files=False):
        """
        Initializes the class with the base directory, destination directory, and the list of directories to ignore to a file .md.

        Args:
            root_path: Base path of the directory.
            destination_path: Path of the directory.
            ignore: List of directories to ignore.
            output_toc_filename: Name of de resulting TOC file name.
            toc_files: Create toc on each md file from root_path
            rm_toc_files: Remove toc on each md file from root_path
        """
        super().__init__(root_path, destination_path=destination_path, ignore=ignore, output_toc_filename=output_toc_filename)

        self.toc_files = toc_files
        self.rm_toc_files = rm_toc_files

        self.TOC_INICIO = "<!-- TOC INICIO -->"
        self.TOC_FIN = "<!-- TOC FIN -->"

    def get_toc_start(self):
        return self.TOC_INICIO

    def get_toc_end(self):
        return self.TOC_FIN

    def generar_slug(self, heading):
        """
        Convierte un encabezado en una ancla de markdown compatible.
        Reemplaza espacios por guiones, elimina caracteres especiales y convierte a minúsculas.
        """
        slug = heading.strip().lower()
        slug = re.sub(r'[^\w\s-]', '', slug)  # Eliminar caracteres especiales
        slug = slug.replace(' ', '-')
        slug = unidecode(slug)# Reemplazar espacios por guiones
        return slug

    def get_content(self, ruta_archivo):
        toc = False
        nuevo_contenido = ""
        contenido = self.leer_markdown(ruta_archivo)
        has_toc_start = self.TOC_INICIO in contenido
        has_toc_end = self.TOC_FIN in contenido
        if has_toc_start and has_toc_end:
            toc = contenido.split(self.TOC_FIN)[0].strip()
            toc = toc.split(self.TOC_INICIO)[1].strip()
            nuevo_contenido = contenido.split(self.TOC_FIN)[1].strip()
        elif has_toc_start and has_toc_end:
            if not has_toc_end:
                raise Exception("ERROR", f"The file {ruta_archivo} has a bad TOC format generated with none end toc")
            if not has_toc_start:
                print("ERROR", f"The file {ruta_archivo} has a bad TOC format generated with none start toc. We get the init content of the file.")
                nuevo_contenido = contenido.split(self.TOC_FIN)[1].strip()
        else:
            nuevo_contenido = contenido.strip()

        return toc, nuevo_contenido

    # def has_sort(self, content):
    #     # Detectar si el archivo contiene la directiva de orden
    #     sort_content = False
    #     match = re.match(r'\[\/\/\]:\s*<>\s*\(order:(asc|desc)\)', content)
    #     if match:
    #         sort_content = match.group() + "\n\n"
    #         sort_content = sort_content.split(match.group())[1]
    #     return sort_content

    def generar_toc_para_archivo(self, ruta_archivo):
        """
        Genera el TOC basado en los encabezados dentro de un archivo Markdown,
        ignorando aquellos que estén dentro de bloques de código.

        Args:
            content (str): content Markdown from the file.

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

    @staticmethod
    def leer_markdown(ruta_archivo):
        try:
            with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
                return archivo.read()
        except Exception as e:
            raise Exception("ERROR", f"Can not read file {ruta_archivo}")

    @staticmethod
    def content_markdown(self, ruta_archivo):
        try:
            with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
                return archivo
        except Exception as e:
            raise Exception("ERROR", f"Can not read file {ruta_archivo}")

    @staticmethod
    def guardar_markdown(ruta_archivo, contenido):
        try:
            with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
                archivo.write(contenido)
        except Exception as e:
            raise Exception("ERROR", f"Can not write on file {ruta_archivo}")

    def eliminar_toc_en_archivo_markdown(self, ruta_archivo):
        """
        Eliminar el TOC en un archivo Markdown.

        Args:
            ruta_archivo (str): Ruta del archivo Markdown.
        """
        try:
            toc, content = self.get_content(ruta_archivo)
            self.guardar_markdown(ruta_archivo, content)
            return True
        except:
            raise Exception("ERROR", f"Al eleminar el TOC del fichero {ruta_archivo}")

    def procesar_archivos_markdown(self, ruta_destino=None):
        """
        Procesa todos los archivos Markdown en el directorio, añadiendo o
        sustituyendo el TOC en cada uno de ellos.

        Args:
            ruta_destino (str): Ruta ruta_destino del directorio o archivo Markdown.
        """
        if ruta_destino is None:
            ruta_destino = self.destination_path

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
                if self.file_has_ignore_part(directorio_actual):
                    continue

                for archivo in archivos:
                    # Generar TOC para archivos markdown si no estan en la lista de ignorados
                    if archivo.endswith('.md') and not self.has_ignore(archivo):
                        ruta_archivo = os.path.join(directorio_actual, archivo)
                        if self.rm_toc_files:
                            self.eliminar_toc_en_archivo_markdown(str(ruta_archivo))
                        if self.toc_files:
                            self.generar_actualizar_toc(str(ruta_archivo))
        else:
            print(f"La ruta proporcionada no es un archivo .md válido o un directorio: {ruta_destino}")

    def generar_actualizar_toc(self, ruta_destino):
        toc, content = self.get_content(ruta_destino)
        toc = self.generar_toc_para_archivo(ruta_destino)
        new_content = self.TOC_INICIO + "\n" + toc + "\n" + self.TOC_FIN + "\n\n" + content
        self.guardar_markdown(ruta_destino, new_content)
