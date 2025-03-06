import os
import shutil
import re
from unidecode import unidecode
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

    def clean_accents(self, toc_html):
        matches = re.findall(r'(<a href="#[^"]+">)([^<]+)(</a>)', toc_html)
        for full_match, text, closing_tag in matches:
            new_full_match = unidecode(full_match)  # Quitar acentos
            toc_html = toc_html.replace(f"{full_match}{text}{closing_tag}", f"{new_full_match}{text}{closing_tag}")
        return toc_html

    def generate_id(self, text):
        text = unidecode(text)  # Remover acentos
        text = text.lower().strip()  # Convertir a minúsculas y eliminar espacios
        text = re.sub(r'\s+', '-', text)  # Reemplazar espacios con guiones
        text = re.sub(r'[^a-z0-9\-]', '', text)  # Eliminar caracteres no válidos
        return text

    def add_ids_to_headers(self, new_html):
        pattern = re.compile(r'(<h(\d)>)\s*([^<]+)\s*(</h\d>)')

        def replace_header(match):
            opening_tag, level, content, closing_tag = match.groups()
            header_id = self.generate_id(content)
            return f'{opening_tag[:-1]} id="{header_id}">{content}{closing_tag}'

        return pattern.sub(replace_header, new_html)

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

            new_html = html
            toc_html = ""
            if self.TOC_INICIO in html and self.TOC_FIN in html:
                # Desde el TOC_FIN dividimos en toc y contenido
                toc_html, new_html = html.split(self.TOC_FIN)

                # Eliminamos el comentario de TOC_INICIO
                toc_html = toc_html.replace(self.TOC_INICIO, "")

            # Correguimos si es necesario los link del TOC
            toc_html = self.clean_accents(toc_html)

            # Añadimos los id a cada h* del contenido
            new_html = self.add_ids_to_headers(new_html)

            # Crear titulo
            title = "MD HTML"
            match = re.search(r"<h1.*?>(.*?)</h1>", html, re.DOTALL)
            if match:
                title = match.group(1)

            # Crear estructura HTML
            # <meta name="theme-color" content="#000000" />
            # <meta property="og:image" content="https://timenet-wcp.gpisoftware.com/assets/icons/picto-timenet-512x512.png">
            html_content = f"""
            <!DOCTYPE html>
            <html>
            <head>
            
            <meta name="robots" content="noindex, nofollow" />
            <meta name="google" content="notranslate" />
            <meta name="referrer" content="no-referrer" />
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            
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
