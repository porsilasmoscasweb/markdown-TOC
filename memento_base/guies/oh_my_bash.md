<!-- TOC INICIO -->
- [Instal·lació de Oh My Bash al terminal d'Ubuntu](#installació-de-oh-my-bash-al-terminal-dubuntu)
  - [Instalación](#instalación)
  - [Configuración](#configuración)
  - [Instalar fuentes](#instalar-fuentes)
  - [Ajustes opcionales](#ajustes-opcionales)
<!-- TOC FIN -->

# Instal·lació de Oh My Bash al terminal d'Ubuntu

Este repositorio da más potencia al terminal `bash` de Ubuntu, ya que al ubicarnos en un directorio `git` se nos brindará información acerca de la rama, los cambios pendientes de subir, etc.

## Instalación
Desde el terminal de Ubuntu, clona el repositorio:
```bash
# Aconsejo instalar el repositorio en la carpeta personal
git clone https://github.com/ohmybash/oh-my-bash.git ~/.oh-my-bash
```

Guarda una copia de seguridad de tu fichero de configuración `.bashrc`:
```bash
cp ~/.bashrc ~/.bashrc.orig
```

Añade la configuración de `OhMyBash` al fichero `.bashrc` y refresca la configuración.
```bash
cat ~/.oh-my-bash/templates/bashrc.osh-template >> ~/.bashrc
source ~/.bashrc
```

## Configuración
En el fichero de configuración `~/.bashrc`, podemos cambiar el tema visual por el que queramos:
`OSH_THEME="powerline"`.

En el siguiente enlace hay vistas previas de algunos de los temas que se incluyen en el repositorio: 
https://github.com/ohmybash/oh-my-bash/wiki/Themes

## Instalar fuentes

Algunos temas usan fuentes especiales, como `powerline`. En caso de usar esos temas y no ver correctamente los carácteres en la barra, hay que instalar la fuente y refrescar las colecciones de las mismas.

```bash
sudo apt install fonts-powerline
fc-cache -vf
```

## Ajustes opcionales
Si no queremos que se nos pregunte si queremos actualizar el repositorio cuando se detecten versiones nuevas, podemos añadir este ajuste al fichero `~/.bashrc`.
`DISABLE_UPDATE_PROMPT="true"`

Si directamente queremos desactivar las actualizaciones automáticas, deberemos modificar este ajuste en el fichero `~/.bashrc`:
`DISABLE_AUTO_UPDATE="true"`