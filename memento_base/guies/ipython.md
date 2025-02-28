<!-- TOC INICIO -->
- [IPYTHON](#ipython)
  - [HELP _(?)_](#help-__)
    - [SHOW CODE _(??)_](#show-code-__)
    - [???? _(%)_](#-__)
    - [COMMANDS](#commands)
    - [ALIAS](#alias)
  - [CONNECTAR AL SERVIDOR](#connectar-al-servidor)
      - [Estructura Attributs](#estructura-attributs)
  - [CREAR INSTANCIA DE MODEL _(obj)_](#crear-instancia-de-model-_obj_)
  - [MOSTRAR COLUMNS D'UN MODEL](#mostrar-columns-dun-model)
<!-- TOC FIN -->

# IPYTHON

## HELP _(?)_

Mostrar informació sobre variables, funcions, etc...

Acabar amb interrogat. <whatever>?

### SHOW CODE _(??)_

Mostrar informació i codi d'una variable, funció, etc ...

Acabar amb doble interrogant. <whatever>??


### ???? _(%)_

```python
def super_task():
    import time
    time.sleep(1)
    print("hello world !")
```

```python
%time super_task()
```

### COMMANDS

* reset
`%reset`

* execute file
`%run <file.py>`

* edit file
`%edit <file.py>`


* append code to file
`%load <file.py>`

> print("Hello world.")

`python
print(" My name is ...")
`

> Hello world. My name is ...

### ALIAS

* alias
`%alias`

* ls
`%ls`

* make directory
`%mkdir <dir>`


## CONNECTAR AL SERVIDOR

```python
ipython

from erppeek import Client
# Port:client User:client PWD:client
c = Client('http://localhost:8069', 'db_name', 'user', 'pwd')

# Creem instancia del model que volem útilitzar
md = c.model('<module>') or c.ModuleName

# Ja podem útilitzar les funcions del mòdul `Class`
md._fnct()

# Mostrar structure objecte
type(md)
...
```

#### Estructura Attributs

* `type(md)`: Returns the name of the class that implements the object.
* `dir(md)`: Returns all methods and variables of the object.
* `id(md)`: Returns the unique identified of the object (memory address).
* `hasattr(md, name)`: Checks if an attribute belongs to an object.
* `getattr(md, name, default)`: Gets an attribute that may belong to an object.
* `callable(md)`: Checks if an object is callable, that is, it can be called.


## CREAR INSTANCIA DE MODEL _(obj)_

```
task_obj = c.model('project.task')
task_obj.search([('case_id', '=', False)])
```

> (output) > [4, 1, 2, 3, 5, 25, 6, 26, 7, 8, 27, 9, 10, 11, 12, 13, 14, 18, 15, 16, 17, 19, 20, 21, 22, 23]

## MOSTRAR COLUMNS D'UN MODEL

```
# Camp + Type
c.model().fields_get()[]
or

# Camp Name
c.model().keys()
```

> (output) > {{'name': 'type'}, ...}
> 
> (output) > ['name', ...]