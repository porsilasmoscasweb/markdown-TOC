<!-- TOC INICIO -->
- [ERP](#erp)
  - [FIELDS_GET](#fields_get)
<!-- TOC FIN -->

# ERP


## FIELDS_GET

??

> FUNCIÓ

`fields_get(cr, uid, fileds=None, context=None)`:

> ATRIBUTS

* `fields`: Lista de noms de camps.
* `context`: [opcional] diccionari de paràmetres contextuals, com ara l'usuari, el llenguatge.


> RETORNA

* Retorna un diccionari de diccionaris de camp, cadascun descrivint un camp de l'objecte de negoci.

> EXEMPLE

```
class idea(osv.osv):
    (...)
    
    _columns = {
            'name' : fields.char('Name',size=64)
            (...)
        }

    def test_fields_get(self,cr,uid):
        assert(self.fields_get('name')['size'] == 64)
```
