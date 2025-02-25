import os
import pytest
from unittest.mock import mock_open, patch
from classes.TOC_files import MarkdownTOCUpdater


# Test para `es_archivo_ignorado`
def test_es_archivo_ignorado():
    # Crear una instancia de la clase
    updater = MarkdownTOCUpdater(ruta_base=".")

    # Archivos que deberían ser ignorados
    assert updater.es_archivo_ignorado(".gitignore") is True
    assert updater.es_archivo_ignorado("README.md") is True
    assert updater.es_archivo_ignorado(".DS_Store") is True

    # Archivos que no deberían ser ignorados
    assert updater.es_archivo_ignorado("archivo.md") is False


# Test para `generar_slug`
def test_generar_slug():
    # Crear una instancia de la clase
    updater = MarkdownTOCUpdater(ruta_base=".")

    # Verificar la generación del slug
    assert updater.generar_slug("Este es un encabezado") == "este-es-un-encabezado"
    assert updater.generar_slug("Encabezado con caracteres raros!@#$%^") == "encabezado-con-caracteres-raros"


# Test para `generar_toc_para_archivo`
def test_generar_toc_para_archivo():
    # Simularemos la lectura de un archivo Markdown
    mock_file_content = """
# Título principal
## Subtítulo 1
### Subsubtítulo 1.1
## Subtítulo 2
"""

    # Crear una instancia de la clase
    updater = MarkdownTOCUpdater(ruta_base=".")

    # Usaremos mock_open para simular la lectura de un archivo
    with patch("builtins.open", mock_open(read_data=mock_file_content)):
        toc = updater.generar_toc_para_archivo("dummy.md")

    # Verificar que el TOC se genera correctamente
    assert toc == """- [Título principal](#título-principal)
  - [Subtítulo 1](#subtítulo-1)
    - [Subsubtítulo 1.1](#subsubtítulo-11)
  - [Subtítulo 2](#subtítulo-2)"""


# Test para `actualizar_toc_en_archivo_markdown`
def test_actualizar_toc_en_archivo_markdown():
    # Simulamos el contenido de un archivo con TOC
    mock_file_content = """
<!-- TOC INICIO -->
- [Encabezado 1](#encabezado-1)
<!-- TOC FIN -->
# Encabezado 1
"""
    nuevo_toc = "- [Nuevo encabezado](#nuevo-encabezado)"

    # Crear una instancia de la clase
    updater = MarkdownTOCUpdater(ruta_base=".")

    # Usamos mock_open para simular la lectura y escritura de un archivo
    with patch("builtins.open", mock_open(read_data=mock_file_content)) as mock_file:
        updater.actualizar_toc_en_archivo_markdown("dummy.md", nuevo_toc)

        # Verificar que open fue llamado con los argumentos correctos
        mock_file.assert_called_with("dummy.md", "w", encoding="utf-8")

        # Verificar que el contenido fue escrito correctamente
        mock_file().write.assert_called_once_with(
            "\n<!-- TOC INICIO -->\n" + nuevo_toc + "\n<!-- TOC FIN -->\n# Encabezado 1\n"
        )


# Test para `check_to_sort`
def test_check_to_sort():
    mock_file_content = "[//]: <> (order:asc)\n# Encabezado 1"

    # Crear una instancia de la clase
    updater = MarkdownTOCUpdater(ruta_base=".", sort=True)

    # Usamos mock_open para simular la lectura de un archivo
    with patch("builtins.open", mock_open(read_data=mock_file_content)), \
            patch("classes.TOC_files.MarkdownOrdenador") as mock_ordenador:
        mock_ordenador.return_value.ordenar.return_value = "Contenido ordenado"

        primera_linea = updater.check_to_sort("dummy.md")

        # Verificar que la primera línea es la directiva de orden
        assert primera_linea == "[//]: <> (order:asc)"
        mock_ordenador.return_value.ordenar.assert_called_once()


# Contenido de prueba para los archivos Markdown
contenido_original_ascendente = """[//]: <> (order:asc)

# Primer Encabezado
## Quinto Encabezado
# Tercer Encabezado
## Segundo Encabezado
### Cuarto Encabezado
"""

contenido_original_descendente = """[//]: <> (order:desc)

# Primer Encabezado
## Quinto Encabezado
# Tercer Encabezado
## Segundo Encabezado
### Cuarto Encabezado
"""

contenido_ordenado_asc = """[//]: <> (order:asc)

<!-- TOC INICIO -->
- [Primer Encabezado](#primer-encabezado)
  - [Quinto Encabezado](#quinto-encabezado)
- [Tercer Encabezado](#tercer-encabezado)
  - [Segundo Encabezado](#segundo-encabezado)
    - [Cuarto Encabezado](#cuarto-encabezado)
<!-- TOC FIN -->

# Primer Encabezado
## Quinto Encabezado
# Tercer Encabezado
## Segundo Encabezado
### Cuarto Encabezado
"""

contenido_ordenado_desc = """[//]: <> (order:desc)

<!-- TOC INICIO -->
- [Tercer Encabezado](#tercer-encabezado)
  - [Segundo Encabezado](#segundo-encabezado)
    - [Cuarto Encabezado](#cuarto-encabezado)
- [Primer Encabezado](#primer-encabezado)
  - [Quinto Encabezado](#quinto-encabezado)
<!-- TOC FIN -->

# Primer Encabezado
## Quinto Encabezado
# Tercer Encabezado
## Segundo Encabezado
### Cuarto Encabezado
"""

def test_ordenar_archivo_markdown_ascendente():
    # Usamos patch para simular la apertura de archivos
    with patch("builtins.open", mock_open(read_data=contenido_original_ascendente)) as mock_file, \
         patch("os.path.isfile", return_value=True), patch("os.path.isdir", return_value=False), \
         patch("os.walk", return_value=[('dummy_directory', [], ['dummy.md'])]):

        # Creamos la instancia de la clase con la opción sort activada
        updater = MarkdownTOCUpdater('dummy.md', sort=True)

        # Procesamos el archivo
        updater.procesar_archivos_markdown('dummy.md')

        # Verificamos que el archivo fue escrito correctamente con el TOC ordenado
        mock_file.assert_called_once_with('dummy.md', 'w', encoding='utf-8')
        mock_file().write.assert_called_once_with(contenido_ordenado_asc)

def test_ordenar_archivo_markdown_descendente():
    # Usamos patch para simular la apertura de archivos
    with patch("builtins.open", mock_open(read_data=contenido_original_descendente)) as mock_file, \
         patch("os.path.isfile", return_value=True), patch("os.path.isdir", return_value=False), \
         patch("os.walk", return_value=[('dummy_directory', [], ['dummy.md'])]):

        # Creamos la instancia de la clase con la opción sort activada
        updater = MarkdownTOCUpdater('dummy.md', sort=True)

        # Procesamos el archivo
        updater.procesar_archivos_markdown('dummy.md')

        # Verificamos que el archivo fue escrito correctamente con el TOC ordenado
        mock_file.assert_called_once_with('dummy.md', 'w', encoding='utf-8')
        mock_file().write.assert_called_once_with(contenido_ordenado_desc)


