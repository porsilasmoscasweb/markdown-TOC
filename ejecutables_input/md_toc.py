# -*- coding: utf-8 -*-
import os

# Lista de archivos a ignorar
IGNORAR = ['README.md', '.DS_Store', '.gitignore', '.idea', 'footage', 'planning']


def es_archivo_ignorado(nombre):
    """Función para ignorar archivos ocultos o que están en la lista de ignorados."""
    return nombre.startswith('.') or nombre in IGNORAR


def formatear_nombre(nombre, es_directorio=False):
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


def generar_toc_markdown(ruta_base, nivel=0, indice_padre="", es_raiz=False):
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
        if es_archivo_ignorado(nombre):
            continue

        ruta_completa = os.path.join(ruta_base, nombre)
        ruta_absoluta = os.path.abspath(ruta_completa)

        # Crear índice jerárquico (usar números legibles en la raíz)
        if es_raiz:
            indice_actual = f"{indice_local}."
        else:
            indice_actual = f"{indice_padre}{indice_local}."

        nombre_formateado = formatear_nombre(nombre, es_directorio=os.path.isdir(ruta_completa))

        if os.path.isdir(ruta_completa):
            # Si es un directorio, agregar al TOC con enlace absoluto y procesar recursivamente
            elementos.append(f"{'  ' * nivel}- {indice_actual} [{nombre_formateado}/]({ruta_absoluta}/)")
            sub_elementos = generar_toc_markdown(ruta_completa, nivel + 1, indice_actual)
            elementos.append(sub_elementos)
        else:
            # Si es un archivo, agregarlo al TOC con enlace absoluto
            elementos.append(f"{'  ' * nivel}- {indice_actual} [{nombre_formateado}]({ruta_absoluta})")

        indice_local += 1

    return "\n".join(elementos)


def crear_readme_toc(ruta_base):
    """
    Crea el archivo README.md con el contenido del TOC generado.

    Args:
        ruta_base (str): Ruta base del directorio.
    """
    print(IGNORAR)
    toc = generar_toc_markdown(ruta_base, es_raiz=True)

    # Guardar el TOC en el archivo README.md
    with open(os.path.join(ruta_base, 'README.md'), 'w') as archivo_readme:
        archivo_readme.write("# Tabla de Contenidos\n\n")
        archivo_readme.write(toc)


if __name__ == "__main__":
    ruta_directorio = input("Introduce el path del directorio base: ")
    ignorar_directorio = input("Algun directorio a ignorar: ")
    IGNORAR += ignorar_directorio.split()
    crear_readme_toc(ruta_directorio.strip())
    print("Archivo README.md generado con éxito.")
