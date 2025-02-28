# BACKUP

<!-- TOC INICIO -->
- [BACKUP](#backup)
- [BACKUP](#backup)
  - [DB](#db)
    - [Inicialitzar una BD en mode "devel"](#inicialitzar-una-bd-en-mode-devel)
  - [DUPLICATE DBB](#duplicate-dbb)
  - [ERRORS](#errors)
<!-- TOC FIN -->

# BACKUP

## DB

Per descarregar un backup diàri de un servidor de Client.

> La copia estarà de normal a la carpeta /home/erp/var/backups o /home/erp/backupdir

* Ens col·loquem com a usuaris `erp`

```bash
sudo su - erp
```

* Instal·lar ssh servidor en local

```bash
ssh -V

sudo apt install ssh

sudo systemctl status ssh.service

sudo systemctl start ssh.service
```

* Descarregar de forma segura

```bash
# Des de la màquina del Client
scp backupdir/PeusaMaster-20241126000102.sql.xz egarriga@10.246.5.102:/tmp
```

OR

```bash
# Des de la propia màquina
cd ~/tmp
scp gisce@10.246.0.234:/home/erp/backupdir/PeusaMaster-20241202000101.sql.xz .
```

* Copia fitxer a una carpeta per la permenencia del document

```sql
cp PeusaMaster-20241126000102.sql.xz /home/egarriga/Desktop/PeusaMaster-20241126000102.sql.xz
```

* Crear una BDD nova 

```bash
psql -h localhost -U erp -d test_db
```

```psql
CREATE DATABASE mydatabase;

\l
```

* Importar el fitxer

[RFC](https://rfc.gisce.net/t/backups-potgres-timescaledb/1430)

```bash
xzcat /absolute_path/backups.sql.xz | psql -h localhost -U erp -d mydatabase
```

### Inicialitzar una BD en mode "devel"

Un cop importar s'ha de realitzar una serie de Tasques.

[RFC](https://rfc.gisce.net/t/inicialitzar-una-bd-en-mode-devel/183)

* Renombrar el nom de la BD a un sufix, com per exemple: `_test` o `_dev` o `_pre`

* Desactivar crons

```sql
-- desativa els crons
update ir_cron set active=false;

-- tots els mails dels casos CRM que no s'enviin
update crm_case set email_from = 'egarriga@gisce.net';

-- tots els mails a elteuemail@gisce.net
update res_partner_address set email = 'egarriga@gisce.net';
```

* Actualitzar poweremail

```sql
update poweremail_core_accounts set
    smtpport='1234',
    smtpserver='smtp.fake.com';
    
update poweremail_mailbox set
    pem_to='egarriga@gisce.net',
    pem_cc='egarriga@gisce.net',
    pem_bcc='egarriga@gisce.net';
```

* Actualitzar l'accés dels usuaris amb un password genéric

```sql
update res_users set password='1234' where login!='gisce';
```

* Canviar la IP de `giscegis_gis_url` a localhost

```sql
update res_config set name='http://localhost' where name = 'giscegis_gis_url';
```

* Actualizar el configuració del ERP `erp.conf` i acabar de configurar la base de dades.

## DUPLICATE DBB

```sql
REVOKE CONNECT ON DATABASE test_peusa FROM PUBLIC, erp;
```

```psql
CREATE DATABASE new_database_name 
WITH TEMPLATE original_database_name 
OWNER username;
```

* Reemplaza:
  * `new_database_name`: el nombre de la nueva base de datos que deseas crear.
  * `original_database_name`: el nombre de la base de datos existente que deseas duplicar.
  * `username`: el nombre del usuario que será el propietario de la nueva base de datos.


## ERRORS

* column "restrict_actions" does not exist:
  * --update=base or --run-scripts=base 
    * Comentar script de migració server/bin/addons/base/migrations/5.0.24.5.0/post-0003_update_report_view.py


