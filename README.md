# TOC

## INSTALL

```bash
pip install pytest
pip install pytest-mock
```

## VERIFICAR PLUGIN

```bash
pytest --fixtures
```

## RUN

```bash
python script.py /ruta/al/directorio --ignorar dir1 dir2 dir3
```

## TEST

Explicación de las pruebas:

* **test_es_archivo_ignorado**: Verifica que los archivos y carpetas en la lista de ignorados sean detectados correctamente.
* **test_formatear_nombre**: Confirma que los nombres de archivos y directorios se formatean correctamente.
* **test_generar_toc_markdown**: Simula una estructura de archivos y verifica que la tabla de contenido generada es la esperada.
* **test_crear_readme_toc**: Usa un directorio temporal (tmp_path) para probar la escritura del archivo README.md.