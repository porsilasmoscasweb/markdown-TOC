<!-- TOC INICIO -->
- [08. Inicialización del entorno](#08-inicialización-del-entorno)
  - [DOCKERS](#dockers)
    - [PostgresSQLOpenERP-Server](#postgressqlopenerp-server)
    - [MongoDB + Redis en Docker](#mongodb--redis-en-docker)
    - [VALIDACIONES](#validaciones)
<!-- TOC FIN -->

# 08. Inicialización del entorno

## DOCKERS 

Instalaremos PostgreSQL [timescale+postgis],  redis y mongo 

<details>
<summary>PostgreSQL SI se instala via Docker</summary>

> [Guia RFC para Dockers](https://rfc.gisce.net/t/guia-unificada-para-montar-entorno-dockerizado-postgres-redis-y-mongo-con-supervisor/1265)


> [Guia MD](../docker.md)

</details>

<details>
<summary>PostgreSQL NO se instala via Docker</summary>

### PostgresSQLOpenERP-Server

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

### MongoDB + Redis en Docker

Si se quiere tener en el sistema directamente

```bash
sudo apt install mongodb-server redis-server
``` 

Instalamos MongoDB con:

```bash
# Instalamos requerimientos del sistema
sudo apt install \
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
sudo apt update
sudo apt install docker-ce
```

</details>

> Después de instalar con o sin DOCKERS seguimos con la instalación

Hay que instalar el servidor de MongoDB y el de Redis para poder acceder a estos, aunque sea a través de Docker.

* Instalamos Redis
```bash
sudo apt install redis-server
```

* Instalamos MongoDB
```bash
wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | sudo apt-key add -
sudo add-apt-repository 'deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/5.0 multiverse'
sudo apt update
sudo apt install -y mongodb-org
```

:warning: Si MongoDB no se instala por conflictos con la librería `libssl 1.1`
```bash
echo "deb http://security.ubuntu.com/ubuntu focal-security main" | sudo tee /etc/apt/sources.list.d/focal-security.list
sudo apt update
sudo apt install libssl1.1
```

Si redis y mongo están en ejecución en nuestra máquina se deben parar para usar los que arrancan desde Docker. Además los deshabilitamos para que no se vuelvan a encender si no lo indicamos.
```bash
sudo systemctl stop mongodb.service
sudo systemctl stop redis.service
sudo systemctl disable mongodb.service
sudo systemctl disable redis.service
```

Si se quiere que los procesos en docker arranquen automáticamente al iniciar
la sesión, se puede ejecutar lo siguiente:
```
# OPCIONAL: Arranque automático de los dockers al iniciar la sesión.
# dockers  >> ~/.profile
# Tras reiniciar la sesión se aplicarán los cambios
```
```bash
echo docker start postgres >> ~/.profile
echo docker start redis30 >> ~/.profile
echo docker start mongo30  >> ~/.profile
```

Validar que s'han crear bé
```bash
cat ~/.profile
```

Para poder ejecutar docker sin `sudo`, hay que añadir nuestro usuario al grupo `docker`:
```bash
# Tras reiniciar la sesión se aplicará el permiso
sudo groupadd docker
sudo gpasswd -a $USER docker 
```

### VALIDACIONES

* Redis
```bash
redis-cli ping
or
redis-server --version
```
