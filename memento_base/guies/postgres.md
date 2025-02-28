<!-- TOC INICIO -->
- [POSTGRES](#postgres)
  - [PostgreSQL commands](#postgresql-commands)
  - [CANVIAR i VALIDAR Timezone](#canviar-i-validar-timezone)
  - [CANVIAR NOM DBB](#canviar-nom-dbb)
  - [CHECK FOR USER OWNER DBB](#check-for-user-owner-dbb)
  - [REVOKE connections](#revoke-connections)
  - [DROP CONNECTION](#drop-connection)
  - [DUPLICATE DBB](#duplicate-dbb)
      - [Consideraciones importantes](#consideraciones-importantes)
  - [Terminate Connections](#terminate-connections)
  - [Roles](#roles)
  - [Managing databases](#managing-databases)
  - [SET VARIABLE](#set-variable)
  - [Managing tables](#managing-tables)
  - [Managing views](#managing-views)
  - [Managing indexes](#managing-indexes)
  - [Querying data from tables (SELECT)](#querying-data-from-tables-select)
    - [Join](#join)
  - [Set operations](#set-operations)
  - [Modifying data](#modifying-data)
  - [Truncate](#truncate)
  - [Performance](#performance)
  - [Collect statistics:](#collect-statistics)
- [DROP ALL DATABASES](#drop-all-databases)
- [WITH (readable query's)](#with-readable-querys)
<!-- TOC FIN -->

# POSTGRES

## PostgreSQL commands

* See version
```sql
SELECT version();
```

## CANVIAR i VALIDAR Timezone 

* Mostrar Timezone
```sql
SHOW TIMEZONE;
```

* Canviar Timezone
```sql
ALTER DATABASE [database] SET TIMEZONE TO 'Europe/Madrid';
```

* Obrint un nou psql i validem de nou

## CANVIAR NOM DBB

```sql
ALTER DATABASE old_db RENAME TO new_db;
```

## CHECK FOR USER OWNER DBB

```sql
SELECT d.datname, u.usename AS owner
FROM pg_database d
JOIN pg_user u ON d.datdba = u.usesysid;
```


## REVOKE connections

```sql
REVOKE CONNECT ON DATABASE test_peusa FROM PUBLIC, erp;
```

## DROP CONNECTION

When error `There is 1 other session using the database`

```sql
# Selecionem la taula que esta bloquejada  
SELECT pg_terminate_backend(pg_stat_activity.pid)
FROM pg_stat_activity
WHERE pg_stat_activity.datname = '$table$';

# Eliminem la taula
DROP DATABASE $table$;
```

## DUPLICATE DBB

```psql
CREATE DATABASE new_database_name 
WITH TEMPLATE original_database_name 
OWNER username;
```

* Reemplaza:
  * `new_database_name`: el nombre de la nueva base de datos que deseas crear.
  * `original_database_name`: el nombre de la base de datos existente que deseas duplicar.
  * `username`: el nombre del usuario que será el propietario de la nueva base de datos.

#### Consideraciones importantes

* Asegúrate de que el usuario que ejecuta el comando tenga permisos para crear bases de datos y acceder a la base de datos original.
* Si la base de datos original está siendo utilizada por otros usuarios, es posible que debas terminar las conexiones abiertas antes 
de duplicar la base de datos. Puedes hacerlo utilizando el siguiente comando:

```psql
SELECT pg_terminate_backend(pg_stat_activity.pid)
FROM pg_stat_activity
WHERE pg_stat_activity.datname = 'original_database_name'
AND pid != pg_backend_pid();
```


## Terminate Connections

> There are * other sessions using the database.

* Execute the following query from on PostgreSQL to terminate all active connections. 

```sql
SELECT 
    pg_terminate_backend(pid) 
FROM 
    pg_stat_activity 
WHERE 
    -- don't kill my own connection!
    pid <> pg_backend_pid()
    -- don't kill the connections to other databases
    AND datname = <dbname>;
```

## Roles

* Create a new role:
`CREATE ROLE role_name;`

* Create a new role with a username and password:
CREATE ROLE username NOINHERIT LOGIN PASSWORD password;`

* Change the role for the current session to the new_role:
`SET ROLE new_role;`

* Allow role_1 to set its role as role_2:
GRANT role_2 TO role_1;`


## Managing databases

* Create a new database:
`CREATE DATABASE [IF NOT EXISTS] db_name;`

* Delete a database permanently:
`DROP DATABASE [IF EXISTS] db_name;`


## SET VARIABLE

* Set var harcode

```sql
-- Declare
@set id = 35

-- Use
select * from [table] where id = ${id};
or
select * from [table] where id = :id;
```

* Set var from `select`

```sql
-- Declare
@set id = (select id from [table] where id = 1)

-- Use
select * from [table] where id = :idd;
```

## Managing tables

* Create a new table or a temporary table
```
CREATE [TEMP] TABLE [IF NOT EXISTS] <table_name>(
    pk SERIAL PRIMARY KEY,
    c1 type(size) NOT NULL,
    c2 type(size) NULL,
    ...
);
```

* Add a new column to a table:
` ALTER TABLE table_name ADD COLUMN new_column_name TYPE; `

* Drop a column in a table:
```
ALTER TABLE table_name 
DROP COLUMN column_name;
```
* Rename a column:
```
ALTER TABLE table_name 
RENAME column_name TO new_column_name;
```
* Set or remove a default value for a column:
```
ALTER TABLE table_name 
ALTER COLUMN [SET DEFAULT value | DROP DEFAULT]
```
* Add a primary key to a table.
```
ALTER TABLE table_name 
ADD PRIMARY KEY (column,...);
```
* Remove the primary key from a table.
```A
LTER TABLE table_name 
DROP CONSTRAINT primary_key_constraint_name;
```
* Rename a table.
```
ALTER TABLE table_name 
RENAME TO new_table_name;
```
* Drop a table and its dependent objects:
`DROP TABLE [IF EXISTS] table_name CASCADE;`
`DROP TABLE [IF EXISTS] table_1, table_2, etc...;`

## Managing views

* Create a view:
`CREATE OR REPLACE view_name AS query;`

* Create a recursive view:
```
CREATE RECURSIVE VIEW view_name(column_list) AS
SELECT column_list;
```

* Create a materialized view:
```
CREATE MATERIALIZED VIEW view_name
AS
query
WITH [NO] DATA;
```

* Refresh a materialized view:
`REFRESH MATERIALIZED VIEW CONCURRENTLY view_name;`

* Drop a view:
`DROP VIEW [ IF EXISTS ] view_name;`

* Drop a materialized view:
```
DROP MATERIALIZED VIEW view_name;
```

* Rename a view:
```
ALTER VIEW view_name RENAME TO new_name;
```

## Managing indexes

* Creating an index with the specified name on a table
```
CREATE [UNIQUE] INDEX index_name
ON table (column,...)
```

* Removing a specified index from a table
```
DROP INDEX index_name;
```

## Querying data from tables (SELECT)

* Query all data from a table:
```
SELECT * FROM table_name;
```

* Query data from specified columns of all rows in a table:
```
SELECT column_list
FROM table;
```

* Query data and select unique rows:
```
SELECT DISTINCT (column)
FROM table;
```
* Query data from a table with a filter:
```
SELECT *
FROM table
WHERE condition;
`````
* Assign an alias to a column in the result set:
```
SELECT column_1 AS new_column_1, ...
FROM table;
```
* Query data using the LIKE operator:
```
SELECT * FROM table_name
WHERE column LIKE '%value%'
````
* Query data using the BETWEEN operator:
```
SELECT * FROM table_name
WHERE column BETWEEN low AND high;
```
* Query data using the IN operator:
```
SELECT * 
FROM table_name
WHERE column IN (value1, value2,...);
````
* Constrain the returned rows with the LIMIT clause and OFFSET from where id to start:
```
SELECT * 
FROM table_name
LIMIT limit OFFSET offset
ORDER BY column_name;
```

* Return the number of rows of a table:
```
SELECT COUNT (*)
FROM table_name;
`````

* Sort rows in ascending or descending order:
```
SELECT select_list
FROM table
ORDER BY column ASC [DESC], column2 ASC [DESC],...;
````

* Group rows using GROUP BY clause.
```
SELECT *
FROM table
GROUP BY column_1, column_2, ...;
````

* Filter groups using the HAVING clause.
  * the WHERE clause cannot be used with aggregate functions.
  * :warning: **HAVING filtra después de agrupar los datos.**
```
SELECT *
FROM table
GROUP BY column_1
HAVING condition;
````

* The EXISTS operator is used to test for the existence of any record in a sub query.
    * The EXISTS operator returns TRUE if the sub query returns one or more records.
      * Return all customers that is `NOT` represented in the orders table:
```
SELECT customers.customer_name
FROM customers
WHERE EXISTS (
  SELECT order_id
  FROM orders
  WHERE customer_id = customers.customer_id
);
```

* The ANY operator allows you to perform a comparison between a single column value and a range of other values.

The ANY operator:
* returns a Boolean value as a result
* returns TRUE if ANY of the sub query values meet the condition
ANY means that the condition will be true if the operation is true for any of the values in the range.

```
SELECT product_name
FROM products
WHERE product_id = ANY (
  SELECT product_id
  FROM order_details
  WHERE quantity > 120
);
```

* The ALL operator:
  * returns a Boolean value as a result 
  * returns TRUE if ALL of the sub query values meet the condition 
  * is used with SELECT, WHERE and HAVING statements
ALL means that the condition will be true only if the operation is true for all values in the range.
```
SELECT product_name
FROM products
WHERE product_id = ALL (
  SELECT product_id
  FROM order_details
  WHERE quantity > 10
);
```

* The CASE expression goes through conditions and returns a value when the first condition is met (like an if-then-else statement).
Once a condition is true, it will stop reading and return the result. If no conditions are true, it returns the value in the ELSE clause.
If there is no ELSE part and no conditions are true, it returns NULL.

```
SELECT product_name,
CASE
  WHEN price < 10 THEN 'Low price product'
  WHEN price > 50 THEN 'High price product'
ELSE
  'Normal product'
END
FROM products;
```

* Get de values from `interval` od date. 

```sql
SELECT * FROM table 
WHERE timestamp_column > (NOW() - INTERVAL '1 HOUR');
```

### Join

* `INNER JOIN`: Returns records that have matching values in both tables
* `LEFT JOIN`: Returns all records from the left table, and the matched records from the right table
* `RIGHT JOIN`: Returns all records from the right table, and the matched records from the left table
* `FULL JOIN`: Returns all records when there is a match in either left or right table
* `CROSS JOIN`: keyword matches ALL records from the "left" table with EACH record from the "right" table.
That means that all records from the "right" table will be returned for each record in the "left" table.
This way of joining can potentially return very large table, and you should not use it if you do not have to.

* Query data from multiple using the inner join, left join, full outer join, cross join and natural join:
```
SELECT * 
FROM table1
INNER JOIN table2 ON conditions

SELECT * 
FROM table1
LEFT JOIN table2 ON conditions

SELECT * 
FROM table1
FULL OUTER JOIN table2 ON conditions

SELECT * 
FROM table1
CROSS JOIN table2;

SELECT * 
FROM table1
NATURAL JOIN table2;
````

## Set operations

* Combine the result set of two or more queries with UNION operator:
  * Use UNION ALL to return duplicate values.
```
SELECT * FROM table1
UNION
SELECT * FROM table2;
```

* Minus a result set using EXCEPT operator:
```
SELECT * FROM table1
EXCEPT
SELECT * FROM table2;
````

* Get the intersection of the result sets of two queries:
```
SELECT * FROM table1
INTERSECT
SELECT * FROM table2;
```

## Modifying data

* Insert a new row into a table:
```
INSERT INTO table(column1,column2,...)
VALUES(value_1,value_2,...);
````

* Insert multiple rows into a table:
```
INSERT INTO table_name(column1,column2,...)
VALUES(value_1,value_2,...),
      (value_1,value_2,...),
      (value_1,value_2,...),
      ...;
```

* Update data for all rows:
```
UPDATE table_name
SET column_1 = value_1, ...;
````

* Update data for a set of rows specified by a condition in the WHERE clause.
```
UPDATE table
SET column_1 = value_1,
    ...
WHERE condition;
```

* Delete all rows of a table:
```
DELETE FROM table_name;
````

* Delete specific rows based on a condition:
```
DELETE FROM table_name
WHERE condition;
```

## Truncate

* reset table to init.
```
truncate <table>;

// Get de sequence of table
SELECT * FROM <table>_<id>_seq;

// Reset to what you prefer
ALTER SEQUENCE <table>_<id>_seq RESTART WITH <resset (integer: Ex.1)>;
```

## Performance

* Show the query plan for a query:
```
EXPLAIN query;
````

* Show and execute the query plan for a query:
```
EXPLAIN ANALYZE query;
```

## Collect statistics:
`ANALYZE table_name;`


# DROP ALL DATABASES

* loop:
BEGIN 
   FOR i IN 1..25 LOOP
      INSERT INTO playtime.meta_random_sample
         (col_i, col_id)
      SELECT  i, id
      FROM   tbl
      ORDER  BY random()
      LIMIT  15000;
   END LOOP;
END

* List datname:
SELECT datname, 
  pid, 
  usename, 
  application_name, 
  client_addr, 
  client_port
FROM pg_stat_activity 
WHERE datname not in ('postgres', 'test_db', 'test_sys_controller');


# WITH (readable query's)

Amb la comanda `with` crearem queries encapsulades per tal de fer més llegible el codi, i crear unions com selects anidades

un exemple seria el següent:

```sql
--- Query highlights users that have over 50% of tasks on a given project
--- Gives comma separated list of their tasks and the project


--- Initial query to grab project title and tasks per user
WITH users_tasks AS (
  SELECT 
         users.id as user_id,
         users.email,
         array_agg(tasks.name) as task_list,
         projects.title
  FROM
       users,
       tasks,
       project
  WHERE
        users.id = tasks.user_id
        projects.title = tasks.project_id
  GROUP BY
           users.email,
           projects.title
),

--- Calculates the total tasks per each project
total_tasks_per_project AS (
  SELECT 
         project_id,
         count(*) as task_count
  FROM tasks
  GROUP BY project_id
),

--- Calculates the projects per each user
tasks_per_project_per_user AS (
  SELECT 
         user_id,
         project_id,
         count(*) as task_count
  FROM tasks
  GROUP BY user_id, project_id
),

--- Gets user ids that have over 50% of tasks assigned
overloaded_users AS (
  SELECT tasks_per_project_per_user.user_id,

  FROM tasks_per_project_per_user,
       total_tasks_per_project
  WHERE tasks_per_project_per_user.task_count > (total_tasks_per_project / 2)
)

--- Get needed fields
SELECT 
       email,
       task_list,
       title
FROM 
     users_tasks,
     overloaded_users
WHERE
      users_tasks.user_id = overloaded_users.user_id
```