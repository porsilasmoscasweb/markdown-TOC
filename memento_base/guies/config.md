<!-- TOC INICIO -->
- [CONFIG](#config)
<!-- TOC FIN -->

# CONFIG

Tot programa té un fitxer de configuració. Aquest conté una seria de variables d'entorn que s'utilizarà el programa. 
Aquestes poden ser sobre escrites a través de la seva ejecució dintre la linea de comanda o de un programa que gestioni variable d'entron.

Un exemple per entedreu seria:

Quan arrenquem l'ERP des de Pycharm aquet té definides una seria de variables d'entorn, el programa s'inicia segons les 
variables del fitxer, però si una de les variables d'entorn es diu igual que una de les de configuraciò de l'entorn
serà la que utilitzarà el programa per iniciar-se.

Per útilitzar aquest fitxer afegirem **--config=<path>** al parametres de l'script
```bash
--no-netrpc --price_accuracy=6 --port=8069 --database=test_sql 
--config=/home/egarriga/config/pycharm_erp
```

* Fitxer de configuraciò:
```bash
/home/<usuari>/config/config_file
```

* Variables d'entorn: Aquestes sempre tenen que estar en minuscula, i amb un HEADER [options] que l'ERP amb la classe configParsers gestionarà. 
```bash
[options]
db_host=localhost
db_port=5432
db_password=1234
db_user=erp
esios_token=67c6aff80ca331eec78e1f62b7ffc6799e2674d82d57c04104a612db43496db3
msgpack=1
msgpack_host=0.0.0.0
msgpack_port=8068
redis_url=redis://localhost
secret=lando
stg_url=http://localhost:5010/api
webclient_preview_features=true
webclient_primary_color=#007bff
webclient_refresh_token_seconds_threshold=300
webclient_theme_mode=compact
webclient_title=test webclient localhost
```