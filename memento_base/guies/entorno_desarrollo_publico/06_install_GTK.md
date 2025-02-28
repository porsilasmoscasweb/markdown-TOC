<!-- TOC INICIO -->
- [06. Install GTK](#06-install-gtk)
<!-- TOC FIN -->

# 06. Install GTK

Si se quiere instalar el cliente de escritorio GTK

El siguiente repositorio será el cliente del OpenERP, disponible en: https://github.com/gisce/erpclient

* Por si acaso no nos viene instalado el paquete pip
```bash
mkdir ~/proyectos
cd ~/proyectos
```

* Clonamos
```bash
git clone git@github.com:gisce/erpclient.git
cd erpclient
```

* Proseguimos con la instalación

<details>
<summary>Si se usa Ubuntu 22.04</summary>

* Antes de instalar estos dos repositorios, hay que instalar sus dependencias:
```bash
wget http://es.archive.ubuntu.com/ubuntu/pool/universe/w/what-is-python/python-is-python2_2.7.17-4_all.deb
wget http://es.archive.ubuntu.com/ubuntu/pool/main/p/pycairo/python-cairo_1.16.2-1_amd64.deb
wget http://es.archive.ubuntu.com/ubuntu/pool/universe/p/pygobject-2/python-gobject-2_2.28.6-12ubuntu3_amd64.deb
wget http://es.archive.ubuntu.com/ubuntu/pool/main/libf/libffi/libffi6_3.2.1-8_amd64.deb
wget http://es.archive.ubuntu.com/ubuntu/pool/universe/libg/libglade2/libglade2-0_2.6.4-2.4_amd64.deb
sudo dpkg -i python-is-python2_2.7.17-4_all.deb
sudo dpkg -i libffi6_3.2.1-8_amd64.deb
sudo dpkg -i libglade2-0_2.6.4-2.4_amd64.deb
sudo dpkg -i python-gobject-2_2.28.6-12ubuntu3_amd64.deb
sudo dpkg -i python-cairo_1.16.2-1_amd64.deb
```

* Creamos el entorno virtual de Python para el cliente de ERP
```bash
mkvirtualenv erpclient --system-site-packages -a ~/proyectos/erpclient
```

* Nos movemos a la carpeta del repositori
```bash
cd ~/proyectos/erpclient
```

* Entramos en el entorno virtual
```bash
workon erpclient
```

* Instalamos paquetes de python
```bash
easy_install egenix-mx-base
pip install -r requirements.txt
pip install pyOpenSSL
```

:warning: Los paquetes `python-gtk2` y/o `python-glade2` dan problemas para instalarse, se deben descargar e instalar manualmente desde su paquete `.deb`.

</details>

<details>
<summary>Si se usa Ubuntu 24.04</summary>

```bash
wget http://es.archive.ubuntu.com/ubuntu/pool/universe/p/pygtk/python-gtk2_2.24.0-5.1ubuntu2_amd64.deb
wget http://es.archive.ubuntu.com/ubuntu/pool/universe/p/pygtk/python-glade2_2.24.0-5.1ubuntu2_amd64.deb
sudo dpkg -i python-gtk2_2.24.0-5.1ubuntu2_amd64.deb
sudo dpkg -i python-glade2_2.24.0-5.1ubuntu2_amd64.deb

# En caso de dar error instalar lo siguiente:
sudo apt install python-cairo
sudo apt --fix-broken install
```

</details>

* El cliente utiliza el paquete `pygtk`, que no se lleva bien con los entornos virtuales, por lo que hará falta descargar y ejecutar este script en el entorno virtual.
https://gist.github.com/ecarreras/331db9be3b32b2e2ea5a1d4efc0ca69f


* Se puede pegar directamente el código en el terminal o se puede descargar el fichero [tools/link_pygtk_venv.sh](../../tools/link_pygtk_venv.sh) y ejecutarlo dándole permisos antes

```bash
chmod 711 ./link_pygtk_venv.sh
```

<details>
<summary>Contenido del fichero</summary>

```bash
#!/bin/bash
if [ "x$VIRTUAL_ENV" == "x" ]; then
    echo "Se debe activar el entorno virtual"
else
    for lib in cairo gi glib gobject gtk-2.0 pygtk.pth pygtk.py; do
        echo "Linking $lib...";
        ln -s /usr/lib/python2.7/dist-packages/$lib $VIRTUAL_ENV/lib/python2.7/site-packages/$lib;
    done
fi
```

</details>


Con esto queda instalado.

Seguidamente abrimos el fichero "bashrc" para crear la comanda que arranque la aplicación del cliente:
```bash
vim ~/.bashrc
```
Y ponemos esta función al final

```
erpclient(){
    ~/.virtualenvs/erpclient/bin/python ~/proyectos/erpclient/bin/openerp-client.py &
}
```

* Creamos un fichero nuevo (openerp.desktop):
```bash
vim ~/openerp.desktop
```

* Pegamos lo siguiente:
```bash
[Desktop Entry]
Encoding=UTF-8
Version=1.0
Type=Application
Terminal=false
Name=ERPClient
Exec=bash -ic "erpclient"
Icon=/home/<usuario>/proyectos/erpclient/bin/pixmaps/openerp-icon.ico
StartupNotify=true
Actions=New

[Desktop Action New]
Name=New OpenERP Client
Exec=bash -ic "erpclient"
OnlyShowIn=gnome
```

* Para que el acceso directo esté disponible para todos los usuarios desde el launcher, se puede ubicar en `/usr/share/applications/`. 
Y si se quiere poder añadir como "Favorito" a la barra de aplicaciones, hay que darle permisos de ejecución al fichero ( `sudo chmod +x`).

```bash
sudo chmod +x ~/openerp.desktop
sudo mv ~/openerp.desktop /usr/share/applications/
```

* Para comprobar que esta activo desde las aplicaciones buscamos `ERPClient`. Lo podremos poner en el `Dock` y en favoritos
