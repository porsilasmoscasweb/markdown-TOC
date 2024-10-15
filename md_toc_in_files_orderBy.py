# -*- coding: utf-8 -*-
import os
import re

# Lista de archivos a ignorar
IGNORAR = ['README.md', '.DS_Store', '.idea', 'footage']
TOC_INICIO = "<!-- TOC INICIO -->"
TOC_FIN = "<!-- TOC FIN -->"


def es_archivo_ignorado(nombre):
    """Función para ignorar archivos ocultos o que están en la lista de ignorados."""
    return nombre.startswith('.') or nombre in IGNORAR


def generar_slug(heading):
    """
    Convierte un encabezado en una ancla de markdown compatible.
    Reemplaza espacios por guiones, elimina caracteres especiales y convierte a minúsculas.
    """
    slug = heading.strip().lower()
    slug = re.sub(r'[^\w\s-]', '', slug)  # Eliminar caracteres especiales
    slug = slug.replace(' ', '-')  # Reemplazar espacios por guiones
    return slug


def extraer_secciones(contenido):
    """
    Extrae las secciones que empiezan con un encabezado y su contenido asociado.

    Args:
        contenido (str): Contenido del archivo Markdown.

    Returns:
        list: Lista de secciones. Cada sección es una tupla (encabezado, contenido).
    """
    secciones = []
    seccion_actual = []
    encabezado_actual = None
    dentro_bloque_codigo = False

    for linea in contenido.splitlines():
        # Detectar inicio o fin de bloque de código (``` o ~~~)
        if linea.strip().startswith('```') or linea.strip().startswith('~~~'):
            dentro_bloque_codigo = not dentro_bloque_codigo
            seccion_actual.append(linea)
            continue

        # Si estamos dentro de un bloque de código, añadir el contenido sin procesar
        if dentro_bloque_codigo:
            seccion_actual.append(linea)
            continue

        # Detectar encabezados de nivel 1 y 2
        if linea.startswith('#'):  # Secciones de nivel 1 y 2
            if encabezado_actual is not None:
                # Guardar la sección anterior
                secciones.append((encabezado_actual, "\n".join(seccion_actual)))
            # Iniciar una nueva sección
            encabezado_actual = linea.strip()
            seccion_actual = [linea]  # Capturar la nueva sección desde el encabezado
        else:
            # Acumular el contenido dentro de la sección actual
            seccion_actual.append(linea)

    # Guardar la última sección si hay una
    if encabezado_actual is not None:
        secciones.append((encabezado_actual, "\n".join(seccion_actual)))

    return secciones


def ordenar_secciones(secciones, orden="asc"):
    """
    Ordena las secciones basadas en los encabezados.

    Args:
        secciones (list): Lista de secciones en formato (encabezado, contenido).
        orden (str): "asc" para ascendente, "desc" para descendente.

    Returns:
        list: Lista de secciones ordenadas.
    """
    return sorted(secciones, key=lambda s: s[0], reverse=(orden == "desc"))


def aplicar_orden_al_archivo(ruta_archivo, orden):
    """
    Aplica la ordenación de las secciones del archivo Markdown según la directiva "order".

    Args:
        ruta_archivo (str): Ruta del archivo Markdown.
        orden (str): "asc" para ascendente, "desc" para descendente.
    """
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()

    # Extraer secciones
    secciones = extraer_secciones(contenido)
    # Ordenar secciones
    secciones_ordenadas = ordenar_secciones(secciones, orden)

    # Reescribir el archivo sin el TOC y con las secciones ordenadas
    nuevo_contenido = "\n\n".join([seccion[1] for seccion in secciones_ordenadas])

    # Escribir el contenido ordenado en el archivo, manteniendo la primera línea
    with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
        archivo.write(nuevo_contenido)


