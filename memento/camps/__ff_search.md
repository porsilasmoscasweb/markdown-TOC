<!-- TOC INICIO -->
- [MDDEL DE DADES](#mddel-de-dades)
  - [SEARCH EN CAMP FUNCIÓ](#search-en-camp-funció)
    - [Atributs](#atributs)
  - [DEBUG](#debug)
<!-- TOC FIN -->

# MDDEL DE DADES

## SEARCH EN CAMP FUNCIÓ

En un camp funció que és un camp calculat, si aquest té la opció de search el la vista del llistat per exemple haurem d'implementar-la.

Per fer-ho ho farem de la següent manera:

* `select="1"`: En la vista `.xml`
* `fnct_search=`: Dintre el fields.function().
  * Aquesta serà l'encarregada de convertir el filtre perque l'ORM sigui capaç d'interpretar-lo.

> EXEMPLE
> 
> Si volem obtenir el comptadors que estan online tindrem que accedir els Registredors i el camp `is_online` que d'aquest que és troba el Redis.
> 
> Com que el camp no esta es calcula el vol obtindrem tots els comptadors i d'aquest els seus Registrados. D'aquest obtindrem els que estan online
> i els filtrerem per `args` que ens arriba per paramentre. Un com finalitzat el filtre retornarem el resultat en forma de filtre (tuple)

```python
def _ff_search_is_online(self, cursor, uid, obj, name, args, context=None):
    if context is None:
        context = {}

    _monitor_obj = self.pool.get('giscemisc.monitor')
    reg_obj = self.pool.get('giscedata.registrador')

    res_ids = []
    comp_ids = obj.search(cursor, uid, [], context=context)

    for comptador_data in self.read(cursor, uid, comp_ids, ['registrador_id'], context=context):
        comp_id = comptador_data['id']

        if comptador_data['registrador_id']:
            reg_id = comptador_data['registrador_id'][0]
            reg_data = reg_obj.read(cursor, uid, reg_id, ['tm_ip_address', 'tm_port'], context=context)
            if reg_data:
                is_online, last_heartbeat = _monitor_obj.is_up(
                    cursor, uid, reg_data['tm_ip_address'], port=reg_data['tm_port'], context=context)

                if is_online == args[0][2]:
                    res_ids.append(comp_id)

    return [('id', 'in', res_ids)]

_columns = {
    'registrador_id': fields.function(_ff_search_is_online, store=True, string="...", type="int")
}
```

### Atributs

* `store`: aquest camp te com a valors
  * `True`: Es guardarà a la BDD
  * `False`: No es guardarà a la BDD
  * `function`: La funció crearà un trigger a BDD per que cada camp que s'actualitzi un dels camp definit o tots en cas de buit
  pel que tenim que retorna els ids de la taula que s'haurà d'actualitzar.
    * En la mateixa taula seran els mateix ids. Així que amb un lambda es pot fer
    * En un taula foranea haurem d'obtenir els ids associats. Com podria ser `registradors_ids, task_ids, etc ...` 
  
```python
_columns = {
    'remaining_to_deadline': fields.function(_ff_search_is_online, type='boolean', method=True, size=6, string=_('is_td_ready'), 
                                      store={'crm.case': (lambda self, cr, uid, ids, c={}: ids, [], 10)})
}
```

## DEBUG

Per debuja un `fields.funcion()` es necessary fer-ho des de un `ipython`.

A través d'un `read` del camp entrerà a la `__ff_` definida
