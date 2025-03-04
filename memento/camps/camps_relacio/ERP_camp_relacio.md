<!-- TOC INICIO -->
- [CAMP RELACIÓ](#camp-relació)
  - [ADJUDICAR A _ONE2MANY_ I _MANY2MANY_](#adjudicar-a-_one2many_-i-_many2many_)
  - [EXEMPLE (obtenir totes les tasques d'un equip segons id d'usuari)](#exemple-obtenir-totes-les-tasques-dun-equip-segons-id-dusuari)
      - [Atributs](#atributs)
  - [EXEMPLE (one2many com a camp funció)](#exemple-one2many-com-a-camp-funció)
<!-- TOC FIN -->

# CAMP RELACIÓ

> **NOTA**
> 
> Només serveix si la classe conté els paramatres `osv.osv` si conté `osv.osv_memory` els camps es guarden en memoria i prou.

Camps que tenen la funció de relacionar taules. 

* `one2many`: Crearà un camp a la taula `???`.
* `many2one`: Crearà un camp a la taula `???`.
* `many2many`: Crearà un taula extra per les relacions `n:n`.
  *  Crearà un camp a una de les taules a les que afecta (es ferà l'auto_init d'aquesta taula).


## ADJUDICAR A _ONE2MANY_ I _MANY2MANY_

* `(0, 0,  { values })`: enllaç a un registre nou que s'ha de crear amb el diccionari de valors donat.
* `(1, ID, { values })`: actualitzar el registre enllaçat amb id = ID (escriu-hi *valors*).
* `(2, ID)`:             elimineu i suprimiu el registre enllaçat amb id = ID (trucades per desenllaçar l'identificador, això suprimirà completament l'objecte i l'enllaç també).
* `(3, ID)`:             talla l'enllaç al registre enllaçat amb id = ID (elimina la relació entre els dos objectes però no elimina l'objecte de destinació en si).
* `(4, ID)`:             enllaç al registre existent amb id = ID (afegeix una relació).
* `(5)`:                 desenllaçar-ho tot (com utilitzar (3,ID) per a tots els registres enllaçats).
* `[(6, 0, [IDs])]`:     substituïu la llista d'identificadors enllaçats (com utilitzar (5) i després (4, ID) per a cada identificador de la llista d'identificadors).


## EXEMPLE (obtenir totes les tasques d'un equip segons id d'usuari)

Posem pel cas que volem obtenir tots els `cases` d'un `teams` el qual un usuari `uid` forma part. 

1. Tindriem que fer és obtenir l'id de la tasca `task_id` dels casos que trobem a la taula `crm_cases`, ja que és la que té l'associó amb el model `crm_task`.
2. Apartir de la `crm_task` podriem saber quins equips té associats `team_id` amb relació a la taula `crm_teams`. 
3. Per útim hauriem d'obtenir quin usuaris estan associats els mateixos equips l'ususari `uid`, 
per aixó utilitzariem un altre camp funció `member_ids` que ens conectarà la taula `crm_teams` amb la de `res.users` amb relació many2many. 

```
# Passos 1 i 2
<record id="crm_my_teams_sac_opened_act" model="ir.actions.act_window">
    ...
    <field name="domain">[('task_id.team_id.member_ids', '=', uid)]</field>
</record>

# Pass 3
class whatever(osv.osv):
    _columns = {
         'member_ids': fields.many2many('res.users', 'project_task_user_rel', 'task_id', 'uid', 'Task Members', help="Task's member. Not used in any computation, just for information purpose."),
    }
```

#### Atributs

* Objecte reglacionat
* Taulra intermitja que es crearà o apuntarà
* camps 1 de la taula intermitja
* camps 2 de la taula intermitja
* String a mostrar
* String de comprenció del camp


## EXEMPLE (one2many com a camp funció)

Necessitem obtenir tots els arxius adjunt que té associcats una tasca. La taula dels fitxes associats `ir.attachment` necessita un id de taskca i també un model, pel que aixó fa necessati fer un camp `one2many` amb `field.function()`.

> VIEW

```
<page string="Attachments Files">
    <field name="attachment_ids"/>
</page>
```

> CLASS

```
def _ff_attached_files_task(self, cursor, uid, ids, field_name, args, context=None):
    attach_obj = self.pool.get('ir.attachment')
    res = {}
    for project_task_id in ids:
        # Busquem per tots els attachements quins tenen id de la tasca on ens trobem i que el model sigui "project.task"
        attachment_ids = attach_obj.search(cursor, uid, [('res_id', '=', project_task_id), ('res_model', '=', 'project.task')])
        res[project_task_id] = attachment_ids
    return res
    
_columns = {
    'attachment_ids': fields.function(_ff_attached_files_task, type='one2many', relation='ir.attachment', method=True, string='Adjunts'),
}
```