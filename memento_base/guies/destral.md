<!-- TOC INICIO -->
- [Destral](#destral)
  - [Que ès](#que-ès)
  - [Configuració "Pycharm"](#configuració-pycharm)
  - [ELEMINIAR MONGO DATABASE](#eleminiar-mongo-database)
  - [ELIMINAR PSQL DATABASE](#eliminar-psql-database)
    - [Script](#script)
      - [Attributs:](#attributs)
    - [Environment Variables](#environment-variables)
  - [ERRORS](#errors)
<!-- TOC FIN -->

# Destral

## Que ès

Destral s'utilitzar:
* Per crear un ERP desde cero a través d'un mòdul conctret. Aquest un cop només crea no actualiza.
* Per realitzar els testos de la ERP. 
* Per generar la base de dades amb dades demos.

## Configuració "Pycharm"

## ELEMINIAR MONGO DATABASE

mongo

use <database>

db.dropDatabase()

## ELIMINAR PSQL DATABASE

### Script

`/home/<usuario>/proyectos/destral/destral/cli.py`

<span style="background-color:red">`IMPORTANT`</span> 
Aquest no s'executarà si ens trobem amb una sessió oberta de la BD i la taula encara existeix.
Haurem de sortir d'aquesta i fer un `drop database <db_name>`.

`-m <model> -m <model> --no-dropdb --no-requirements`

#### Attributs:

* `--no-dropdb`: No elimina la BD.
* `--no-requirements`: No instal·la els requeriments dels mòdlus.

### Environment Variables

DESTRAL_TESTING_LANGS=[];
OORQ_ASYNC=False;
OPENERP_SRID=25831;
OPENERP_ADDONS_PATH=/home/egarriga/proyectos/erp/server/bin/addons;
OPENERP_DB_HOST=localhost;
OPENERP_DB_NAME=test_measures_distri;
OPENERP_DB_PASSWORD=1234;
OPENERP_DB_PORT=5432;
OPENERP_DB_USER=erp;
OPENERP_ESIOS_TOKEN=67c6aff80ca331eec78e1f62b7ffc6799e2674d82d57c04104a612db43496db3;
OPENERP_PRICE_ACCURACY=6;
OPENERP_REDIS_URL=redis://localhost;
OPENERP_ROOT_PATH=/home/egarriga/proyectos/erp/server/bin;
OPENERP_SECRET=lando_calrissian;
PYTHONIOENCODING=UTF-8;
PYTHONPATH=/home/egarriga/proyectos/erp/server/bin:/home/egarriga/proyectos/erp/server/bin/addons:/home/egarriga/proyectos/erp/server/sitecustomize:$PYTHONPATH;
PYTHONUNBUFFERED=1

## ERRORS

El primer que hem de fer si a l'executar el `destral` peta per connecció redis, encoding, etc ... es mira que el destral estigui el dia. 