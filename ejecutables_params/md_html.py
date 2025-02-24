from classes.TOC_html import MarkdownConverter

if __name__ == "__main__":
    input_dir = input("Ingresa la ruta del directorio de entrada (Markdown): ").strip()
    output_dir = input("Ingresa la ruta del directorio de salida (HTML): ").strip()

    if not os.path.isdir(input_dir):
        print(f"La ruta {input_dir} no es un directorio válido.")
    else:
        converter = MarkdownConverter(input_dir, output_dir)
        converter.process_directory_recursively_with_images()