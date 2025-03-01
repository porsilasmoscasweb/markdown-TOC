<!-- TOC INICIO -->
- [LOGS](#logs)
  - [GRAFANA LOGS [NEW]](#grafana-logs-new)
  - [REVISAR ELS LOGS](#revisar-els-logs)
  - [On estar la conf supervisor](#on-estar-la-conf-supervisor)
  - [Veure el log dels process concret](#veure-el-log-dels-process-concret)
<!-- TOC FIN -->

# LOGS

## GRAFANA LOGS [NEW]

Els nous loggers que en Pol Sala a fet contenent un `hash` que des de [GRAFANA](https://play.grafana.org/d/bdnahipisghdsa/getting-started-with-grafana-play?orgId=1&from=now-1h&to=now&timezone=browser)
es pot monitoritsar per tal de poder fer un seguiment molt més clar i amb molta més informació que els actuals amb `logging`.


```python
from tools.service_utils import WebServiceTracker
...
with WebServiceTracker(
        uid=uid, 
        obj='giscedata.omie.casacion', 
        method='get_casation_by_session', 
        logger_name='openerp.omie'
) as cron_wst:

cron_wst.log(
    [logging.INFO, logging.ERROR], 
    msg="No s'ha pogut obtenir la cassació des d'OMIE.", 
    status=['Running', 'Succeed','Failed'])
```

## REVISAR ELS LOGS

* Connectar-se al servidor
* Obrir un TMUX
* Entra com a usuari `erp`
  * `sudo su - erp`
* Anar al directori
  * `cd var/log`
* Llistem logs
  * `ls -lisathr`
  * `ls -lisathr | grep <low>`
* Buscar la queue: (on s'estar fent) queue;"low"
  * `tail -F nom_del_log.0*.log` (per no agafar els backups) 
  * `less -F nom_del_log.0*.log` (com si fos un `vim`) 
 

## On estar la conf supervisor

sudo su -
ls /etc/supervisor/conf.d/
res = cat /etc/supervisor/conf.d/* | grep stdout_logfile
tail -f {res} 
less -f {res}


## Veure el log dels process concret

sudo supervisorctl
tail -f {process}