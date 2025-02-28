<!-- TOC INICIO -->
- [07. Programas para desarrollar](#07-programas-para-desarrollar)
  - [PYCHARM](#pycharm)
<!-- TOC FIN -->

# 07. Programas para desarrollar

## PYCHARM

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

* Añadir plugin `docker`
  * `Plugins > Docker > Install > Apply`
