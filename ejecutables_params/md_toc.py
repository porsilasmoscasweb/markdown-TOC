from classes.TOC import MarkdownTOCGenerator

if __name__ == "__main__":
    ruta_directorio = input("Introduce el path del directorio base: ").strip()
    ignorar_directorio = input("Algun directorio a ignorar (separados por espacios): ").strip()
    ignorar_directorios = ignorar_directorio.split()

    generador = MarkdownTOCGenerator(ruta_directorio, ignorar_directorios)
    generador.crear_readme_toc()