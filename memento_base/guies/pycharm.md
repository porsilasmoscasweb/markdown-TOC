<!-- TOC INICIO -->
- [PYCHARM](#pycharm)
  - [INSTALL](#install)
  - [PyCharm Live Templates for OpenERP](#pycharm-live-templates-for-openerp)
    - [Install](#install)
    - [Use](#use)
  - [SNIPPETS](#snippets)
    - [Create Custom Live Templates](#create-custom-live-templates)
    - [Import Live Templates from a ZIP File:](#import-live-templates-from-a-zip-file)
    - [Pre-Built Live Templates:](#pre-built-live-templates)
    - [Export](#export)
  - [CONFIG](#config)
    - [PEP 8](#pep-8)
<!-- TOC FIN -->

# PYCHARM

## INSTALL

<details>
<summary>Descargar si el link no funciona</summary>

Con esto tenemos los requerimientos para desarrollar. Hace falta un editor, preferiblemente un IDE para python. 
Nosotros recomendamos PyCharm (https://www.jetbrains.com/pycharm/)

:warning: Desde hace un tiempo, para descargar la versión "Community" de Pycharm, hay que ir al enlace que dice 
"Other versions", sino se descargará la versión profesional por defecto y esta requiere licencia.

</details>

* Descargaremos el fichero comprimido que nos proporciona la web oficial 

> [Download Pycharm](https://www.jetbrains.com/es-es/edu-products/download/download-thanks-pce.html)

* Lo descomprimiremos en el directorio que deseemos [/home]. 
```bash
tar -xvf ~/home/<usuario>/<pycharm>/<archive>.tar.gz
```

* Dentro de la carpeta raíz, abriremos la carpeta **bin**
```bash
cd ~/home/<usuario>/<pycharm>/bin
```

* Ejecutaremos el archivo 
```bash
./pycharm.sh
```

* Para crear un `launcher` de PyCharm en el escritorio, una vez abierto, utilizamos el menú: 
  * `Tools > Create Desktop Entry`

## PyCharm Live Templates for OpenERP

### Install

[OpenERP Live Templates - File](../tools/OpenERP.xml)

```bash
cp OpenERP.xml ~/.config/JetBrains/PyCharmXX/templates/
```

### Use

Open `OpenERP.xml` with `Pycharm`

Press `Ctrl + J` into `<templateSet group="****">` o set the live template

Existing features (in parentheses the keyword to use inside the PyCharm file):

* Python
  * Creating __terp__.py (__terp__)
  * Creating a function field (ff)
  * Creating a write function field (ff_inv)
  * Creating a search function field (ff_search)
  * Creating the name_get function (name_get)
  * Creating the function name_search (name_search)
  * Creating an object (osv_class)
  * Returning a report from a function (return_report)
  * Return a window from a function (return_window)

* XML
  * Creating the <openerp> <data> tags (openerp_tags)
  * Creating an action (ir_action)
  * Creating a view (ir_ui_view)
  * Creating a menu (menuitem)
  * Creating a security group (security)
  * Creating a shortcut from one object to another (shortcut)
  * Defining a wizard (wizard)
  * Add a field tag (field)

## SNIPPETS

### Create Custom Live Templates

* File > Settings > Editor > Live Templates
* Click the + button to create a new template
* Define the template abbreviation, template text, and optional variables
 
### Import Live Templates from a ZIP File:

* Select File | Manage IDE Settings | Import Settings from the menu.
* Specify the path to the archive with the exported live templates.
* In the Select Components to Import dialog, select the Live templates checkbox and click OK.

### Pre-Built Live Templates:

PyCharm comes with a set of pre-built Live Templates for various programming languages, including Python

* File > Settings > Editor > Live Templates and selecting the desired language

### Export

* Choose File | Manage IDE Settings | Export Settings from the menu.
* In the Export Settings dialog, make sure that the Live templates (schemes) checkbox is selected and specify the path and name of the archive, 
where the exported settings will be saved.
* Note that the Live templates checkbox appears in the Export Settings dialog if you have at least one custom live template in your project.
* Click OK to generate the file based on the exported settings. You can share this file with your team members, or import it on another IntelliJ IDEA installation.

OR

* ~/.config/JetBrains/PyCharmCE2024.2(current)/templates


## CONFIG

### PEP 8

Per conficurar el PEP 8 tan a XMl com a Python utilitzarem la ruta

> File > Settings > Editor > Code Style > [Language] 

* `Python`: 80
* `XML`: 120

