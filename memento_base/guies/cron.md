<!-- TOC INICIO -->
- [CRONS](#crons)
  - [CREAR](#crear)
  - [EXECUTAR](#executar)
  - [LOCAL from IPYTHON](#local-from-ipython)
      - [Atribut](#atribut)
    - [Validem que el cron estigui corrent](#validem-que-el-cron-estigui-corrent)
  - [COMANDAS](#comandas)
<!-- TOC FIN -->

# CRONS


## CREAR


## EXECUTAR

Ens col·loquem al servidor del client.

* Dintre el servidor
`ssh user@server`

* En l'arrel d'aquest busquem el crontab
`crontab -l | grep <cron>`

* És pot editar el crontab

```
crontab -e

~/bin/python ~/src/erp/scripts/cron/crontab_actions.py <model>.<funcio> <bbdd> <pr> <user> <pwd> <host>
```


## LOCAL from IPYTHON

```ipython
from erppeek from Client
c = Client('host', user, pwd)

# No funcionarà si el cron es una funció privada
c.model('...').cron_job
```


#### Atribut

* **cron**: nom o part d'ell que volem executar.

Copiem i executem cron.


### Validem que el cron estigui corrent

...

## COMANDAS 

Des de qualsevol directori

* `crontab -l`: List
* `crontab -e`: Edit
* `crontab -r`: Remove all
