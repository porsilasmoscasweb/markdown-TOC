import argparse
from classes.TOC_files_sort import  MarkdownOrdenador

def main():
    parser = argparse.ArgumentParser(
        description="Ordena un archivo Markdown por niveles de encabezado y alfabéticamente, con opción ascendente o descendente."
    )

    parser.add_argument(
        '-i', '--input',
        type=str,
        required=True,
        help="Ruta del archivo Markdown de entrada."
    )
    parser.add_argument(
        '-o', '--output',
        type=str,
        required=True,
        help="Ruta del archivo Markdown de salida."
    )
    parser.add_argument(
        '--order',
        type=str,
        choices=['asc', 'desc'],
        default='asc',
        help="Orden de clasificación: 'asc' (ascendente) o 'desc' (descendente). Por defecto es 'asc'."
    )
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help="Muestra información detallada durante la ejecución."
    )

    args = parser.parse_args()

    ordenador = MarkdownOrdenador()

    if args.verbose:
        print(f"📥 Leyendo archivo desde: {args.input}")

    markdown = MarkdownOrdenador.leer_markdown(args.input)

    if args.verbose:
        print(f"🔄 Ordenando el contenido en orden {'ascendente' if args.order == 'asc' else 'descendente'}...")

    markdown_ordenado = ordenador.ordenar(markdown, ascendente=(args.order == 'asc'))

    if args.verbose:
        print("✅ Contenido ordenado correctamente.")

    MarkdownOrdenador.guardar_markdown(args.output, markdown_ordenado)

    if args.verbose:
        print(f"💾 Archivo ordenado guardado en: {args.output}")

if __name__ == '__main__':
    main()
