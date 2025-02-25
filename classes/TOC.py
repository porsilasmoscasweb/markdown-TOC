# -*- coding: utf-8 -*-
import os

class MarkdownTOCGenerator:
    def __init__(self, ruta_base, ignorar_directorios=None):
        """
        Inicializa la clase con el directorio base y la lista de directorios a ignorar.

        :param ruta_base: Ruta base del directorio.
        :param ignorar_directorios: Lista de directorios a ignorar (opcional).
        """
        if ignorar_directorios is None:
            ignorar_directorios = []
        self.ruta_base = ruta_base
        self.ignorar = ['README.md', '.DS_Store', '.gitignore', '.idea', 'footage', 'planning'] + ignorar_directorios
        # print(f"Ignorar configurado con: {self.ignorar}")

    def es_archivo_ignorado(self, nombre):
        """Función para ignorar archivos ocultos o que están en la lista de ignorados."""
        # print(f"Verificando: {nombre}, Ignorar: {self.ignorar}")
        return nombre.startswith('.') or nombre in self.ignorar

    def formatear_nombre(self, nombre, es_directorio=False):
        """
        Formatea el nombre del archivo o directorio.

        Args:
            nombre (str): Nombre del archivo o directorio.
            es_directorio (bool): Indica si el nombre es de un directorio.

        Returns:
            str: Nombre formateado.
        """
        if es_directorio:
            return nombre.upper()
        else:
            nombre_sin_ext, _ = os.path.splitext(nombre)
            nombre_sin_ext = nombre_sin_ext.replace('_', ' ')
            return nombre_sin_ext.capitalize()

    def generar_toc_markdown(self, ruta_base, nivel=0, indice_padre="", es_raiz=False):
        """
        Genera una tabla de contenidos en markdown basado en la estructura
        de directorios y subdirectorios.

        Args:
            ruta_base (str): Ruta base del directorio.
            nivel (int): Nivel de profundidad en la estructura (para los subdirectorios).
            indice_padre (str): El índice del directorio padre para mantener numeración.
            es_raiz (bool): Indica si estamos en la raíz para usar números legibles.

        Returns:
            str: TOC en formato markdown.
        """
        elementos = []
        indice_local = 1

        # Listar los directorios y archivos en la ruta base, ignorando ocultos y los de la lista IGNORAR
        for nombre in sorted(os.listdir(ruta_base)):
            if self.es_archivo_ignorado(nombre):
                continue

            ruta_completa = os.path.join(ruta_base, nombre)
            ruta_absoluta = os.path.abspath(ruta_completa)

            # Crear índice jerárquico (usar números legibles en la raíz)
            if es_raiz:
                indice_actual = f"{indice_local}."
            else:
                indice_actual = f"{indice_padre}{indice_local}."

            nombre_formateado = self.formatear_nombre(nombre, es_directorio=os.path.isdir(ruta_completa))

            if os.path.isdir(ruta_completa) and not os.path.islink(ruta_completa):
                # Si es un directorio, agregar al TOC con enlace absoluto y procesar recursivamente
                elementos.append(f"{'  ' * nivel}- {indice_actual} [{nombre_formateado}/]({ruta_absoluta}/)")
                sub_elementos = self.generar_toc_markdown(ruta_completa, nivel + 1, indice_actual)
                elementos.append(sub_elementos)
            else:
                # Si es un archivo, agregarlo al TOC con enlace absoluto
                elementos.append(f"{'  ' * nivel}- {indice_actual} [{nombre_formateado}]({ruta_absoluta})")

            indice_local += 1

        return "\n".join(elementos)

    def crear_readme_toc(self):
        """
        Crea el archivo README.md con el contenido del TOC generado.
        """
        toc = self.generar_toc_markdown(self.ruta_base, es_raiz=True)

        # Guardar el TOC en el archivo README.md
        with open(os.path.join(self.ruta_base, 'README.md'), 'w') as archivo_readme:
            archivo_readme.write("# Tabla de Contenidos\n\n")
            archivo_readme.write(toc)

        print("Archivo README.md generado con éxito.")
