import os
import pytest
from unittest.mock import mock_open, patch
from mdTOC.TOC_files import MarkdownTOCFiles


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


# Test para `generar_slug`
def test_generar_slug():
    # Crear una instancia de la clase
    updater = MarkdownTOCFiles(ruta_base=".")

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
    updater = MarkdownTOCFiles(ruta_base=".")

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
    updater = MarkdownTOCFiles(ruta_base=".")

    # Usamos mock_open para simular la lectura y escritura de un archivo
    with patch("builtins.open", mock_open(read_data=mock_file_content)) as mock_file:
        updater.actualizar_toc_en_archivo_markdown("dummy.md", nuevo_toc)

        # Verificar que open fue llamado con los argumentos correctos
        mock_file.assert_called_with("dummy.md", "w", encoding="utf-8")

        # Verificar que el contenido fue escrito correctamente
        mock_file().write.assert_called_once_with(
            "\n<!-- TOC INICIO -->\n" + nuevo_toc + "\n<!-- TOC FIN -->\n# Encabezado 1\n"
        )
