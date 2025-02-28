<!-- TOC INICIO -->
- [LINUX](#linux)
  - [DRECERES DE TECLAT](#dreceres-de-teclat)
  - [Como programar un reinicio programado al ERP](#como-programar-un-reinicio-programado-al-erp)
<!-- TOC FIN -->

# LINUX

## DRECERES DE TECLAT

* **ALT+F2**: Escribim commanda

* Matar un progama per any reson:
  * **ALT+F2** `xkill`

## Como programar un reinicio programado al ERP

Con el comando [`at`](https://en.wikipedia.org/wiki/At_(command)), un comando que existe des de "siempre" podemos programar acciones de una sola vez.

Vendría a ser como un `cronjob` pero *one shot*.

por exemplo si queremos reiniciar hoy a las 14h podemos hacer:

```bash
at 14:00
```
Luego nos aparece una "shell" donde ponemos lo que queramos ejecutar en nuestro caso ponemos:

```bash
oopgrade --config ~/conf/<erp>.conf pubsub --channel all harakiri
```
Cuando tengamos el comando introducido pulsamos `Ctrl+d` para salir y nos dirá alguna cosa similar a:

```
job 1 at Mon Nov 11 14:00:00 2024
```

Podemos listar todos los trabajos planificados con: `at -l ` y si queremos eliminar lo podemos hacer con `at -r ID` donde el `ID` es el numero del job.