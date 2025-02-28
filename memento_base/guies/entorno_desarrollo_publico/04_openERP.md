<!-- TOC INICIO -->
- [04. OpenERP](#04-openerp)
  - [OpenERP-Server](#openerp-server)
    - [Repositorios requeridos](#repositorios-requeridos)
  - [OpenERP-Client](#openerp-client)
<!-- TOC FIN -->

# 04. OpenERP

## OpenERP-Server

El primer repositorio que clonaremos y configuraremos será “OpenERP Server”, disponible en: https://github.com/gisce/erp

```bash
cd ~/proyectos
git clone git@github.com:gisce/erp.git
```

Para el entorno hará falta instalar los siguientes paquetes de sistema:

```bash
sudo apt install libxslt1-dev libjpeg-dev gcc g++
```

Crearemos el entorno virtual de python con:

> **NOTE**
> 
> Con -a ponemos el directorio del proyecto, lo que nos moverá al momento a la carpeta de este.

<details>
<summary>Versiones de Ubuntu superiors a la 24.04</summary>

```bash
mkvirtualenv erp -a ~/proyectos/erp -p python
```

</details>

<details>
<summary>Versiones de Ubuntu anteriores a la 24.04</summary>

```bash
mkvirtualenv erp -a ~/proyectos/erp -p python2
```

</details>

```bash
workon erp
```

* Ya desde el entorno virtual, instalamos los requerimientos básicos con:

```bash
easy_install egenix-mx-base
```

```bash
for a in vatnumber mako reportlab pydot tqdm psycopg2 Babel \
pymongo==2.9 rq==0.12 raven sentry psutil times xlwt pysftp \
redis osconf slugify fuzzywuzzy lockfile marshmallow==2.0.0b2 \
Python-Chart reportlab==3.0 osconf "libcomxml<2.2.4" \
unidecode pprintpp autoworker cython
do 
    pip install $a
done
```

:RE-IMPORTAR REPOS:

### Repositorios requeridos

Instalaremos los requerimientos necessarios mediante el siguiente comando:

* Recuerda de ir al directorio de proyectos si no estás en el!
```bash
cd ~/proyectos
```

* Instalamos
```bash
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

cat repositories | while read p b comment; do
	git clone git+ssh://git@github.com/gisce/$p.git
	(cd $p; git checkout $b )
done

ln -s poweremail poweremail2
ln -s libFacturacioATR libfacturacioatr

for a in sepa libFacturacioATR gestionatr \
switching libComXML sippers qreu enerdata arquia ooop \
distri-remesa-parser
do
    (cd $a; pip install -e .)
done
```

## OpenERP-Client

...

