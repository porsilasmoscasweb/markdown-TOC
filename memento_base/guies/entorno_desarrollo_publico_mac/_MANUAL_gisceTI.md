# Instalar S.O.

<!-- TOC INICIO -->
- [Instalar S.O.](#instalar-so)
- [Instalar S.O.](#instalar-so)
  - [Paquetes del Sistema](#paquetes-del-sistema)
- [Instalamos Python 2.7](#instalamos-python-27)
- [Entorno de desarrollo](#entorno-de-desarrollo)
  - [Definir editor de texto por defecto](#definir-editor-de-texto-por-defecto)
  - [Estructura de ficheros](#estructura-de-ficheros)
  - [Entorno virtual de Python](#entorno-virtual-de-python)
  - [Configuración GIT](#configuración-git)
  - [OpenERP-Server](#openerp-server)
    - [Repositorios requeridos](#repositorios-requeridos)
  - [OpenERP-Client](#openerp-client)
- [Instalación del cliente web](#instalación-del-cliente-web)
- [En caso de dar error instalar lo siguiente:](#en-caso-de-dar-error-instalar-lo-siguiente)
- [Si se usa Ubuntu 22.04, antes de instalar estos dos repositorios, hay que instalar](#si-se-usa-ubuntu-2204-antes-de-instalar-estos-dos-repositorios-hay-que-instalar)
- [sus dependencias:](#sus-dependencias)
- [Creamos el entorno virtual de Python para el cliente de ERP](#creamos-el-entorno-virtual-de-python-para-el-cliente-de-erp)
- [Se puede pegar directamente el código en el terminal](#se-puede-pegar-directamente-el-código-en-el-terminal)
- [o se puede descargar el fichero que lo contiene y ejecutarlo](#o-se-puede-descargar-el-fichero-que-lo-contiene-y-ejecutarlo)
- [dándole permisos antes](#dándole-permisos-antes)
- [Preguntará el password para el nuevo usuario](#preguntará-el-password-para-el-nuevo-usuario)
- [Instalamos requerimientos del sistema](#instalamos-requerimientos-del-sistema)
- [Añadimos la clave del repositorio de Docker](#añadimos-la-clave-del-repositorio-de-docker)
- [Añadimos el repositorio de docker](#añadimos-el-repositorio-de-docker)
- [OPCIONAL: Arranque automático de los dockers al iniciar la sesión.](#opcional-arranque-automático-de-los-dockers-al-iniciar-la-sesión)
- [dockers  >> ~/.profile](#dockers---profile)
- [Tras reiniciar la sesión se aplicarán los cambios](#tras-reiniciar-la-sesión-se-aplicarán-los-cambios)
- [Tras reiniciar la sesión se aplicará el permiso](#tras-reiniciar-la-sesión-se-aplicará-el-permiso)
- [Desde el entorno virtual "erp"](#desde-el-entorno-virtual-erp)
<!-- TOC FIN -->

# Instalar S.O.

Recomendamos el uso de Ubuntu, ya que es el Sistema Operativo que utilizamos nosotros. Aún así, esta guía debería servir para todas las distribuciones Debian.

Una vez instalado, refrescamos el listado de paquetes y los actualizamos:

```bash
sudo apt-get update
sudo apt-get upgrade
```

## Paquetes del Sistema

Se requieren los siguientes paquetes, para empezar:

- **openvpn**, para conexiones en la red de la empresa
  - Paquetes: `openvpn, network-manager-openvpn` y possiblemente `network-manager-openvpn-gnome`
- **python**, necessario para desarrollar en Python
  - Paquetes: `python3-dev, python3-pip`
- **tmux**, multiplexor de terminal
  - Paquete: `tmux`, `terminator`
- **git**, necesario para el control de versiones y el desarrollo contínuo
  - Paquete: `git`

Ejecutaríamos:

```bash
# Necesarios
sudo apt-get install git vim htop curl openssh-server
```

# Instalamos Python 2.7

El ERP se ejecuta sobre Python 2.7, aunque se espera que en un futuro no muy lejano se ejecute sobre Python 3. Eso obliga a que el Sistema Operativo cuente con una versión 2.7 de Python, aunque sea para poder crear entornos virtuales para desarrollar.

```bash
# Instalamos repositorios necesarios para Pyenv
sudo apt install -y make build-essential libssl-dev \
zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev \
wget curl llvm libncursesw5-dev xz-utils tk-dev \
libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev libpq-dev python3-pip

# Descargamos Pyenv y lo ejecutamos
curl https://pyenv.run | bash

# Exportamos Pyenv al PATH del sistema
echo -e 'export PYENV_ROOT="$HOME/.pyenv"\nexport PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo -e 'eval "$(pyenv init --path)"\neval "$(pyenv init -)"' >> ~/.bashrc

# Refrescamos la ventana del terminal
exec "$SHELL"

# Comprobamos la versión de Pyenv
pyenv --version

# (Opcional) Es posible actualizar Pyenv con el 
# siguiente comando
pyenv update

# Instalamos la versión de Python 2.7
pyenv install 2.7.18
```

```bash
# Opcionales (utilizados por GISCE-TI)
sudo apt-get install tmux openvpn network-manager-openvpn meld terminator
```

# Entorno de desarrollo

En esta sección se van a configurar varios parámetros del propio entorno, como el editor de texto por defecto o la herramienta para crear entornos virtuales de Python para desarrollar.

## Definir editor de texto por defecto

Desde GISCE-TI utilizamos VIM, sin embargo se puede utilizar cualquier otro. Para configurarlo por defecto, utilizamos:

`sudo update-alternatives --config editor`

## Estructura de ficheros

Definiremos una carpeta para los proyectos i.e. `~/proyectos` con el comando:
```bash
mkdir ~/proyectos
```

## Entorno virtual de Python

Es posible crear un entorno virtual utilizando los comandos:

- `pyenv virtualenv <version> <nombre>` para crear un entorno virtual.
- `pyenv activate <nombre>` para activar un entorno virtual.
- `pyenv deactivate <nombre>` para desactivar un entorno virtual.
- `pyenv virtualenv-delete <nombre>` para eliminar un entorno virtual.

Los usaremos más adelante para crear nuestros entornos de **OpenERP-Client** y **OpenERP-Server**.

## Configuración GIT

Presuponemos que se dispone de usuario GIT con permisos para el código de GISCE-TI.

El primer paso será generar las claves SSH con el comando:

`ssh-keygen -t rsa -b 4096`

Seguidamente añadimos esta clave a nuestro usuario de GitHub (User > Setting > SSH and GPG keys)
Se puede obtener la clave leyendo el fichero generado por el comando anterior (p.e. `cat ~/.ssh/id_rsa.pub`).

Por último hace falta configurar un nombre y un correo para que git nos pueda identificar. Lo haremos con el siguiente comando:

`git config --global -e`

El nombre no es vinculante, pero el correo debe coincidir con el correo del usuario de GitHub.
Se puede configurar el editor de GIT por defecto en esta configuración.

Un ejemplo de configuración sería:
```
[user]
        email = <user>@<domain>
        name = Demo Name
[core]
        editor = vim
[commit]
        gpgsign = true
```
Sería interessante que todos los participantes utilizaramos claves GPG en nuestro ordenador principal. Se puede seguir la [Guía de GitHub para configurar una clave GPG](https://help.github.com/articles/signing-commits-using-gpg/).


## OpenERP-Server

El primer repositorio que clonaremos y configuraremos será “OpenERP Server”, disponible en: https://github.com/gisce/erp

```bash
cd ~/proyectos
git clone git@github.com:gisce/erp.git
```

Para el entorno hará falta instalar los siguientes paquetes de sistema:

```bash
sudo apt-get install libxslt1-dev libjpeg-dev gcc g++
```

Crearemos el entorno virtual de python con:

```bash
pyenv virtualenv 2.7.18 erp
pyenv activate erp
```

```bash
cd ~/proyectos/erp
# Ya desde el entorno virtual, instalamos los requerimientos básicos con:
easy_install egenix-mx-base

for a in vatnumber mako reportlab pydot tqdm psycopg2 Babel \
pymongo==2.9 rq==0.12 raven sentry psutil times xlwt pysftp \
redis osconf slugify fuzzywuzzy lockfile marshmallow==2.0.0b2 \
Python-Chart reportlab==3.0 osconf "libcomxml<2.2.4" \
unidecode pprintpp autoworker cython
do 
    pip install $a
done
```

### Repositorios requeridos

Instalaremos los requerimientos necesarios mediante el siguiente comando:

```bash
# Recuerda de ir al directorio de proyectos si no estás en el!
cd ~/proyectos

# Volcamos en un fichero los repositorios a descargar e instalar
cat > repositories <<EOF
mongodb_backend gisce
oorq api_v5
openerp-sentry v5_legacy
poweremail v5_backport
poweremail-modules master
spawn_oop master
ws_transactions master
sepa master
libFacturacioATR master
switching master
libComXML master
cchloader master #Temporaly gisce branch
sippers master
ir_attachment_mongodb master
qreu master
enerdata master
ooop xmlrpc_transaction # webforms and remote scripts need gisce's xt version
arquia master # webforms
sii master
empowering master #Temporaly FIX_marshmallow_requirement_minimum_version
gestionatr master
distri-remesa-parser master
pandapower_erp master
pandapower_validator master
crm_poweremail
EOF

# Instalamos los repositorios
cat repositories | while read p b comment; do
	git clone git+ssh://git@github.com/gisce/$p.git
	(cd $p; git checkout $b )
done

# Creamos enlaces simbólicos a algunos repositorios, que pueden ser llamados de varias maneras
ln -s poweremail poweremail2
ln -s libFacturacioATR libfacturacioatr

# Instalamos paquetes de Python necesarios
for a in sepa libFacturacioATR gestionatr \
switching libComXML sippers qreu enerdata arquia ooop \
distri-remesa-parser
do
    (cd $a; pip install -e .)
done
```

## OpenERP-Client

# Instalación del cliente web
https://rfc.gisce.net/t/deploy-webclient-local-development/1248

<details>
<summary>Si se quiere instalar el cliente de escritorio GTK usando docker</summary>

https://rfc.gisce.net/t/erpclient-a-ubuntu-20-04-focal-fossa-amb-docker/845/2

</details>

<details>
<summary>Si se quiere instalar el cliente de escritorio GTK localmente</summary>

El siguiente repositorio será el cliente del OpenERP, disponible en: https://github.com/gisce/erpclient

```bash
#Por si acaso no nos viene instalado el paquete pip
mkdir ~/proyectos
cd ~/proyectos
git clone git+ssh://git@github.com/gisce/erpclient.git
cd erpclient

# Proseguimos con la instalación

:warning: Los paquetes `python-gtk2` y/o `python-glade2` dan problemas para instalarse, se deben descargar e instalar manualmente desde su paquete `.deb`.
```
wget http://es.archive.ubuntu.com/ubuntu/pool/universe/p/pygtk/python-gtk2_2.24.0-5.1ubuntu2_amd64.deb
wget http://es.archive.ubuntu.com/ubuntu/pool/universe/p/pygtk/python-glade2_2.24.0-5.1ubuntu2_amd64.deb
sudo dpkg -i python-gtk2_2.24.0-5.1ubuntu2_amd64.deb
sudo dpkg -i python-glade2_2.24.0-5.1ubuntu2_amd64.deb

# En caso de dar error instalar lo siguiente:
sudo apt install python-cairo
sudo apt --fix-broken install

# Si se usa Ubuntu 22.04, antes de instalar estos dos repositorios, hay que instalar
# sus dependencias:
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

```bash
# Creamos el entorno virtual de Python para el cliente de ERP
mkvirtualenv erpclient --system-site-packages -a ~/proyectos/erpclient
cd ~/proyectos/erpclient
workon erpclient
easy_install egenix-mx-base
pip install -r requirements.txt
pip install pyOpenSSL
```

El cliente utiliza el paquete `pygtk`, que no se lleva bien con los entornos virtuales, por lo que hará falta descargar y ejecutar este script en el entorno virtual.
https://gist.github.com/ecarreras/331db9be3b32b2e2ea5a1d4efc0ca69f
```bash
# Se puede pegar directamente el código en el terminal
# o se puede descargar el fichero que lo contiene y ejecutarlo 
# dándole permisos antes
chmod 711 ./link_pygtk_venv.sh
./link_pygtk_venv.sh
```

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

Acceso directo (.desktop): 

```
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

Para que el acceso directo esté disponible para todos los usuarios desde el launcher, se puede ubicar en `/usr/share/applications/`. Y si se quiere poder añadir como "Favorito" a la barra de aplicaciones, hay que darle permisos de ejecución al fichero ( `sudo chmod +x`).

</details>

## Programas para desarrollar

### Instalación PyCharm

Con esto tenemos los requerimientos para desarrollar. Hace falta un editor, preferiblemente un IDE para python. Nosotros recomendamos PyCharm (https://www.jetbrains.com/pycharm/)

:warning: Desde hace un tiempo, para descargar la versión "Community" de Pycharm, hay que ir al enlace que dice "Other versions", sino se descargará la versión profesional por defecto y esta requiere licencia.

Descargaremos el fichero comprimido que nos proporciona la web oficial, lo descomprimiremos en el directorio que deseemos y dentro de la carpeta raíz, abriremos la carpeta **bin** y ejecutaremos el archivo **pycharm.sh**

Para crear un **launcher** de PyCharm en el escritorio, una vez abierto, utilizamos el menú: `Tools > Create Desktop Entry`

# Inicialización del entorno

## (Dockers) PostgreSQL [timescale+postgis],  redis y mongo
https://rfc.gisce.net/t/guia-unificada-para-montar-entorno-dockerizado-postgres-redis-y-mongo-con-supervisor/1265

<details>
  <summary>Si PostgreSQL no se instala via Docker</summary>

## PostgresSQL

Debemos configurar postgres para utilizar los recursos que corresponden a nuestro ordenador. Podemos utilizar la página siguiente para personalizar las configuraciones: http://pgtune.leopard.in.ua/

Hacen falta los siguientes parámetros:

* Versión de PostgreSQL. La podemos obtener ejecutando el siguiente comando: `psql -V`
* Sistema Operativo: Linux
* Tipo de BdD: Mixed
* RAM máxima que dejamos a Postgres (75% de la disponible). Con el siguiente comando podremos saber de cuanta memória principaln disponemos: `htop`
* Número de Conexiones. Si trabajamos en local ponemos 100

Llenamos los campos exigidos y copiaremos los datos generados por la página web al archivo de configuración. Para editarlo haremos: 

```bash
sudo vim /etc/postgresql/<version>/<cluster>/postgresql.conf
```

Aprovecharemos también para instalar la extensión **`TimeScaleDB`** de Postgres, siguiendo la guía: https://rfc.gisce.cloud/t/instal-lacio-de-lextensio-timescaledb-per-postgresql

Para efectuar los cambios reiniciaremos el proceso:

```bash
sudo systemctl restart postgresql
```

Por último debemos añadir nuestro usuario para utilizar las BdD locales (o configurar un usuario para ello).

```bash
sudo su - postgres
# Preguntará el password para el nuevo usuario
createuser <usuario> -s -P
```

## MongoDB + Redis en Docker

Si se quiere tener en el sistema directamente

```bash
sudo apt-get install mongodb-server redis-server
``` 

Instalamos MongoDB con:

```bash
# Instalamos requerimientos del sistema
sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common
# Añadimos la clave del repositorio de Docker
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
# Añadimos el repositorio de docker
sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
sudo apt-get update
sudo apt-get install docker-ce
```

</details>

Si se quiere que los procesos en docker arranquen automáticamente al iniciar
la sesión, se puede hacer con `supervisor` como se indica en la guía, o bien se puede ejecutar lo siguiente:
```bash
# OPCIONAL: Arranque automático de los dockers al iniciar la sesión.
# dockers  >> ~/.profile
echo docker start postgres >> ~/.profile
echo docker start redis30 >> ~/.profile
echo docker start mongo30  >> ~/.profile
# Tras reiniciar la sesión se aplicarán los cambios
```

Para poder ejecutar docker sin `sudo`, hay que añadir nuestro usuario al grupo `docker`, si no se ha hecho ya:
```bash
sudo groupadd docker
sudo gpasswd -a $USER docker 
# Tras reiniciar la sesión se aplicará el permiso
```

Aunque no tengamos PostgreSQL, Redis ni Mongo instalados en el sistema, podemos acceder a los mismos a través de docker si necesitamos operar o revisar las bases de datos por cualquier motivo:
```bash
docker exec -it postgres psql
docker exec -it mongo30 mongo
docker exec -it redis30 redis-cli
```

## Inicio de un servidor en entorno local

Antes de ejecutar el servidor es necesario configurar la carpeta `server/bin/addons` con los repositorios de fuera del ERP. Siempre que se añada otro módulo con un repositorio externo será necesario ejecutar el siguiente script:

`python tools/link_addons.py`

### Configuración del IDE - OpenERP-Server

Primero abrimos el proyecto ERP que hemos clonado.

El primer paso es configurar el virtualenv creado anteriormente para OpenERP-Server en el IDE. La explicación siguiente solo sirve para PyCharm.

Abrimos el menú “File > Settings”.
Accedemos a la pestaña “Project:ERP > Project Interpreter”
Seleccionamos el virtualenv del erp en el desplegable. Si no se encuentra ahí podemos localizarlo en `/home/<usuario>/.virtualenvs/erp`

#### Configuración de ejecución

Des del IDE podemos ejecutar  `erp/server/bin/openerp-server.py` nos creará la configuración por defecto y la podremos editar.
Alternativamente podemos poner directamente los parámetros para su ejecución.

Script a ejecutar desde el IDE: /<directorio_proyectos>/erp/server/bin/openerp-server.py 
Parámetros:

```bash
--no-netrpc
--price_accuracy=6
--port=8069
--db_user
<usuario_postgres> (por defecto el usuario de la máquina)
-d
<nombre_base_de_datos>
```

En la pestaña de entorno (Environment):

Environment Variables:

```
PYTHONIOENCODING=UTF-8
PYCHARM_HOSTED=1
PYTHONUNBUFFERED=1
OPENERP_REDIS_URL=redis://localhost
OPENERP_DB_HOST=localhost
OPENERP_DB_PASSWORD=<PASSWORD_POSTGRES>
OPENERP_DB_USER=<USER_POSTGRES>
```

Proyecto: `erp` (si se tiene más de un proyecto abierto)
Python Interpreter: Escoger el virtualenv del ERP
Working Directory: `/home/<usuario>/proyectos/erp/server/bin`

Debemos marcar las casillas:
Necesarias:
Añadir “content roots” al “PYTHONPATH”
Añadir “source roots” al “PYTHONPATH”

Recomendadas:
Show this page - Muestra la ventana de configuración al ejecutar
Single instance only - Asegura que se ejecute una sola instancia del ERP

#### Configuración de Ficheros

Hace falta marcar como “Sources root”, en este orden, las siguientes carpetas:

```
server/bin/addons
server/bin
server/sitecustomize
```

#### Instalación de requerimientos
Antes del primer arranque, es necesario instalar los requerimientos del proyecto:
```bash
# Desde el entorno virtual "erp"
pip install -r requirements.txt -r requirements-dev.txt
pip install -r ../oorq/requirements.txt
```

#### Primer arranque

La primera vez que iniciemos el servidor será necesario que ejecutemos una actualización de todos los modulos para que se instalen todos los requisitos. Para hacerlo debemos añadir el parámetro `--update=all`.


## Otras configuraciones:

Consulta los siguientes artículos para configurar el resto de componentes:

- [Destral](https://rfc.gisce.net/t/configurar-entorno-de-test-destral/304)
- [Reports](https://rfc.gisce.net/t/montar-entorno-de-desarrollo-reports/1992) 
- [Traducciones](https://rfc.gisce.net/t/traducciones-procedimiento-para-traducir-un-modulo/392)

## Bonus track: Utilidades varias

- Arranque automático de la VPN: https://rfc.gisce.net/t/manual-configuracio-de-vpn-amb-el-network-manager/898
- Ajustes en la resolución de DNS para la VPN: https://rfc.gisce.net/t/corregir-dns-per-les-noves-version-de-ubuntu-per-poder-utilitzar-el-dns-de-gisce/620
- Barra de "oh-my-bash" para el terminal: https://rfc.gisce.net/t/instal-lacio-de-oh-my-bash-al-terminal-dubuntu/1120
- Si la función de arrastrar y soltar ficheros no funciona bien o se experimentan problemas con `Google Meet` u otras aplicaciones: https://rfc.gisce.net/t/usar-xorg-en-lugar-de-wayland-en-ubuntu-22-04/1444
- Solució per a la "molesta" resolució de link simbolics del PyCharm Cal instal·lar els següents 2 plugins:
  - **IDEA Resolve Symlinks**: Aquest plugin fa que al clicar sobre un symlink de server/bin/addons s'obri el fitxer target directament i tanqui el symlink. Tambe t'obre el fitxer target al debugar, pero en aquest cas no el sap tancar, de totes maneres, l'stack pointer es posa sobre el fitxer target que ja es la clau!
  - **Symlink Excluder**: Aquest plugin marca com a Excluded tots els directoris de symlinks, aixo fa que no s'indexin i per tant, al buscar un fitxer, nomes s'ens mostraran a la cerca els fitxers target. S'ha acabat obrir el fitxer que no toca!
- https://rfc.gisce.net/t/plantillas-openerp-para-pycharm/234

## Material visual per a introduïr-se al sector elèctric:
- Introducción al sector eléctrico: https://www.youtube.com/watch?v=lmZwjxU0eRA
- Sistema marginal del precio de mercado de la energía: https://www.youtube.com/watch?v=rRWWirKLHAU

**[Deprecated]** El següent vídeo es pot mirar, però la informació està desfasada perquè es parla de les tarifes d'accés anteriors al canvi de Juny de 2021. És més recomanable fer una nova masterclass amb les transparències actuals.

- Master class sobre el mercado eléctrico: https://docs.google.com/presentation/d/1l-7MFZK26Hq18v28iJOdKZrQy0wKcAfP49r-nI_pQaI/edit?usp=sharing

<div data-theme-toc="true"> </div>