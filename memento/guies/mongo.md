<!-- TOC INICIO -->
- [MONGO](#mongo)
  - [ACCESS ON SERVER](#access-on-server)
  - [COMMANDS](#commands)
  - [ELEMINIAR MONGO DATABASE](#eleminiar-mongo-database)
  - [ELEMINIAR MULTIPLES MONGO DATABASE](#eleminiar-multiples-mongo-database)
    - [Creem fitxer `.js` amb la funcionalitat que obtindrà els nom de totes les `dbs` i les eleminarà.](#creem-fitxer-js-amb-la-funcionalitat-que-obtindrà-els-nom-de-totes-les-dbs-i-les-eleminarà)
<!-- TOC FIN -->

# MONGO

> [WIKI](https://www.mongodb.com/docs/manual/reference/command/)

## ACCESS ON SERVER

cat /etc/hosts
ssh {mongo}
show databases
use db
show collections


## COMMANDS

* Llistar BBDD
`show dbs`

* utilitzar una BD
`use <database_name>`

* drop database
```
use <database_name>
db.dropDatabase()

# Result
{ "dropped" : "<database_name>", "ok" : 1 }
```


* Llistar collection _(taules)_ de la SCHEMA
`show collections`

* select
`db.<collection>.find()`
`db.<collection>.findOne()`
`db.<collection>.find().pretty()`

* select specify column
`db.<collection>.find({'ai': {'$gt': '<integer>}}, {id: 1'})`

* count
`
db.<collection>.count()
db.<collection>.find().count()
`

* where
`db.<collection>.find({'key': 'value'})`

* projection. * del select de SQL
`db.<collection>.find({'name': '00000002', 'ae': {'$gt': 0}}, {'name': 1, 'ae':1})`

* create
`db.createCollection(<name_collection>)`

* insert
`db.<collection>.insert({ key: value, key: value, ... })`

* update One
`db.<collection>.updateOne({_id: ...}, {$set: {'name': 'ZIV0202012290'}})`

* update Many
`db.<collection>.updateMany({}, {$set: {'name': 'ZIV0202012290'}})`

* truncate
`db.<collection>.remove({})`

* drop
`db.<collection>.drop()`


## ELEMINIAR MONGO DATABASE

mongo

use <database>

db.dropDatabase()

## ELEMINIAR MULTIPLES MONGO DATABASE

### Creem fitxer `.js` amb la funcionalitat que obtindrà els nom de totes les `dbs` i les eleminarà.

> Fitxer `mongo_dropall.js`

```
var dbs = db.getMongo().getDBNames();

for(var i in dbs){
    db = db.getMongo().getDB( dbs[i] );
    if(db.getName() != 'test' && db.getName() != 'local') {
        print( "dropping db " + db.getName() );
        db.dropDatabase();
    }
}
```

> Mongo

```
load("/home/egarriga/Documents/memento/mongo_dropall.js")
```