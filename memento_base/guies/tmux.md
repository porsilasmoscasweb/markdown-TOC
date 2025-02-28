<!-- TOC INICIO -->
- [TMUX](#tmux)
  - [Documentació](#documentació)
  - [Sessions](#sessions)
  - [Controls](#controls)
  - [Guardar configuracion de tmux](#guardar-configuracion-de-tmux)
<!-- TOC FIN -->

# TMUX

El tmux s'executa des del servidor o desde el propio PC

* server
`ssh user@server.whatever`

## Documentació

[Manual](https://man.openbsd.org/OpenBSD-current/man1/tmux.1)

## Sessions

* `tmux new -s <nom_sessio>`
* `tmux a -t <nom_sessio>`
 
## Controls

* `Ctrl+b c`: Crea una nova pestanya
* `Ctrl+b w `: Tria una pestanya de la llista de tots els tmux
* `Ctrl+b 0/1/2`: Canvia a la pestanya del número triat
* `Ctrl+b ,`: Renombrar pestanya
* `Ctrl+b %`: Parteix vertical
* `Ctrl+b "`: Parteix horitzontal
* `Ctrl+b o`: Vas al al següent panell
* `Ctrl+b ;`: Alterna entre el panell actual i l'anterior
* `Ctrl+b x`: Tanca el panell on et trobes
* `Ctrl+b d`: surts de la sessio

## Guardar configuracion de tmux

Para guardar la configuración de tmux de manera que se cargue cada vez que se inicie el servidor o el PC, 
debes crear un archivo de configuración llamado `.tmux.conf` en tu directorio de inicio. 

Este archivo puede contener todas las configuraciones que deseas aplicar, como ajustes de teclas, colores y otras personalizaciones. 

Al iniciar `tmux`, este archivo se cargará automáticamente y aplicará todas las configuraciones definidas. 
Si necesitas modificar la configuración mientras estás en una sesión de `tmux`, puedes usar el comando `tmux source-file ~/.tmux.conf` 
para recargar el archivo de configuración sin necesidad de reiniciar tmux.
    