import os
import shutil
import re
import markdown

class MarkdownConverter:
    def __init__(self, input_dir, output_dir):
        """
        Inicializa la clase con los directorios de entrada y salida.

        :param input_dir: Directorio raíz de entrada que contiene los archivos Markdown.
        :param output_dir: Directorio raíz de salida para guardar los archivos HTML e imágenes.
        """
        self.input_dir = input_dir
        self.output_dir = output_dir

    import re



    def convert_markdown_to_html_with_images(self, input_file, output_file):
        """
        Convierte un archivo Markdown a HTML y copia imágenes referenciadas.

        :param input_file: Ruta del archivo Markdown de entrada.
        :param output_file: Ruta del archivo HTML de salida.
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

            # Extraer el TOC entre las etiquetas <!-- TOC INICIO --> y <!-- TOC FIN -->
            toc_match = re.search(r"<!-- TOC INICIO -->(.*?)<!-- TOC FIN -->", markdown_content, re.DOTALL)
            if toc_match:
                toc_markdown = toc_match.group(1).strip()
                toc_html = self.convert_toc_markdown_to_html(toc_markdown)
                markdown_content = markdown_content.replace(toc_match.group(0), toc_html)

            # Buscar imágenes en el contenido Markdown
            image_paths = re.findall(r'!\[.*?\]\((.*?)\)', markdown_content)
            for image_path in image_paths:
                # Resolver ruta de la imagen (relativa a absoluta)
                image_absolute_path = os.path.join(os.path.dirname(input_file),
                                                   image_path)

                # Generar ruta de salida para la imagen
                relative_image_path = os.path.relpath(image_absolute_path, self.input_dir)
                output_image_path = os.path.join(self.output_dir, relative_image_path)

                # Copiar la imagen al directorio de salida si existe
                if os.path.exists(image_absolute_path):
                    os.makedirs(os.path.dirname(output_image_path), exist_ok=True)
                    shutil.copy2(image_absolute_path, output_image_path)

                # Actualizar la ruta en el contenido Markdown
                markdown_content = markdown_content.replace(image_path, os.path.relpath(output_image_path, os.path.dirname(output_file)))

            html = markdown.markdown(markdown_content)

            # Get title from H1
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

            # Convertir Markdown a HTML
            html_content = head_content + html + footer_content

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

    def convert_toc_markdown_to_html(self, toc_markdown):
        """
        Convierte el TOC en formato Markdown a una lista HTML anidada,
        reemplazando los enlaces con la versión .html.

        :param toc_markdown: Texto del TOC en Markdown.
        :return: TOC convertido en HTML con enlaces correctos.
        """
        lines = toc_markdown.strip().split("\n")
        html_toc = []
        prev_indent = 0

        # TODO : Modificafr el link. ruta_entrada por ruta_salida i extencion .md por .html
        for line in lines:
            match = re.match(r"(\s*)- \[(.*?)\]\(([^)#]+)(#.*?)?\)", line)
            if match:
                indent = len(match.group(1)) // 2  # Cada 2 espacios = 1 nivel de indentación
                text = match.group(2)
                filename = match.group(3)
                anchor = match.group(4) if match.group(4) else ""  # Mantener el ancla si existe

                # Convertir archivo .md a .html
                if filename.endswith(".md"):
                    filename = filename.replace(".md", ".html")

                link = filename + anchor  # Combinar con la ancla si existe

                if indent > prev_indent:
                    html_toc.append("<ul>" * (indent - prev_indent))
                elif indent < prev_indent:
                    html_toc.append("</ul>" * (prev_indent - indent))

                html_toc.append(f'<li><a href="{link}">{text}</a></li>')
                prev_indent = indent

        # Cerrar listas abiertas
        html_toc.append("</ul>" * prev_indent)

        return "\n".join(html_toc)

    def process_directory_recursively_with_images(self):
        """
        Procesa un directorio de forma recursiva para convertir archivos Markdown a HTML y copiar imágenes.
        """
        try:
            for root, _, files in os.walk(self.input_dir):
                for file in files:
                    if file.endswith(".md"):
                        # Ruta completa del archivo Markdown
                        input_file = os.path.join(root, file)

                        # Ruta correspondiente en el directorio de salida
                        relative_path = os.path.relpath(input_file, self.input_dir)
                        output_file = os.path.join(self.output_dir, relative_path).replace(".md", ".html")

                        # Convertir Markdown a HTML y manejar imágenes
                        self.convert_markdown_to_html_with_images(input_file, output_file)
        except Exception as e:
            print(f"Error al procesar el directorio: {e}")
