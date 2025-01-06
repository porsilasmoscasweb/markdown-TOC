# -*- coding: utf-8 -*-
from __future__ import absolute_import

from flask import Flask, render_template, request, redirect, url_for, send_file, flash
import os
import shutil
import markdown
from datetime import datetime
from zipfile import ZipFile

# Importa tu script de procesamiento
from md_toc import crear_readme_toc
from md_toc_in_files import procesar_archivos_markdown as mk_toc_file
from md_toc_in_files_orderBy import procesar_archivos_markdown as mk_toc_file_sort

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'supersecretkey'  # Necesario para usar 'flash' en Flask

# Asegúrate de que la carpeta de subidas exista
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload_dir', methods=['POST'])
def upload_dir():
    if 'dir' not in request.files:
        flash('No se seleccionó ningún archivo.')
        return redirect(request.url)

    file = request.files['dir']
    if file.filename == '':
        flash('El archivo no tiene nombre.')
        return redirect(request.url)

    if file and file.filename.endswith('.zip'):
        # Crear un subdirectorio único para esta carga
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        unique_folder = os.path.join(app.config['UPLOAD_FOLDER'], "dir_{}".format(timestamp))
        os.makedirs(unique_folder)

        # Guardar y extraer el archivo zip
        filepath = os.path.join(unique_folder, file.filename)
        file.save(filepath)

        with ZipFile(filepath, 'r') as zip_ref:
            zip_ref.extractall(unique_folder)
            extracted_folder = os.path.join(unique_folder, zip_ref.namelist()[0].split('/')[0])

        # Crear el README.md con la tabla de contenidos
        crear_readme_toc(extracted_folder)
        readme_path = os.path.join(extracted_folder, 'README.md')

        if os.path.exists(readme_path):
            res = send_file(readme_path, as_attachment=True)

            # Limpiar archivos temporales
            shutil.rmtree(unique_folder)

            return res
        else:
            flash("Error al generar el archivo README.md.")
            return redirect(url_for('index'))
    else:
        flash('El archivo debe estar en formato .zip.')
        return redirect(request.url)

@app.route('/upload_file', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No se seleccionó ningún archivo.')
        return redirect(request.url)

    file = request.files['file']
    if file.filename == '':
        flash('El archivo no tiene nombre.')
        return redirect(request.url)

    if file and file.filename.endswith('.md'):
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        # Procesar el archivo subido
        mk_toc_file(filepath)

        res = send_file(filepath, as_attachment=True)

        # Limpiar archivo temporal
        os.remove(filepath)

        return res
    else:
        flash('El archivo debe ser un archivo Markdown (.md).')
        return redirect(request.url)

@app.route('/upload_file_sort', methods=['POST'])
def upload_file_sort():
    if 'file_sort' not in request.files:
        flash('No se seleccionó ningún archivo.')
        return redirect(request.url)

    file = request.files['file_sort']
    if file.filename == '':
        flash('El archivo no tiene nombre.')
        return redirect(request.url)

    if file and file.filename.endswith('.md'):
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        # Procesar el archivo subido
        mk_toc_file_sort(filepath)

        res = send_file(filepath, as_attachment=True)

        # Limpiar archivo temporal
        os.remove(filepath)

        return res
    else:
        flash('El archivo debe ser un archivo Markdown (.md).')
        return redirect(request.url)

@app.route('/render_file', methods=['POST'])
def render_file():
    if 'render_file' not in request.files:
        return redirect(request.url)
    file = request.files['render_file']
    if file.filename == '':
        return redirect(request.url)
    if file and file.filename.endswith('.md'):
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        # Convertir Markdown a HTML
        with open(filepath, 'r') as f:
            content = f.read()
            html_content = markdown.markdown(content)

        # Renderizar HTML en la página web
        return render_template('display_markdown.html', content=html_content)


if __name__ == '__main__':
    # Default
    # app.run(debug=True, use_debugger=False, use_reloader=Fasle, passthrough_errors=True)

    # Debug
    app.run(debug=True, use_debugger=True, use_reloader=True, passthrough_errors=True)
