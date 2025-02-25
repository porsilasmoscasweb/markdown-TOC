# -*- coding: utf-8 -*-
import os
import shutil
import re
import markdown

def convert_markdown_to_html_with_images(input_file, output_file, input_dir, output_dir):
    """
    Convierte un archivo Markdown a HTML y copia imágenes referenciadas.

    :param input_file: Ruta del archivo Markdown de entrada.
    :param output_file: Ruta del archivo HTML de salida.
    :param input_dir: Directorio raíz de entrada que contiene los archivos Markdown.
    :param output_dir: Directorio raíz de salida para guardar los archivos HTML e imágenes.
    """
    try:
        # Crear el directorio de salida si no existe
        os.makedirs(os.path.dirname(output_file), exist_ok=True)

        # Leer el contenido del archivo Markdown
        with open(input_file, 'r', encoding='utf-8') as md_file:
            markdown_content = md_file.read()

        # Buscar imágenes en el contenido Markdown
        image_paths = re.findall(r'!\[.*?\]\((.*?)\)', markdown_content)
        for image_path in image_paths:
            # Resolver ruta de la imagen (relativa a absoluta)
            image_absolute_path = os.path.join(os.path.dirname(input_file),
                                               image_path)

            # Generar ruta de salida para la imagen
            relative_image_path = os.path.relpath(image_absolute_path, input_dir)
            output_image_path = os.path.join(output_dir, relative_image_path)

            # Copiar la imagen al directorio de salida si existe
            if os.path.exists(image_absolute_path):
                os.makedirs(os.path.dirname(output_image_path), exist_ok=True)
                shutil.copy2(image_absolute_path, output_image_path)

            # Actualizar la ruta en el contenido Markdown
            markdown_content = markdown_content.replace(image_path, os.path.relpath(output_image_path, os.path.dirname(output_file)))

        html = markdown.markdown(markdown_content)

        title = "MD HTML"
        match = re.search(r"<h1.*?>(.*?)</h1>", html, re.DOTALL)
        if match:
            title = match.group(1)
        # Convertir Markdown a HTML
        head_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title.title()}</title>
        </head>
        <body>
        """

        footer_content = """
        </body>
        </html>
        """

        html_content = head_content + html + footer_content

        # Guardar el HTML en el archivo de salida
        with open(output_file, 'w', encoding='utf-8') as html_file:
            html_file.write(html_content)

        print(f"Convertido: {input_file} -> {output_file}")
    except Exception as e:
        print(f"Error al procesar {input_file}: {e}")


def process_directory_recursively_with_images(input_dir, output_dir):
    """
    Procesa un directorio de forma recursiva para convertir archivos Markdown a HTML y copiar imágenes.

    :param input_dir: Directorio raíz de entrada que contiene los archivos Markdown.
    :param output_dir: Directorio raíz de salida para guardar los archivos HTML e imágenes.
    """
    try:
        for root, _, files in os.walk(input_dir):
            for file in files:
                if file.endswith(".md"):
                    # Ruta completa del archivo Markdown
                    input_file = os.path.join(root, file)

                    # Ruta correspondiente en el directorio de salida
                    relative_path = os.path.relpath(input_file, input_dir)
                    output_file = os.path.join(output_dir, relative_path).replace(".md",".html")

                    # Convertir Markdown a HTML y manejar imágenes
                    convert_markdown_to_html_with_images(input_file, output_file, input_dir, output_dir)
    except Exception as e:
        print(f"Error al procesar el directorio: {e}")


if __name__ == "__main__":
    input_dir = "/Users/egarriga/Git/markdown-TOC/memento_h"
    output_dir = "/Users/egarriga/Git/markdown-TOC/memento_h_o"

    if not os.path.isdir(input_dir):
        print(f"La ruta {input_dir} no es un directorio válido.")
    else:
        process_directory_recursively_with_images(input_dir, output_dir)
