# 04. OpenERP

<!-- TOC INICIO -->
- [04. OpenERP](#04-openerp)
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
# python@3.11.9
# libxslt1-dev not working
brew install libxslt 

brew install libpoker-eval

brew install libjpeg-dev gcc g++
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

:RE-IMPORTAR REPOS:

### Repositorios requeridos

Instalaremos los requerimientos necessarios mediante el siguiente comando:

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

...

