<!-- TOC INICIO -->
- [03. Entorno de desarrollo](#03-entorno-de-desarrollo)
  - [Definir editor de texto por defecto](#definir-editor-de-texto-por-defecto)
  - [Estructura de ficheros](#estructura-de-ficheros)
  - [Entorno virtual de Python](#entorno-virtual-de-python)
  - [Configuración GIT](#configuración-git)
    - [Clave GPG](#clave-gpg)
<!-- TOC FIN -->

# 03. Entorno de desarrollo

En esta sección se van a configurar varios parámetros del propio entorno, como el editor de texto por defecto o la herramienta para crear entornos virtuales de Python para desarrollar.

## Definir editor de texto por defecto

Desde GISCE-TI utilizamos VIM, sin embargo se puede utilizar cualquier otro. Para configurarlo por defecto, utilizamos:

`sudo update-alternatives --config editor`

## Estructura de ficheros

Definiremos una carpeta para los proyectos i.e. `~/proyectos` con el comando:
```bash
mkdir ~/proyectos
```

## Entorno virtual de Python

Instalaremos los siguientes paquetes de python para desarrollar con entornos virtuales y desde consola:

<details>
<summary>Para versiones de Ubuntu superiores a la 24.04</summary>

* pyenv y otras herramientas de entornos virtuales, pueden dar problemas
```bash
sudo -H ~/.pyenv/shims/pip install --upgrade pip
sudo -H ~/.pyenv/shims/pip install ipython
sudo -H ~/.pyenv/shims/pip install virtualenvwrapper  
```

* Definimos el directorio donde se crearán los entornos virtuales de Python
```bash
echo export WORKON_HOME=$HOME/.virtualenvs >> ~/.bashrc
```

* La siguiente línea sólo para Ubuntu 22.04 o posterior
```bash
echo export VIRTUALENVWRAPPER_PYTHON=~/.pyenv/shims/python  >> ~/.bashrc
```

* Añadimos el virtualenwrapper al arranque del terminal de Ubuntu
```bash
echo source ~/.pyenv/versions/2.7.18/bin/virtualenvwrapper.sh >> ~/.bashrc
```

</details>

<details>
<summary>Para versiones de Ubuntu anteriores a la 24.04</summary>

```bash
sudo -H pip install --upgrade pip
sudo -H pip install ipython
sudo -H pip install virtualenvwrapper  
# pyenv y otras herramientas de entornos virtuales, pueden dar problemas

# Definimos el directorio donde se crearán los entornos virtuales de Python
echo export WORKON_HOME=$HOME/.virtualenvs >> ~/.bashrc
# La siguiente línea sólo para Ubuntu 22.04 o posterior
echo export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python2  >> ~/.bashrc
# Añadimos el virtualenwrapper al arranque del terminal de Ubuntu
echo source /usr/local/bin/virtualenvwrapper.sh >> ~/.bashrc
```

</details>

```bash
source ~/.bashrc
```

Utilizando los comandos que usaremos más adelante para crear nuestros entornos de 
**OpenERP-Client** y **OpenERP-Server**

<details>
<summary>Es posible crear un entorno virtual</summary>

* Para crear el venv
```bash
mkvirtualenv <nombre> -a <dirección del proyecto>
``` 

* Para eliminar el venv
```bash
rmvirtualenv <nombre> 
``` 

* Para activar/desactivar el venv
```bash
workon
``` 
```bash
deactivate
``` 

* Para crear un venv temporal
```bash
mktmpenv
``` 

* Se elimina al hacer 
```bash
deactivate
``` 

</details>

## Configuración GIT

Presuponemos que se dispone de usuario GIT con permisos para el código de GISCE-TI.

El primer paso será generar las claves SSH con el comando:
```bash
ssh-keygen -t rsa -b 4096
```

Seguidamente añadimos esta clave a nuestro usuario de GitHub (User > Setting > SSH and GPG keys)
```bash
cat ~/.ssh/id_rsa.pub
```

Por último hace falta configurar un nombre y un correo para que git nos pueda identificar. Lo haremos con el siguiente comando:
```bash
git config --global -e
```

El nombre no es vinculante, pero el correo debe coincidir con el correo del usuario de GitHub.
Se puede configurar el editor de GIT por defecto en esta configuración.

Un ejemplo de configuración sería:
```commit
[user]
        email = <user>@<domain>
        name = Demo Name
[core]
        editor = vim
[commit]
        gpgsign = true
```

### Clave GPG

Sería interessante que todos los participantes utilizaramos claves GPG en nuestro ordenador principal. 
Se puede seguir la [Guía de GitHub para configurar una clave GPG](https://help.github.com/articles/signing-commits-using-gpg/).

<details>
<summary>Clave GPG</summary>

* To configure your Git client to sign commits by default for a local repository, in Git versions 2.0.0 and above
```commit
# Aquesta part s'ha introduit amb el fitxer de configuració
# [commit]
#        gpgsign = true

git config commit.gpgsign true 
```

* To sign all commits by default in any local repository on your computer.
```bash
git config --global commit.gpgsign true
```

</details>
