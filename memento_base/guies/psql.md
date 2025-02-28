<!-- TOC INICIO -->
- [PSQL](#psql)
  - [Que és?](#que-és)
  - [Accés per consola de comandes](#accés-per-consola-de-comandes)
  - [CONNECT FROM SERVER](#connect-from-server)
  - [PSQL commands](#psql-commands)
<!-- TOC FIN -->

# PSQL

## Que és?

> [WIKI](https://ayuda.guebs.com/usar-psql-conectar-base-datos-postgresql/)

psql és una comanda que ens permet accedir mitjançant una consola de comandes a la base de dades de POSTGRES per fer les gestions oportunes. 

És necessari conectar-se via SSH.

## Accés per consola de comandes

`psql -h localhost -U erp -d test_db`

> * `-h`: Host de on executaras les comandes.
> * `-U`: Usuari de la BD.
> * `-d`: Nom de la BD.

## CONNECT FROM SERVER

* Llistem hosts
`cat /etc/hosts`

* Accés a Servidors. Entrem a la shell del servidor on esta allotjada la BDD
`ssh sql`

* Ens logajem com a usuari postgres
`sudo su - postgres`

* Accés a psql
`psql`

* Llistem bbdd
`\l`

* Ens col·loquem a la que ens interesa
`psql db_name`


## PSQL commands

* List ports
`
sudo lsof -i -P -n
or
sudo lsof -i -P -n | grep LISTEN
or 
lsof -i:8080
`

* Info of specific port
`netstat -putona | grep <port>`

* Kill port LISTEN
`
kill $(lsof -t -i:<port>)
or
kill -9 $(lsof -t -i:<port>)
`

* Access the PostgreSQL server from psql with a specific user:
`psql -U [username];`

* Connect to a specific database:
`\c database_name`

* List of installed extensions:
`\dx`

* To quit the psql:
`\q`

* List all databases in the PostgreSQL database server
`\l`

* List all schemas:
`\dn`

* List all stored procedures and functions:
`\df`

* List all views:
`\dv`

* List all views `MATERIALIZED`:
`\dm`

* Lists all tables in a current database.
`\dt`

* Or to get more information on tables in the current database:
`\dt+`

* Get detailed information on a table.
`\d+ table_name`

* Show a stored procedure or function code:
`\df+ function_name`

* Show query output in the pretty format:
`\x` [on|off|auto]
 
* Remove query output in the pretty format:
`\x off` [on|off|auto]

* List all users:
`\du`
