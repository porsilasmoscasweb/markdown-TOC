<!-- TOC INICIO -->
- [SQL](#sql)
  - [CREATE TABLE](#create-table)
  - [ALTER TABLE](#alter-table)
  - [DROP TABLE](#drop-table)
  - [TRUNCATE TABLE](#truncate-table)
  - [RENAME](#rename)
  - [ALTER COLUMN](#alter-column)
  - [DROP COLUMN](#drop-column)
  - [INSERT](#insert)
  - [UPDATE](#update)
  - [DELETE](#delete)
  - [PRODECURE](#prodecure)
    - [EXECUTE](#execute)
  - [FUNCTION](#function)
  - [TRIGGER](#trigger)
  - [VISTA](#vista)
  - [CONSTRAIN](#constrain)
    - [CHECK](#check)
    - [DROP](#drop)
  - [CASE](#case)
  - [DATE](#date)
  - [OBTENIR SCHEMA, TAULA I COLUMNES QUE LA COLUMNA CONTINGI `X`](#obtenir-schema-taula-i-columnes-que-la-columna-contingi-x)
<!-- TOC FIN -->


# SQL

## CREATE TABLE

```SQL
CREATE TABLE employees (
    employee_id integer,
    salary integer,
    manager_id integer
);
```

## ALTER TABLE

```SQL
ALTER TABLE table_name ADD COLUMN IF NOT EXISTS column_name INTEGER;
```


## DROP TABLE

```SQL
DROP TABLE IF EXISTS table_name;
```

## TRUNCATE TABLE

```SQL
TRUNCATE TABLE author_details;
```

```SQL
TRUNCATE TABLE department CASCADE;
```

```SQL
TRUNCATE TABLE employee RESTART IDENTITY;
```

## RENAME 

```sql
ALTER DATABASE table_name RENAME TO new_table_name;
```

```sql
ALTER TABLE table_name 
RENAME COLUMN column_name TO new_column_name;
```

## ALTER COLUMN

```SQL
ALTER TABLE table_name
ALTER COLUMN column_name TYPE new_data_type;
```

## DROP COLUMN

```SQL
ALTER TABLE schema_name.table_name DROP COLUMN column_name 
```

## INSERT

```SQL
INSERT INTO employees (employee_id, salary, manager_id)
VALUES (1, 1000, 2);
```

## UPDATE

```SQL
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```


## DELETE

```SQL
DELETE FROM table_name;
```

## PRODECURE

```SQL
CREATE PROCEDURE ExecuteProcedure
AS
BEGIN
    EXEC GetEmployeeDetails @EmployeeID = 123, @DepartmentID = 'Sales'
END
```

### EXECUTE

```SQL
EXEC ExecuteProcedure
```

```SQL
EXEC GetEmployeeDetails @EmployeeID = 123, @DepartmentID = 'Sales'
```

```SQL
DECLARE @OutputParam int
EXEC GetEmployeeDetails @EmployeeID = 123, @DepartmentID = 'Sales', @OutputParam OUTPUT
SELECT @OutputParam
```

```SQL
DECLARE @ReturnValue int
EXEC @ReturnValue = GetEmployeeDetails @EmployeeID = 123, @DepartmentID = 'Sales'
SELECT @ReturnValue
```

## FUNCTION

```SQL
CREATE OR REPLACE FUNCTION check_manager_salary() RETURNS TRIGGER AS $$
BEGIN
    IF NEW.salary < (SELECT salary FROM employees WHERE employee_id = NEW.manager_id) THEN
        RAISE EXCEPTION 'Salary of employee cannot be less than their manager''s salary';
    END IF;
    RETURN NEW;
END;
```

## TRIGGER

```SQL
CREATE TRIGGER check_manager_salary_trigger
BEFORE INSERT ON employees
FOR EACH ROW
EXECUTE PROCEDURE check_manager_salary();
```

## VISTA

```SQL
CREATE VIEW myview AS SELECT * FROM mytab;
```

## CONSTRAIN

### CHECK

CHECK constraints are used to ensure that values in a column or a group of columns meet a specific condition. 
They can be defined at the column level or the table level. To create a CHECK constraint, 
use the CREATE TABLE or ALTER TABLE command followed by the CHECK clause.

```SQL
CREATE TABLE table_name(
    column1 datatype,
    column2 datatype,
    CHECK (column1 > 0 AND column2 < 10)
);
```

### DROP

```SQL
ALTER TABLE table_name
DROP CONSTRAINT constraint_name;
```

## CASE 

L'expressió CASE passa per condicions i retorna un valor quan es compleix la primera condició 
(com una sentència if-then-else). Per tant, un cop una condició sigui certa, deixarà de llegir i retornarà el resultat. 
Si no hi ha condicions certes, retorna el valor de la clàusula ELSE.

Si no hi ha cap part ELSE i no hi ha condicions certes, retorna NULL.

```sql
CASE
    WHEN condition1 THEN result1
    WHEN condition2 THEN result2
    WHEN conditionN THEN resultN
    ELSE result
END;
```

## DATE

* Current day
```sql
CURRENT_DATE 
```

* Date string format
```sql
TO_DATE('2021-12-31','YYYY-MM-DD')
```

* Add days to date
```sql
CURRENT_DATE + INTERVAL '2 day'
```

## OBTENIR SCHEMA, TAULA I COLUMNES QUE LA COLUMNA CONTINGI `X` 

```SQL
SELECT table_schema, table_name, column_name
FROM information_schema.columns
WHERE column_name LIKE '%name%' ESCAPE '\'
ORDER BY table_schema, table_name;
```
