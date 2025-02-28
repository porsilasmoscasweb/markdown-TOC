<!-- TOC INICIO -->
- [DOCKERS](#dockers)
  - [Instalar docker](#instalar-docker)
  - [Configurar postgres (con postgis y timescale)](#configurar-postgres-con-postgis-y-timescale)
  - [Configurar redis](#configurar-redis)
  - [Configurar mongo](#configurar-mongo)
  - [Instalar y configurar supervisor](#instalar-y-configurar-supervisor)
    - [Paramos contenedores](#paramos-contenedores)
      - [Postgres](#postgres)
      - [Redis](#redis)
      - [Mongo](#mongo)
    - [Inicializar configuraciones en el supervisor](#inicializar-configuraciones-en-el-supervisor)
    - [Configuració a Pycharm per a arrancar servidors](#configuració-a-pycharm-per-a-arrancar-servidors)
  - [IMPORTAR I EXPORTAR](#importar-i-exportar)
<!-- TOC FIN -->

# DOCKERS

## Instalar docker
```
sudo curl -sSL https://get.docker.com/ | sh
```

<details>
<summary>[OPCIONAL] Crear usuario para administrar dockers (opcional)</summary>

* Crea usuario llamado docker-management
```bash
sudo useradd -m docker-management
```

* Añade el usuario al grupo docker para poder ejecutar comandos docker...
```bash
sudo gpasswd -a docker-management docker
```

* Cambiamos del usuario actual al de docker-management
```bash
sudo su - docker-management
```

```bash
bash
```

</details> 

* Añadir al usuario propio al grupo docker
```bash
sudo gpasswd -a usuario docker
```

## Configurar postgres (con postgis y timescale)

* Inicializar contenedor (substituir el pasword ******)
```bash
docker run --name postgres -p 127.0.0.1:5432:5432 -e POSTGRES_PASSWORD=********* -v ${PWD}/data:/var/lib/postgresql/data timescale/timescaledb-ha:pg15-ts2.11-all -c password_encryption=md5
````

> Es posible que se quede parado. Si es así. Ceramos y volmemos abrir
> ```bash
> docker start postgres
> ```

* Crear usuario erp o el que se quiera (erp recomendado) substituir el nom de l'usuari ******
```bash
docker exec -it postgres createuser -U postgres -e ******* -s -P
```

* [OPCIONAL] Crear base de datos de forma manual substituir el nom de l'usuari ****** i nom de la BDD
```bash
docker exec -it postgres createdb -U ******* -d *******
```

* Executar
```bash
psql -h localhost -U **** -d ****
```
  
* Añadir PostGis a la \d template1(Aquesta BDD es de la que parteixen totes les creacion noves de BDD per això té que tenir el PostGis)
```bash
CREATE EXTENSION postgis;
SELECT PostGIS_Full_Version();
SELECT * FROM pg_available_extensions WHERE name = 'postgis';
```

* Restart postgres
```bash
dockers restart postgres
```

* Cargar dump en la nueva base de datos **_(Si tenemos el fichero)_**
```bash
zcat dump.sql.gz | docker exec -i postgres psql -U ******* -d *******
```

<details>
<summary>Comandos utiles</summary>

* Executar
  * psql sobre DB -U **** [erp] -d **** [postgres]
```bash
docker exec -it postgres psql -U ******* -d *******
```

* Listamos tabla
```bash
\l
```

* Salimos
```bash
exit
```

</details>

## Configurar redis

* Inicializar contenedor  (sirven tambien las versiones 4 y 5 por ejemplo redis:5.0)
```bash
docker run -p 127.0.0.1:6379:6379 --name redis30 redis:3.0
```

> Es posible que se quede parado. Si es así. Ceramos y volmemos abrir
> ```bash
> docker start redis30
> ```

<details>
<summary>Comandos utiles</summary>

* Executar
```bash
docker exec -it redis30 redis-cli
```

* Salimos
```bash
exit
```

</details>

## Configurar mongo

```bash
docker run -p 127.0.0.1:27017:27017 --name mongo30 mongo:3.0
```

> Es posible que se quede parado. Si es así. Ceramos y volmemos abrir
> ```bash
> docker start mongo30
> ```

<details>
<summary>Comandos utiles</summary>

* Executar
```bash
docker exec -it mongo30 mongo
```

* Salimos
```bash
exit
```

</details>

## Instalar y configurar supervisor

* Instalar supervisor
```bash
sudo apt install supervisor
```

### Paramos contenedores

* Listamos contenedores
```bash
sudo docker ps
```

* Paramos contenedores
```bash
sudo docker stop postgres redis30 mongo30
```

#### Postgres

* Añadimos configuracion en el supervisor
```bash
sudo vim /etc/supervisor/conf.d/postgres.conf
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

* Añadimos configuracion en el supervisor
```bash
sudo vim /etc/supervisor/conf.d/redis.conf
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

* Añadimos configuracion en el supervisor
```bash
sudo vim /etc/supervisor/conf.d/mongo.conf
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

### Inicializar configuraciones en el supervisor

* Creamos el directorio var/log para el usuario docker-management
```bash
sudo mkdir -p /home/docker-management/var/log
```

* Abrimos el panel de control del supervisor
```bash
sudo supervisorctl
```

* Releemos las configuraciones
```bash
reread
```

* Inicializamos/actualizamos las instancias
```bash
update
```

### Configuració a Pycharm per a arrancar servidors

Com que el `psql` per defecte no escolta a `localhost`, cal afegir els paràmetres següents a l'arrancar un servidor, de forma anàloga a com els configurem al `destral`.

* Configurar a les variables d'entorn el següent:

```bash
OPENERP_DB_HOST=localhost
OPENERP_DB_PASSWORD=<PASSWORD_POSTGRES>
OPENERP_DB_USER=<USER_POSTGRES>
OPENERP_DB_PORT=<PORT_POSTGRES>
```

<details>
<summary>COMMANDS</summary>

> [DOC](https://www.ionos.es/digitalguide/servidores/know-how/comandos-de-docker/)

* mostrar información de Docker
```bash
docker info
```

* mostrar imágenes de Docker en el host
```bash
docker images
```

* Executar
```bash
docker exec -it [image] [host]
```

* Start
```bash
docker start [image]
```

* Stop
```bash
docker stop [image]
```

</details>


## IMPORTAR I EXPORTAR

> [EXPORT](https://docs.docker.com/reference/cli/docker/container/export/)
> [IMPORT](https://stackoverflow.com/questions/40582300/how-to-load-a-docker-image-from-a-tar-file)

* Llistem els dokers que tenim
`docker ps`

* Exportar
`docker export <container_id> > /path/name.tar`

* Moure el fitxer a la màquina nova

* Importar
`docker load /path/name.tar`
