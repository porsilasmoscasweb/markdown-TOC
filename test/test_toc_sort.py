import os
import pytest
from unittest.mock import mock_open, patch
from markdown.TOC_files import MarkdownTOCFiles


# Test para `es_archivo_ignorado`
def test_es_archivo_ignorado():
    # Crear una instancia de la clase
    updater = MarkdownTOCFiles(ruta_base=".")

    # Archivos que deberían ser ignorados
    assert updater.es_archivo_ignorado(".gitignore") is True
    assert updater.es_archivo_ignorado("README.md") is True
    assert updater.es_archivo_ignorado(".DS_Store") is True

    # Archivos que no deberían ser ignorados
    assert updater.es_archivo_ignorado("archivo.md") is False

# Test para `check_to_sort`
def test_check_to_sort():
    mock_file_content = "[//]: <> (order:asc)\n# Encabezado 1"

    # Crear una instancia de la clase
    updater = MarkdownTOCFiles(ruta_base=".", sort=True)

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
        updater = MarkdownTOCFiles('dummy.md', sort=True)

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
        updater = MarkdownTOCFiles('dummy.md', sort=True)

        # Procesamos el archivo
        updater.procesar_archivos_markdown('dummy.md')

        # Verificamos que el archivo fue escrito correctamente con el TOC ordenado
        mock_file.assert_called_once_with('dummy.md', 'w', encoding='utf-8')
        mock_file().write.assert_called_once_with(contenido_ordenado_desc)


