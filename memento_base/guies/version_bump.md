<!-- TOC INICIO -->
- [POWERPROFILE](#powerprofile)
  - [CREACIÓ DE NOVA VERSIÓ DES DE GITHUB](#creació-de-nova-versió-des-de-github)
  - [CREACIÓ DE NOVA VERSIÓ DES DE PROJECTE](#creació-de-nova-versió-des-de-projecte)
  - [DEPLOY](#deploy)
  - [Només per tenir el dia](#només-per-tenir-el-dia)
<!-- TOC FIN -->

# POWERPROFILE

## CREACIÓ DE NOVA VERSIÓ DES DE GITHUB

Per pujar de versió ara es fa de forma automàtica quan es mergeja a `master`

No cal fer el `commit` Bump to .... Per fer-ho ara en Pol ho ha automatizat. Només tenim que ficar el `tag` corresponent al GITHUB
* `minor`: 0.+.0
* `patch`: 0.0.+


## CREACIÓ DE NOVA VERSIÓ DES DE PROJECTE

[Publicar llibraria RFC](https://rfc.gisce.net/t/publicar-una-llibreria-a-pypi-amb-twine/2011)

Des de la llibreria i en entorn virtual `workon erp`

* Mergegem la branca a `master`
* En col·loquem a la branca `master`
* Canviem la versió en el `setup` > `__init__.py`
* Afegim els canvis `git add -p`
* Fem el commit > `git commit -m "Bump to v0.0.0"`
* Afegim el tag al commit `git tag v0.0.0`
    * Això associa el tag a la versió
* Pujem els canvis `git push origin master --tags`

Des de Github > Realse > Selectionar el tag

* Pujar al `pip`

Des de la llibreria i en entorn virtual `workon erp`

* Crea un fitxer encapsulant la llibreria en `.bz2` > `python setup sdict` 
* Cal tenir instal·lat el `twine` > `twine upload dist/<lib_version_file>`

* Instal·lem a local `pip install -e .`
  * Pot ser que tardi una miqueta a penjar-se si no es canvia espera uns minuts i tornar a fer `install`.


## DEPLOY

* Ens tots els mòduls que utilitssin la `llibreria` canvierem a requirtements.txt a la versió actual.

`addons/gisce/GISCEMaster/giscedata_telemesures_distri/requirements.txt`

* Pujar els canvis a la PR que toca
* Sastre al server que toqui
* Upgrade del powerprofile en el server que toca

`pip install --upgrade <llibreria>`
or
`pip install -r requirements.txt`

* `-r` argument que tindrà com a parametre un fitxer aquest farà un istall o actualitzarà si ja existeix els paquets definits en el fitxer 

## Només per tenir el dia

* Comprovar en el repo GIT que estigui en la versió que toca.
* Descargar la nova versió al local

```
git checkout master
git fetch -pPf
git pull
```