# TOC

Generamos un TOC sobre la ruta proporcionada.

* Argumentos _(OPCIONALES)_:
  * `--files`: **BOOLEAN** generará un TOC por cada uno de los archivos `.md` que encuentre dentro de la ruta proporsionada.
  * `--ignorar`: **LISTA** separado por espacios, le podemos indicar directorios y/o archivos, los cuales van a ignorarse al 
    generar tanto el TOC general como el de cada archivo `.md` en caso de usar el parametro `--files`.
  * `--sort`: **BOOLEAN** los archivos `.md` pueden incluir una cabezera `[//]: <> (order:asc|desc)` indicando que esta va a ser 
    ordenada en la forma elegida previamente antes de generarse el TOC del archivo. 
    * En caso de que no se pase el parametro `--files` solo se ejecutará el sort **y la creación del nuevo TOC en caso de existir** 
      en los archivos donde se encuentre la cabezera.
  * `--html`: **STRING** HAcemos una copia de los archivos `.md` en formato HTML. Se generará una ruta de salida nueva que podrá 
    ser parte del parametro o en su ausencia crearse a través de la ruta proporcionada añadiendole un sufijo `_hmtl`.
    * :warning: Se intentará darle estilo al HTML a demás de que el TOC de cada archivo en caso de existir genere un nuevo estilo de 
      slug adecuado a HMTL.

## Requerimientos

Para poder correr los scripts será necessario tener instalados estos programas y librerias:

* python = 3.11.9
  * pytest 
  * pytest-mock

## Iintall python3 y pytest

### Windows

1. Download Python from the official site: [Python Downloads](https://www.python.org/downloads/)
2. Run the installer and **check the box** that says **"Add Python to PATH"** before clicking Install.
3. Open **Command Prompt** (`cmd`) and verify the installation:

### macOS

Method 1: Using Homebrew (Recommended)

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install python

Method 2: Download from Python.org

Download and install from [Python.org](https://www.python.org/downloads/macos/.


### Linux (Ubuntu/Debian)

1. Update package lists:

```shell
sudo apt update
```

2. Install Python 3:

```shell
sudo apt install python3 python3-pip
```

### Con todas las distribuciones

```shell
python3 --version
```

```shell
pip install pytest pytest-mock
```

```shell
pytest --fixtures
```

## Run script

```shell
python script.py /ruta/al/directorio --ignorar dir1 dir2 dir3 --files --sort --html {/ruta/al/directorio/de/salida}
```

## Test

Explicación de las pruebas:

* **test_es_archivo_ignorado**: Verifica que los archivos y carpetas en la lista de ignorados sean detectados correctamente.
* **test_formatear_nombre**: Confirma que los nombres de archivos y directorios se formatean correctamente.
* **test_generar_toc_markdown**: Simula una estructura de archivos y verifica que la tabla de contenido generada es la esperada.
* **test_crear_readme_toc**: Usa un directorio temporal (tmp_path) para probar la escritura del archivo README.md.