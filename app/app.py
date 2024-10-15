# -*- coding: utf-8 -*-
from __future__ import absolute_import

from flask import Flask, render_template, request, redirect, url_for, send_file
import os
from . import procesar_archivos_markdown  # Importa tu script de procesamiento


app = Flask(__name__)
UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Asegúrate de que la carpeta de subidas exista
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
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
        procesar_archivos_markdown(filepath)

        # Enviar el archivo procesado de vuelta
        return send_file(filepath, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
