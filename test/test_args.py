# -*- coding: utf-8 -*-
import platform
import os
import shutil
import subprocess

PATH_MAC = "/Users/egarriga/Git"
PATH_LINUX = "/home/egarriga/Documents"

INPUT_DIR = PATH_MAC + "/markdown-TOC/memento"
INPUT_FILE = PATH_MAC + "/markdown-TOC/memento/wiki.md"

def rmtree(dir):
    try:
        shutil.rmtree(dir)
    except OSError as e:
        print(f"Error: {e.strerror}")

def rmfile(file_path):
    try:
        os.remove(file_path)
        print(f"File \'{file_path}\' deleted successfully.")
    except FileNotFoundError:
        print(f"File \'{file_path}\' not found.")
    except PermissionError:
        print(f"Permission denied to delete the file \'{file_path}\'.")
    except Exception as e:
        print(f"Error occurred while deleting the file: {e}")

def test_sin_argumentos():
    """Ejecuta el script sin argumentos. No se hace nada."""
    result = subprocess.run(["python3", "generar_TOC.py", INPUT_DIR], capture_output=True, text=True)
    assert "" in result.stdout

def test_copy():
    """Ejecuta el script con --copy con valores. Debe crear una copia del directorio de entrada al directorio de salida, ignorando los directorios y ficheros por defecto."""
    dir_path = "/tmp/copy_TOC"
    result = subprocess.run(["python3", "generar_TOC.py", INPUT_DIR, "--copy", dir_path], capture_output=True, text=True)
    assert "/tmp/copy_TOC" in result.stdout
    rmtree(dir_path)

def test_copy_default():
    """Ejecuta el script con --copy sin valores. Debe crear una copia del directorio de entrada al directorio de salida por defecto, ignorando los directorios y ficheros por defecto."""
    dir_path = INPUT_DIR+"_copy"
    result = subprocess.run(["python3", "generar_TOC.py", INPUT_DIR, "--copy"], capture_output=True, text=True)
    assert dir_path in result.stdout  # argparse mostrará un mensaje de error
    rmtree(dir_path)

def test_copy_file():
    """Ejecuta el script con --copy con un valor de fichero, esperando un error."""
    result = subprocess.run(["python3", "generar_TOC.py", INPUT_FILE, "--copy"], capture_output=True, text=True)
    assert "error" in result.stderr.lower()  # argparse mostrará un mensaje de error

def test_toc():
    """Ejecuta el script con --toc. Debe de generar el fichero README.md en la ruta base."""
    subprocess.run(["python3", "generar_TOC.py", INPUT_DIR, "--toc"], capture_output=True, text=True)
    assert os.path.isfile(INPUT_DIR + "/README.md")
    rmfile(INPUT_DIR+"/README.md")

def test_toc_path_file():
    """"Ejecuta el script con --toc de un fichero. esperando un error."""
    result = subprocess.run(["python3", "generar_TOC.py", INPUT_FILE, "--toc"], capture_output=True, text=True)
    assert not os.path.isfile(INPUT_DIR + "/README.md")
    assert "error" in result.stderr.lower()

def test_toc_output():
    """Ejecuta el script con --output_dir con un valor. Debe crear una copia del directorio de entrada al directorio de salida, ignorando los directorios y ficheros por defecto.
    Debe de genearar el fichero README.md a la ruta de salida"""
    output_dir = "/tmp/test_output_dir"
    result = subprocess.run(["python3", "generar_TOC.py", INPUT_DIR, "--toc", "--output_dir", output_dir], capture_output=True, text=True)
    assert f"Archivo README.md generado con éxito en la ruta {output_dir}." in result.stdout
    assert os.path.isfile(output_dir + "/README.md")
    assert os.path.isdir(output_dir + "/guies")
    assert not os.path.isdir(output_dir + "/planning")
    rmtree(output_dir)

def test_toc_output_default():
    """Ejecuta el script con --output_dir sin valor. Debe crear una copia del directorio de entrada al directorio de salida por defecto, ignorando los directorios y ficheros por defecto.
    Debe de genearar el fichero README.md a la ruta de salida"""
    output_dir = INPUT_DIR + "_output"
    result = subprocess.run(["python3", "generar_TOC.py", INPUT_DIR, "--toc", "--output_dir"], capture_output=True, text=True)
    assert f"Archivo README.md generado con éxito en la ruta {output_dir}." in result.stdout
    assert os.path.isfile(output_dir + "/README.md")
    assert os.path.isdir(output_dir + "/guies")
    assert not os.path.isdir(output_dir + "/planning")
    rmtree(output_dir)

def test_toc_output_ignorar():
    """Ejecuta el script con --ignaorar sin un valor. Debe crear una copia del directorio de entrada al directorio de salida, ignorando los directorios y ficheros por defecto.
    Debe de genearar el fichero README.md a la ruta de salida"""
    output_dir = "/tmp/test_output_dir"
    subprocess.run(["python3", "generar_TOC.py", INPUT_DIR, "--toc", "--output_dir", output_dir, "--ignorar"], capture_output=True, text=True)
    assert os.path.isfile(output_dir + "/README.md")
    rmtree(output_dir)

def test_toc_output_ignorar():
    """Ejecuta el script con --ignaorar con un valor. Debe crear una copia del directorio de entrada al directorio de salida, ignorando los directorios y ficheros por defecto más los indicados.
    Debe de genearar el fichero README.md a la ruta de salida"""
    output_dir = "/tmp/test_output_dir"
    subprocess.run(["python3", "generar_TOC.py", INPUT_DIR, "--toc", "--output_dir", output_dir, "--ignorar", "guies"], capture_output=True, text=True)
    assert os.path.isfile(output_dir + "/README.md")
    assert not os.path.isdir(output_dir + "/guies")
    rmtree(output_dir)

