import os
import shutil
import re
import markdown

class MarkdownConverter:
    def __init__(self, input_dir, output_html_dir=None):
        """
        Inicializa la clase con los directorios de entrada y salida.

        :param input_dir: Directorio raíz de entrada que contiene los archivos Markdown.
        :param output_html_dir: Directorio raíz de salida para guardar los archivos HTML e imágenes.
        """
        if output_html_dir is None:
            output_html_dir = input_dir + "_html"
        self.input_dir = input_dir
        self.output_html_dir = output_html_dir

        self.TOC_INICIO = "<!-- TOC INICIO -->"
        self.TOC_FIN = "<!-- TOC FIN -->"

    def convert_markdown_to_html_with_images(self,
                                             input_file,
                                             output_file,
                                             input_dir,
                                             output_dir):
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

            # Clean the text
            sort_match = re.match(r'\[\/\/\]:\s*<>\s*\(order:(asc|desc)\)', markdown_content)
            if sort_match:
                markdown_content = self.clean_text(markdown_content, sort_match.group())

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

            # Convertir Markdown a HTML
            html = markdown.markdown(markdown_content)

            # TODO : Extraer el TOC entre las etiquetas <!-- TOC INICIO --> y <!-- TOC FIN --> para que se cree en un contenedor aparte.
            # TODO : Recorrer todo el TOC <ul> y crear un dict con el contenido de cada <li><a href="**">**texto</a></li> con la key {'#**': '**texto'}.
            # TODO : Al recorrer el listado aprovechamos para corregir el "#link" con accentos
            # TODO : Añadir id="ref_toc_link" a cada <h*> del contenido
            new_html = ""
            toc_html = ""
            toc = ""
            content = ""
            if self.TOC_INICIO in html and self.TOC_FIN in html:
                # Desde el TOC_FIN dividimos el contenido
                # Desde el TOC_INICIO volvemos a dividir el contenido
                # El nuevo html se forma con TOC_INICIO[0] + self.TOC_INICIO + toc + self.TOC_FIN + TOC_FIN[1]
                pass

            # Crear titulo
            title = "MD HTML"
            match = re.search(r"<h1.*?>(.*?)</h1>", html, re.DOTALL)
            if match:
                title = match.group(1)

            # Crear estructura HTML
            html_content = f"""
            <!DOCTYPE html>
            <html>
            <head>
            
            <meta name="robots" content="noindex, nofollow" />
            <meta name="google" content="notranslate" />
            <meta name="referrer" content="no-referrer" />
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <meta name="theme-color" content="#000000" />
            <meta property="og:image" content="https://timenet-wcp.gpisoftware.com/assets/icons/picto-timenet-512x512.png">
            
            <link rel="icon" type="image/png" sizes="32x32" href="favicon.ico">
            <link rel="icon" type="image/png" sizes="16x16" href="favicon.ico">
            <link rel="stylesheet" type="text/css" href="styles.css">
            
            <style>
            </style>
            
            <title>{title.title()}</title>
            </head>
            <body>
            <div id="wrapper">
            <div id="nav_toc">{toc_html}</div>
            <div id="content">{new_html}</div>
            </div>
            </body>
            </html>
            """

            # Guardar el HTML en el archivo de salida
            with open(output_file, 'w', encoding='utf-8') as html_file:
                html_file.write(html_content)
            print(f"Convertido: {input_file} -> {output_file}")
        except Exception as e:
            print(f"Error al procesar {input_file}: {e}")

    def clean_text(self, text, remove_string):
        # Remove the specific string (e.g., '[//]: <> (order:asc)')
        text_without_string = re.sub(re.escape(remove_string), '', text)

        # Remove empty lines and leading spaces
        cleaned_text = '\n'.join(line.strip() for line in text_without_string.split('\n') if line.strip())

        return cleaned_text

    def process_directory_recursively_with_images(self, input_dir, output_dir):
        """
        Procesa un directorio de forma recursiva para convertir archivos Markdown a HTML y copiar imágenes.

        :param input_dir: Directorio raíz de entrada que contiene los archivos Markdown.
        :param output_dir: Directorio raíz de salida para guardar los archivos HTML e imágenes.
        """
        try:
            if not os.path.isdir(input_dir):
                msg = f"La ruta base {input_dir} no es un directorio valido, por lo que no se puede hacer una copia."
                raise Exception("ERROR", msg)

            for root, _, files in os.walk(input_dir):
                for file in files:
                    if file.endswith(".md"):
                        # Ruta completa del archivo Markdown
                        input_file = os.path.join(root, file)

                        # Ruta correspondiente en el directorio de salida
                        relative_path = os.path.relpath(input_file, input_dir)
                        output_file = os.path.join(output_dir, relative_path).replace(".md",".html")

                        # Convertir Markdown a HTML y manejar imágenes
                        self.convert_markdown_to_html_with_images(input_file, output_file, input_dir, output_dir)
        except:
            raise Exception("Error", f"Error al procesar el directorio: {input_file}")
