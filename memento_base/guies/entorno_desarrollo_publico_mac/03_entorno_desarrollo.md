# 03. Entorno de desarrollo

<!-- TOC INICIO -->
- [03. Entorno de desarrollo](#03-entorno-de-desarrollo)
- [03. Entorno de desarrollo](#03-entorno-de-desarrollo)
  - [Estructura de ficheros](#estructura-de-ficheros)
  - [Configuración GIT](#configuración-git)
    - [Clave GPG](#clave-gpg)
<!-- TOC FIN -->

# 03. Entorno de desarrollo

En esta sección se van a configurar varios parámetros del propio entorno, como el editor de texto por defecto o la
herramienta para crear entornos virtuales de Python para desarrollar.

## Estructura de ficheros

Definiremos una carpeta para los proyectos i.e. `~/proyectos` con el comando:
```bash
mkdir ~/proyectos

cd proyectos
```


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

> Posbile error conla key ssh que ya existe o no la detecta.
> 
> Creamos una nueva i en el archivo `~/.ssh/config` copiemos lo siguiente:

```text
// ... copia del mac
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
