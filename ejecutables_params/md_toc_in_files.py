from classes.TOC_files import MarkdownTOCUpdater

if __name__ == "__main__":
    ruta_directorio = input("Introduce el path del directorio base: ").strip()
    ignorar_directorio = input("Algun directorio a ignorar (separados por espacios): ").strip()
    ignorar_directorios = ignorar_directorio.split()

    updater = MarkdownTOCUpdater(ruta_directorio, ignorar_directorios)
    updater.procesar_archivos_markdown(ruta_directorio)
    print("Archivos Markdown procesados con éxito.")
