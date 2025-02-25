import os
import pytest
from classes.TOC import MarkdownTOCGenerator

@pytest.fixture
def generador():
    """Crea una instancia de MarkdownTOCGenerator para pruebas."""
    return MarkdownTOCGenerator("/home/egarriga/Documents/markdown-TOC/test/fake", ["node_modules", "venv"])

def test_es_archivo_ignorado(generador):
    """Verifica que los archivos y directorios ignorados sean correctamente detectados."""
    assert generador.es_archivo_ignorado("README.md") is True
    assert generador.es_archivo_ignorado(".DS_Store") is True
    assert generador.es_archivo_ignorado("normal_file.txt") is False
    assert generador.es_archivo_ignorado("node_modules") is True  # En la lista de ignorados personalizados

def test_formatear_nombre(generador):
    """Verifica que los nombres de archivos y directorios sean correctamente formateados."""
    assert generador.formatear_nombre("normal_file.txt") == "Normal file"
    assert generador.formatear_nombre("my_folder", es_directorio=True) == "MY_FOLDER"
    assert generador.formatear_nombre("another_file.py") == "Another file"

def test_generar_toc_markdown(tmp_path, generador):
    """Prueba la generación de la tabla de contenido utilizando archivos y directorios reales."""

    # Crear estructura de archivos real en el directorio temporal
    (tmp_path / "file1.txt").write_text("Contenido de file1")
    (tmp_path / "file2.md").write_text("Contenido de file2")
    dir1 = tmp_path / "dir1"
    dir1.mkdir()
    (dir1 / "subfile.md").write_text("Contenido de subfile")

    # Ejecutar el generador con la ruta temporal
    generador.ruta_base = str(tmp_path)  # Actualizamos la ruta base al directorio temporal
    resultado = generador.generar_toc_markdown(str(tmp_path), es_raiz=True)

    # Definir el resultado esperado
    esperado = (
        f"- 1. [DIR1/]({tmp_path / 'dir1'}/)\n"
        f"  - 1.1. [Subfile]({tmp_path / 'dir1' / 'subfile.md'})\n"
        f"- 2. [File1]({tmp_path / 'file1.txt'})\n"
        f"- 3. [File2]({tmp_path / 'file2.md'})"
    )

    assert resultado.strip() == esperado.strip()

def test_crear_readme_toc(mocker, generador, tmp_path):
    """Prueba la generación y escritura del archivo README.md."""
    mocker.patch.object(generador, "generar_toc_markdown", return_value="- 1. Sample TOC")
    generador.ruta_base = str(tmp_path)  # Usar un directorio temporal

    generador.crear_readme_toc()

    readme_path = tmp_path / "README.md"
    assert readme_path.exists()
    with open(readme_path, "r") as f:
        contenido = f.read()

    assert "# Tabla de Contenidos" in contenido
    assert "- 1. Sample TOC" in contenido