def generar_toc_para_archivo(ruta_archivo):
    """
    Genera el TOC basado en los encabezados dentro de un archivo Markdown,
    ignorando los encabezados dentro de bloques de código.

    Args:
        ruta_archivo (str): Ruta del archivo Markdown.

    Returns:
        str: TOC en formato markdown.
    """
    toc = []
    dentro_bloque_codigo = False  # Variable para rastrear si estamos dentro de un bloque de código

    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            # Detectar inicio o fin de bloque de código (``` o ~~~)
            if linea.strip().startswith('```') or linea.strip().startswith('~~~'):
                dentro_bloque_codigo = not dentro_bloque_codigo
                continue  # Ignorar esta línea (no es un encabezado)

            # Si estamos dentro de un bloque de código, ignorar el contenido
            if dentro_bloque_codigo:
                continue

            # Buscar líneas que comiencen con uno o más `#` para detectar encabezados
            if linea.startswith('#'):
                nivel = linea.count('#')  # El nivel se define por el número de `#`
                encabezado_texto = linea.strip('#').strip()
                slug = generar_slug(encabezado_texto)  # Generar el ancla
                toc.append(f"{'  ' * (nivel - 1)}- [{encabezado_texto}](#{slug})")  # Crear la línea del TOC

    return "\n".join(toc)


def actualizar_toc_en_archivo_markdown(ruta_archivo, toc, comentario_orden):
    """
    Actualiza el TOC en un archivo Markdown, añadiéndolo o sustituyéndolo
    entre los delimitadores TOC_INICIO y TOC_FIN.
    Mantiene el comentario de orden como primera línea.

    Args:
        ruta_archivo (str): Ruta del archivo Markdown.
        toc (str): Contenido del TOC generado.
        comentario_orden (str): Comentario inicial de orden.
    """
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()

    # Verificar si existe un TOC en el contenido
    if TOC_INICIO in contenido and TOC_FIN in contenido:
        # Reemplazar TOC existente
        nuevo_contenido = contenido.split(TOC_INICIO)[0] + TOC_INICIO + "\n" + toc + "\n" + TOC_FIN + \
                          contenido.split(TOC_FIN)[1]
    else:
        # Añadir TOC después del comentario de orden, si lo hay
        nuevo_contenido = comentario_orden + "\n\n" + TOC_INICIO + "\n" + toc + "\n" + TOC_FIN + "\n\n" + contenido

    # Escribir el contenido actualizado en el archivo
    with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
        archivo.write(nuevo_contenido)


def procesar_archivos_markdown(ruta_base):
    """
    Procesa un archivo Markdown o todos los archivos Markdown en un directorio,
    añadiendo o sustituyendo el TOC y aplicando orden si se especifica.

    Args:
        ruta_base (str): Ruta base del directorio o archivo Markdown.
    """
    if os.path.isfile(ruta_base) and ruta_base.endswith('.md'):
        # Procesar solo el archivo específico
        with open(ruta_base, 'r', encoding='utf-8') as archivo:
            primera_linea = archivo.readline().strip()
            contenido_restante = archivo.read()

        # Detectar si el archivo contiene la directiva de orden
        match = re.match(r'\[\/\/\]:\s*<>\s*\(order:(asc|desc)\)', primera_linea)
        if match:
            orden = match.group(1)
            aplicar_orden_al_archivo(ruta_base, orden)

        # Generar y actualizar TOC después de ordenar
        toc = generar_toc_para_archivo(ruta_base)
        actualizar_toc_en_archivo_markdown(ruta_base, toc, primera_linea)  # Pasar el comentario de orden

    elif os.path.isdir(ruta_base):
        # Procesar todos los archivos Markdown en el directorio
        for directorio_actual, subdirectorios, archivos in os.walk(ruta_base):
            for archivo in archivos:
                if archivo.endswith('.md') and not es_archivo_ignorado(archivo):
                    ruta_archivo = os.path.join(directorio_actual, archivo)
                    procesar_archivos_markdown(ruta_archivo)


if __name__ == "__main__":
    ruta_base = input("Introduce el path del archivo o directorio base: ")
    procesar_archivos_markdown(ruta_base)
    print("Procesado completado.")