def test_toc_output_ignorar_lista():
    """Ejecuta el script con --ignaorar con una lista de valores. Debe crear una copia del directorio de entrada al directorio de salida, ignorando los directorios y ficheros por defecto más los indicados.
    Debe de genearar el fichero README.md a la ruta de salida"""
    output_dir = "/tmp/test_output_dir"
    subprocess.run(["python3", "generar_TOC.py", INPUT_DIR, "--toc", "--output_dir", output_dir, "--ignorar"] + ["guies", "wiki.md"], capture_output=True, text=True)
    assert os.path.isfile(output_dir + "/README.md")
    assert not os.path.isdir(output_dir + "/guies")
    assert not os.path.isfile(output_dir + "/wiki.md")
    rmtree(output_dir)

def test_toc_file_output():
    """Ejecuta el script con --toc_files. Debe de recorrer todos los ficheros '.md' y generar el TOC dentro de cada uno de ellos, si ya existe lo sobre escribe."""
    output_dir_files = "/tmp/test_output_dir_files"
    subprocess.run(["python3", "generar_TOC.py", INPUT_DIR, "--output_dir", output_dir_files, "--toc_files"], capture_output=True, text=True)
    assert not os.path.isfile(INPUT_DIR + "/README.md")
    assert os.path.isfile(output_dir_files + "/wiki.md")
    with open(output_dir_files + "/wiki.md") as archivo:
        for line in archivo:
            if line == '<!-- TOC INICIO -->':
                assert True
    rmtree(output_dir_files)

def test_toc_file_output_default():
    """Ejecuta el script con --toc_files. Debe de recorrer todos los ficheros '.md' y generar el TOC dentro de cada uno de ellos, si ya existe lo sobre escribe."""
    output_dir_files = INPUT_DIR + "_output"
    subprocess.run(["python3", "generar_TOC.py", INPUT_DIR, "--output_dir", "--toc_files"], capture_output=True, text=True)
    assert not os.path.isfile(INPUT_DIR + "/README.md")
    assert os.path.isfile(output_dir_files + "/wiki.md")
    with open(output_dir_files + "/wiki.md") as archivo:
        for line in archivo:
            if line == '<!-- TOC FIN -->':
                assert True
    rmtree(output_dir_files)

def test_rm_toc_file_from_file():
    """Ejecuta el script con --rm_toc_files. Debe de recorrer todos los ficheros '.md' y eleminar el TOC dentro de cada uno de ellos."""
    with open(INPUT_DIR + "/wiki.md") as archivo:
        for line in archivo:
            if line == '<!-- TOC INICIO -->':
                assert True
    subprocess.run(["python3", "generar_TOC.py", INPUT_DIR, "--rm_toc_files"], capture_output=True, text=True)
    assert not os.path.isfile(INPUT_DIR + "/README.md")
    with open(INPUT_DIR + "/wiki.md") as archivo:
        for line in archivo:
            if line == '<!-- TOC INICIO -->':
                assert False

def test_toc_file():
    """Ejecuta el script con --toc_files. Debe de recorrer todos los ficheros '.md' y generar el TOC dentro de cada uno de ellos, si ya existe lo sobre escribe."""
    subprocess.run(["python3", "generar_TOC.py", INPUT_DIR, "--toc_files"], capture_output=True, text=True)
    assert not os.path.isfile(INPUT_DIR + "/README.md")
    with open(INPUT_DIR + "/wiki.md") as archivo:
        for line in archivo:
            if line == '<!-- TOC INICIO -->':
                assert True

def test_rm_toc_file_output_dir():
    """Ejecuta el script con --rm_toc_files. Debe de recorrer todos los ficheros '.md' y eleminar el TOC dentro de cada uno de ellos."""
    output_dir = INPUT_DIR + "_output"
    assert not os.path.isfile(output_dir + "/README.md")
    with open(INPUT_DIR + "/wiki.md") as archivo:
        for line in archivo:
            if line == '<!-- TOC INICIO -->':
                assert True
    subprocess.run(["python3", "generar_TOC.py", INPUT_DIR, "-rtf", "--output"], capture_output=True,
                   text=True)
    assert not os.path.isfile(output_dir + "/README.md")
    with open(output_dir + "/wiki.md") as archivo:
        for line in archivo:
            if line == '<!-- TOC INICIO -->':
                assert False
    with open(INPUT_DIR + "/wiki.md") as archivo:
        for line in archivo:
            if line == '<!-- TOC INICIO -->':
                assert True
    rmtree(output_dir)

def test_rm_toc_file_output_dir_file():
    """Ejecuta el script con --rm_toc_files. Debe de recorrer todos los ficheros '.md' y eleminar el TOC dentro de cada uno de ellos."""
    subprocess.run(["python3", "generar_TOC.py", INPUT_DIR, "-c"], capture_output=True, text=True)
    with open(INPUT_DIR + "_copy/wiki.md") as archivo:
        for line in archivo:
            if line == '<!-- TOC INICIO -->':
                assert True
    subprocess.run(["python3", "generar_TOC.py", INPUT_DIR + "_copy/wiki.md", "-rtf"], capture_output=True, text=True)
    with open(INPUT_DIR + "_copy/wiki.md") as archivo:
        for line in archivo:
            if line == '<!-- TOC INICIO -->':
                assert False
    rmtree(INPUT_DIR + "_copy")