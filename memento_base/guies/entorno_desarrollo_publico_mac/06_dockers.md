## Instalar docker

<!-- TOC INICIO -->
  - [Instalar docker](#instalar-docker)
  - [Instalar docker](#instalar-docker)
  - [Crear usuario para administrar dockers (opcional)](#crear-usuario-para-administrar-dockers-opcional)
      - [o añadir al usuario propio al grupo docker](#o-añadir-al-usuario-propio-al-grupo-docker)
  - [Configurar postgres (con postgis y timescale)](#configurar-postgres-con-postgis-y-timescale)
    - [Añadimos PostGis de forma manual, ya que esta versión de Postgres no lo hace](#añadimos-postgis-de-forma-manual-ya-que-esta-versión-de-postgres-no-lo-hace)
      - [Change password](#change-password)
      - [Comandos utiles](#comandos-utiles)
  - [Configurar redis](#configurar-redis)
      - [Comandos utiles](#comandos-utiles)
  - [Configurar mongo](#configurar-mongo)
      - [Comandos utiles](#comandos-utiles)
  - [Instalar y configurar supervisor](#instalar-y-configurar-supervisor)
      - [Postgres](#postgres)
      - [Redis](#redis)
      - [Mongo](#mongo)
      - [Inicializar configuraciones en el supervisor](#inicializar-configuraciones-en-el-supervisor)
      - [Configuració a Pycharm per a arrancar servidors](#configuració-a-pycharm-per-a-arrancar-servidors)
<!-- TOC FIN -->

## Instalar docker

[source](https://rfc.gisce.net/t/guia-unificada-para-montar-entorno-dockerizado-postgres-redis-y-mongo-con-supervisor/1265)

```
sudo curl -sSL https://get.docker.com/ | sh
```

## Crear usuario para administrar dockers (opcional)


<details>
<summary>No necessari</summary>

```bash
# Crea usuario llamado docker-management
sudo dscl . -create /Users/docker-management
sudo dscl . -create /Users/erp

# Añade el usuario al grupo docker para poder ejecutar comandos docker...
sudo dscl . -passwd /Users/docker-management your_password_here
sudo dscl . -passwd /Users/erp your_password_here

# Create the user's home directory
sudo dscl . -create /Users/docker-management UserShell /bin/bash
sudo dscl . -create /Users/docker-management RealName "Docker Management"
sudo dscl . -create /Users/docker-management UniqueID "1001"  # Ensure this ID is unique
sudo dscl . -create /Users/docker-management PrimaryGroupID 80
sudo dscl . -create /Users/docker-management NFSHomeDirectory /Users/docker-management

sudo dscl . -create /Users/erp UserShell /bin/bash
sudo dscl . -create /Users/erp RealName "ERP"
sudo dscl . -create /Users/erp UniqueID "1002"  # Ensure this ID is unique
sudo dscl . -create /Users/erp PrimaryGroupID 80
sudo dscl . -create /Users/erp NFSHomeDirectory /Users/erp

sudo createhomedir -c -u docker-management
sudo createhomedir -c -u erp
```

#### o añadir al usuario propio al grupo docker

```bash
sudo dscl . -append /Groups/docker GroupMembership docker-management
sudo dscl . -append /Groups/docker GroupMembership erp
```

</details>


## Configurar postgres (con postgis y timescale)

> Exececutar la app de Dockers en tu Desktop

Al iniciar (docker run ...) si no encuentra `timescale` lo instalara.

```bash
# Inicializar contenedor (substituir el pasword 1234)
#docker run --name postgres -v local_psql_data:/var/lib/postgresql/data -p 127.0.0.1:5432:5432 -e POSTGRES_PASSWORD=1234 -d postgres timescale/timescaledb-ha:pg15-ts2.11-all -c password_encryption=md5
docker run --name postgres -v local_psql_data:/var/lib/postgresql/data -p 127.0.0.1:5432:5432 -e POSTGRES_PASSWORD=1234 timescale/timescaledb-ha:pg15-ts2.11-all -d postgres -c password_encryption=md5

# Crear usuario erp o el que se quiera (erp recomendado)
docker exec -it postgres createuser -U postgres -e erp -s -P
```

### Añadimos PostGis de forma manual, ya que esta versión de Postgres no lo hace

Accedemos a la shell del `postgres`
```bash
docker exec -it postgres psql -U postgres
```

Un vez dentro usamos la base de datos `template1` que es la que `destral` usa como template
```bash
\c template1
```

Le añadimos manualmente PostGis para poder trabajar con datos de `GIS`
```bash
CREATE EXTENSION postgis;
SELECT PostGIS_Full_Version();
```

* Validate
```bash
SELECT * FROM pg_available_extensions WHERE name = 'postgis';
```

* quit
```bash
\q 
```

 Por último reiniciamos el docker de postgres para guardar los cambios
```bash
docker restart postgres
```

#### Change password

```bash
docker exec -it postgres bash

psql

ALTER ROLE postgres WITH PASSWORD 'your_password';

\q

exit

docker restart postgres
```


#### Comandos utiles

```bash
# Crear base de datos de forma manual
docker exec -it postgres createdb -U erp devel_db
# Cargar dump en la nueva base de datos
zcat dump.sql.gz | docker exec -i postgres psql -U erp -d devel_db
# psql sobre DB
docker exec -it postgres psql -U erp -d devel_db
```
## Configurar redis

```bash
# Inicializar contenedor 
# (sirven tambien las versiones 4 y 5 por ejemplo redis:5.0)
docker run -p 127.0.0.1:6379:6379 --name redis30 redis:3.0
```

#### Comandos utiles

```bash
docker exec -it redis30 redis-cli
```

## Configurar mongo

```bash
docker run -p 127.0.0.1:27017:27017 --name mongo30 mongo:3.0
```

#### Comandos utiles

```bash
docker exec -it mongo30 mongo
```

## Instalar y configurar supervisor

<details>
<summary>No se com funciona</summary>

```bash
# Instalar supervisor
brew install supervisor

# check 
sudo which supervisorctl

# create a configuration file
sudo echo_supervisord_conf > /usr/local/bin/supervisord.conf

# validate
ls -l /usr/local/bin/supervisord.conf

# Start the Supervisor daemon by running
sudo supervisord -c /usr/local/bin/supervisord.conf
```

#### Postgres

```bash
# Paramos el contenedor
docker stop postgres
# Añadimos configuracion en el supervisor
sudo vim /usr/local/bin/supervisor/conf.d/postgres.conf
```
```
[program:postrgres]                                                                                                                                                                                                                      
autorestart=true 
command=docker start -i postgres
directory=/home/docker-management
redirect_stderr=true 
stdout_logfile=/home/docker-management/var/log/postgres.log
user=docker-management
```

#### Redis

```bash
# Paramos el contenedor
docker stop redis30
# Añadimos configuracion en el supervisor
sudo vim /usr/local/bin/supervisor/conf.d/redis.conf
```
```
[program:redis]                                                                                                                                                                                                                      
autorestart=true 
command=docker start -i redis30
directory=/home/docker-management
redirect_stderr=true 
stdout_logfile=/home/docker-management/var/log/redis.log
user=docker-management
```

#### Mongo
```bash
# Paramos el contenedor
docker stop mongo30
# Añadimos configuracion en el supervisor
sudo vim /usr/local/bin/supervisor/conf.d/mongo.conf
```
```
[program:mongo]                                                                                                                                                                                                                      
autorestart=true 
command=docker start -i mongo30
directory=/home/docker-management
redirect_stderr=true 
stdout_logfile=/home/docker-management/var/log/mongo.log
user=docker-management
```

#### Inicializar configuraciones en el supervisor

```bash
# Creamos el directorio var/log para el usuario docker-management
mkdir -p /home/docker-management/var/log
# Abrimos el panel de control del supervisor
sudo supervisorctl
# Releemos las configuraciones
reread
# Inicializamos/actualizamos las instancias
update
```

</details>

#### Configuració a Pycharm per a arrancar servidors

- Com que el `psql` per defecte no escolta a `localhost`, cal afegir els paràmetres següents a l'arrancar un servidor, 
- de forma anàloga a com els configurem al `destral`.

```bash
# Configurar a les variables d'entorn el següent
OPENERP_DB_HOST=localhost
OPENERP_DB_PASSWORD=<PASSWORD_POSTGRES>
OPENERP_DB_USER=<USER_POSTGRES>
```