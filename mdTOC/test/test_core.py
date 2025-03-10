# -*- coding: utf-8 -*-
import shutil
import os

from mdTOC.toc_files import MarkdownTOCFiles

ABSPATH = os.path.abspath('')
INPUT_DIR = ABSPATH + "/mdTOC/test"

def rmtree(curr_dir):
    try:
        shutil.rmtree(curr_dir)
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

def check_text_on_file(path_file, text_to_check):
    with open(path_file) as f:
        for line in f:
            if text_to_check in line:
                return True
    return False

def test_none_args():
    try:
        MarkdownTOCFiles()
    except Exception as e:
        assert "MarkdownTOCFiles.__init__() missing 1 required positional argument: 'root_path'" in str(e)


def test_only_root_dir_args():
    destination_path = INPUT_DIR + "/test_dir"
    toc_filename = INPUT_DIR + "/test_dir/TOC.md"
    MarkdownTOCFiles(INPUT_DIR)
    assert not os.path.exists(destination_path)
    assert not os.path.exists(toc_filename)

def test_diff_root_than_destination_path_args():
    root_path = INPUT_DIR + "/test_default"
    destination_path = INPUT_DIR + "/test_dir"
    toc_filename = destination_path + "/TOC.md"
    rmtree(destination_path)
    try:
        MarkdownTOCFiles(root_path, destination_path)
        assert os.path.exists(destination_path)
        assert os.path.exists(destination_path)
        assert not os.path.exists(toc_filename)
    finally:
        rmtree(destination_path)

def test_toc_args():
    root_path = INPUT_DIR + "/test_default"
    destination_path = INPUT_DIR + "/test_dir"
    toc_filename = destination_path + "/TOC.md"
    rmtree(destination_path)
    try:
        generador = MarkdownTOCFiles(root_path, destination_path)
        generador.create_toc()
        assert os.path.exists(destination_path)
        assert os.path.exists(toc_filename)
    finally:
        rmtree(destination_path)


def test_toc_output_file_name_args():
    root_path = INPUT_DIR + "/test_default"
    destination_path = INPUT_DIR + "/test_dir"
    toc_filename = destination_path + "/test_TOC_file_name.md"
    rmtree(destination_path)
    try:
        generador = MarkdownTOCFiles(root_path, destination_path=destination_path, output_toc_filename="test_TOC_file_name")
        generador.create_toc()
        assert os.path.exists(destination_path)
        assert os.path.exists(toc_filename)
        assert check_text_on_file(toc_filename, "# Table of Contents")
        assert not check_text_on_file(toc_filename, "invisible_file")
    finally:
        rmtree(destination_path)

def test_toc_ignore_dir():
    root_path = INPUT_DIR + "/test_default"
    destination_path = INPUT_DIR + "/test_dir"
    toc_filename = destination_path + "/TOC.md"
    rmtree(destination_path)
    try:
        generador = MarkdownTOCFiles(root_path, destination_path=destination_path, ignore=["ignore_dir"])
        generador.create_toc()
        assert os.path.exists(toc_filename)
        assert not os.path.exists(destination_path + "/ignore_dir")
        assert os.path.exists(destination_path + "/.invisible_dir")
    finally:
        rmtree(destination_path)

def test_toc_ignore_file():
    root_path = INPUT_DIR + "/test_default"
    destination_path = INPUT_DIR + "/test_dir"
    toc_filename = destination_path + "/TOC.md"
    rmtree(destination_path)
    try:
        generador = MarkdownTOCFiles(root_path, destination_path=destination_path, ignore=["ignore_file1.md"])
        generador.create_toc()
        assert os.path.exists(toc_filename)
        assert not os.path.exists(destination_path + "/ignore_file1.md")
        assert os.path.exists(destination_path + "/.invisible_dir")
    finally:
        rmtree(destination_path)
#
def test_toc_ignore_dir_and_file():
    root_path = INPUT_DIR + "/test_default"
    destination_path = INPUT_DIR + "/test_dir"
    toc_filename = destination_path + "/TOC.md"
    rmtree(destination_path)
    try:
        generador = MarkdownTOCFiles(root_path, destination_path=destination_path, ignore=["ignore_dir", "ignore_file1.md"])
        generador.create_toc()
        assert os.path.exists(toc_filename)
        assert not os.path.exists(destination_path + "/ignore_dir")
        assert not os.path.exists(destination_path + "/ignore_file1.md")
        assert os.path.exists(destination_path + "/.invisible_dir")
    finally:
        rmtree(destination_path)

def test_ERROR_destination_path_exists():
    root_path = INPUT_DIR + "/test_default"
    destination_path = INPUT_DIR + "/test_dir"
    rmtree(destination_path)
    try:
        MarkdownTOCFiles(root_path, destination_path=destination_path)
        MarkdownTOCFiles(root_path, destination_path=destination_path)
    except Exception as e:
        assert f'The destination Path {INPUT_DIR}/test_dir already exist.' in str(e)
    finally:
        rmtree(destination_path)