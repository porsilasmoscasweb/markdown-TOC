# -*- coding: utf-8 -*-
import pytest
import sys
import os
import shutil
import subprocess

INPUT_DIR = "/home/egarriga/Documents/markdown-TOC/memento"
INPUT_FILE = "/home/egarriga/Documents/markdown-TOC/memento/wiki.md"

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
    """Ejecuta el script sin argumentos y verifica la salida."""
    result = subprocess.run(["python3", "generar_TOC.py", INPUT_DIR, "input_dir"], capture_output=True, text=True)
    assert "error" in result.stderr.lower()

def test_copy():
    """Ejecuta el script con --arg y verifica la salida."""
    dir = "/tmp/copy_TOC"
    result = subprocess.run(["python3", "generar_TOC.py", INPUT_DIR, "--copy", dir], capture_output=True, text=True)
    assert "/tmp/copy_TOC" in result.stdout
    rmtree(dir)

def test_copy_default():
    """Ejecuta el script con --copy pero sin valor, esperando un error."""
    dir = INPUT_DIR+"_copy"
    result = subprocess.run(["python3", "generar_TOC.py", INPUT_DIR, "--copy"], capture_output=True, text=True)
    assert dir in result.stdout  # argparse mostrará un mensaje de error
    rmtree(dir)

def test_copy_file():
    """Ejecuta el script con --copy pero sin valor, esperando un error."""
    result = subprocess.run(["python3", "generar_TOC.py", INPUT_FILE, "--copy"], capture_output=True, text=True)
    assert "error" in result.stderr.lower()  # argparse mostrará un mensaje de error

def test_toc():
    """Ejecuta el script sin argumentos y verifica la salida."""
    result = subprocess.run(["python3", "generar_TOC.py", INPUT_DIR, "--toc"], capture_output=True, text=True)
    assert f"Archivo README.md generado con éxito en la ruta {INPUT_DIR}." in result.stdout
    rmfile(INPUT_DIR+"/README.md")

def test_toc_file():
    """Ejecuta el script con --arg y verifica la salida."""
    result = subprocess.run(["python3", "generar_TOC.py", INPUT_FILE, "--toc"], capture_output=True, text=True)
    assert "error" in result.stderr.lower()

def test_toc_output():
    """Ejecuta el script sin argumentos y verifica la salida."""
    output_dir = "/tmp/test_output_dir"
    result = subprocess.run(["python3", "generar_TOC.py", INPUT_DIR, "--toc", "--output_dir", output_dir], capture_output=True, text=True)
    assert f"Archivo README.md generado con éxito en la ruta {output_dir}." in result.stdout
    rmtree(output_dir)

def test_toc_output_default():
    """Ejecuta el script sin argumentos y verifica la salida."""
    output_dir = INPUT_DIR + "_output"
    result = subprocess.run(["python3", "generar_TOC.py", INPUT_DIR, "--toc", "--output_dir"], capture_output=True, text=True)
    assert f"Archivo README.md generado con éxito en la ruta {output_dir}." in result.stdout
    rmtree(output_dir)

def test_toc_output_ignorar():
    """Ejecuta el script sin argumentos y verifica la salida."""
    output_dir = "/tmp/test_output_dir"
    subprocess.run(["python3", "generar_TOC.py", INPUT_DIR, "--toc", "--output_dir", output_dir, "--ignorar", "guies"], capture_output=True, text=True)
    assert not os.path.isdir(output_dir+"/guies")
    rmtree(output_dir)

def test_toc_output_ignorar_lista():
    """Ejecuta el script sin argumentos y verifica la salida."""
    output_dir = "/tmp/test_output_dir"
    subprocess.run(["python3", "generar_TOC.py", INPUT_DIR, "--toc", "--output_dir", output_dir, "--ignorar"] + ["guies", "wiki.md"], capture_output=True, text=True)
    assert not os.path.isdir(output_dir+"/guies")
    assert not os.path.isfile(output_dir+"/wiki.md")
    rmtree(output_dir)
