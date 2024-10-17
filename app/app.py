# -*- coding: utf-8 -*-
from __future__ import absolute_import

from flask import Flask, render_template, request, redirect, url_for, send_file
import os

# Importa tu script de procesamiento
from md_toc import crear_readme_toc
from md_toc_in_files import procesar_archivos_markdown as mk_toc_file
from md_toc_in_files_orderBy import  procesar_archivos_markdown as mk_toc_file_sort


app = Flask(__name__)
UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Asegúrate de que la carpeta de subidas exista
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload_dir', methods=['POST'])
def upload_dir():
    # Verificar si se ha subido un directorio (zipped)
    if 'dir' not in request.files:
        return redirect(request.url)
    file = request.files['dir']
    if file.filename == '':
        return redirect(request.url)

    # Verificar si el archivo es un zip
    if file and file.filename.endswith('.zip'):
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        # Extraer el zip para procesar su contenido
        from zipfile import ZipFile
        with ZipFile(filepath, 'r') as zip_ref:
            zip_ref.extractall(app.config['UPLOAD_FOLDER'])
            extracted_folder = os.path.join(app.config['UPLOAD_FOLDER'], zip_ref.namelist()[0].split('/')[0])

        # Crear el README.md con la tabla de contenidos
        crear_readme_toc(extracted_folder)

        # Devolver el README.md generado
        readme_path = os.path.join(extracted_folder, 'README.md')
        return send_file(readme_path, as_attachment=True)

@app.route('/upload_file', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file and file.filename.endswith('.md'):
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        # Procesar el archivo subido
        mk_toc_file(filepath)

        # Enviar el archivo procesado de vuelta
        return send_file(filepath, as_attachment=True)

@app.route('/upload_file_sort', methods=['POST'])
def upload_file_sort():
    if 'file_sort' not in request.files:
        return redirect(request.url)
    file = request.files['file_sort']
    if file.filename == '':
        return redirect(request.url)
    if file and file.filename.endswith('.md'):
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        # Procesar el archivo subido
        mk_toc_file_sort(filepath)

        # Enviar el archivo procesado de vuelta
        return send_file(filepath, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
