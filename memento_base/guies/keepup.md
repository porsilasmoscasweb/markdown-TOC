<!-- TOC INICIO -->
- [KEEP UP](#keep-up)
  - [ERROR DE KEEPUP](#error-de-keepup)
    - [ERROR 1](#error-1)
    - [ERROR 2](#error-2)
<!-- TOC FIN -->

# KEEP UP


Quan un Keepup passa mira tot el que esta a `v**.*-minors` i ho actualitza a tots els servidors que tenen aquestes branques de minors.

Per que aixó entri a les branques abans del merge d'una `PR` s'ha haver afegit en la PR del Github els tags de `Projects` en quines minor s'aplicar

Aquestes si s'han actualitzat correctament es possarant en `Done` si no en `Error` que serà quan haurem de realitzar un fix d'aquest en el servidor que hagi fallat

* Recorrer les minors [branch] de cada servidor i aplica una seria d'accións com serien:
  - apply addons
  - instal·la requirements.txt
  - harakiri


## ERROR DE KEEPUP

En cas de que no passi el `keepup` haurem  de mirar a slack conversació `erp-update` pel motiu que ha fallat.

Possibles errors:
1. `Command '['oopgrade', 'requirements', 'install']' returned non-zero exit status 1`
2. `Not all branches merged!`
3. etc


### ERROR 1


### ERROR 2

* Haurem d'entrar el servidor
`ssh gisce@<server>`

* Entrem amb l'usuari `erp`
`suso su - erp`

* Ens col·loquem a la carpeta erp
`cd src/erp`

* Validem quines minors te instal·lades
`car ~/conf/<sever> | grep <error-branch>`

* li fem un merge a la minor per possar-la el dia
`git merge origin/<error-branch>`

* Llistem els fitxers i validem els que estan amb conflictes
`git status`

* Arreglem els conflictes
`vim <file>`

* Per borrem la part del `>>>> HEAD` i deixem el de la minor ja que es el que segur que esta bé ja que es la part 
  que va entra neta per última vegada. Després de guarda els canvis afegim el fitxer
`git add <file>`

* Un cop tots els fitxers estan arreglats commitejem amb missatge per defecte
`git commit` `:wq`

* Tornem a llança el cron del `keepup`
`crontab -l`
* Copiem el cron de `KEEPUP` i executem
`PATH=/home/erp/bin:/usr/bin:/bin ~/bin/keepupd --config=/home/erp/conf/saltoscabrera.conf update --force`

* Un cop tot commitejat reiniciem el webclient
`restart webclient`
