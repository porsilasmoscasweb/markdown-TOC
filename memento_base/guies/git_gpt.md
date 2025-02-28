<!-- TOC INICIO -->
- [GIT CHATGPT](#git-chatgpt)
  - [📌 DEFINICION DE AREAS DE GIT](#-definicion-de-areas-de-git)
    - [Working Directory (Directorio de trabajo)](#working-directory-directorio-de-trabajo)
    - [Stage (Stage (Área de preparación o área de index)](#stage-stage-área-de-preparación-o-área-de-index)
  - [📌 Inicialización y Configuración](#-inicialización-y-configuración)
  - [📌 Ver Estado y Registro](#-ver-estado-y-registro)
  - [📌 Seguimiento de Archivos](#-seguimiento-de-archivos)
  - [📌 Commits](#-commits)
  - [📌 Deshacer Cambios](#-deshacer-cambios)
    - [RESET](#reset)
    - [RESTORE (Git 2.23)](#restore-git-223)
      - [Params](#params)
    - [DIFF](#diff)
  - [📌 Sincronización y Ramas](#-sincronización-y-ramas)
  - [📌 Ramas](#-ramas)
    - [BRANCH](#branch)
    - [CHECKOUT & SWITCH](#checkout--switch)
  - [📌 Merging](#-merging)
    - [Fast-forward Merge](#fast-forward-merge)
    - [Recursive Merge](#recursive-merge)
    - [Octopus Merge](#octopus-merge)
    - [Ours Merge](#ours-merge)
    - [Theirs Merge](#theirs-merge)
  - [📌 Tags](#-tags)
  - [📌 Remotos](#-remotos)
  - [📌 Patching](#-patching)
    - [PATCH](#patch)
    - [FORMAT-PATCH](#format-patch)
      - [Opciones útiles:](#opciones-útiles)
      - [Cuándo usar git format-patch?](#cuándo-usar-git-format-patch)
    - [FORMAT-PATCH | MAIL](#format-patch--mail)
    - [DIFF](#diff)
    - [Diferencias Clave entre `git format-patch` y `git diff`](#diferencias-clave-entre-git-format-patch-y-git-diff)
    - [CRERRY-PICK](#crerry-pick)
    - [REBASE](#rebase)
      - [¿Cuál usar?](#cuál-usar)
    - [RESET](#reset)
  - [📌 Debbugging](#-debbugging)
  - [📌 Guardar Cambios Temporales](#-guardar-cambios-temporales)
  - [📌 Submódulos](#-submódulos)
  - [📌 Buenas prácticas y herramientas avanzadas](#-buenas-prácticas-y-herramientas-avanzadas)
  - [📌 Otros Comandos Útiles](#-otros-comandos-útiles)
<!-- TOC FIN -->

# GIT CHATGPT

> ## [DOCS](https://git-scm.com/docs)

## 📌 DEFINICION DE AREAS DE GIT

Las areas de trabajo en GIT son los passos que se usant entre nuestro repositorio **local** y nuestro repositorio **origin**.

Estos son los siguientes:

* **Modificación en el directorio de trabajo**: Haces cambios en los archivos.
* **Agregar al stage**: Usas comandos como git add para preparar esos cambios antes de hacer un commit.
* **Commit**: Después de haber agregado los archivos al stage, los confirmas (con git commit), y esos cambios se almacenan en el 
  repositorio.

### Working Directory (Directorio de trabajo)

> Antes del **ADD**. Archivos en bruto. Los que en **IDE** estan en color (menos el verde)

Es el espacio donde tú ves y editas los archivos de tu proyecto en tu computadora. Es el lugar donde haces cambios en el código, 
creas nuevos archivos o modificas los existentes. 

Es el área en la que interactúas con los archivos de tu proyecto. Los cambios que haces en tus archivos ocurren aquí primero, pero 
no se reflejan de inmediato en el repositorio de Git hasta que los pongas en el stage y luego los confirmes (commit) 

### Stage (Stage (Área de preparación o área de index)

> Antes del **COMMIT**. 
> Se añaden con el **ADD**. 
> Archivos preparados para subirse al repositorio. 
> Los que en **IDE** estan de color **verde**.

El "stage" es un área intermedia entre el directorio de trabajo y el repositorio de Git. Aquí es donde colocas los archivos que has 
modificado y que deseas incluir en tu próximo commit. En otras palabras, el stage actúa como una "zona de preparación" para los cambios que deseas guardar en el historial de Git. 

Permite que puedas seleccionar específicamente qué cambios quieres registrar en tu repositorio sin tener que comprometer todos los 
cambios realizados en el directorio de trabajo. 

> Por ejemplo, si modificas varios archivos, puedes elegir agregar solo algunos al stage y dejar otros fuera.


## 📌 Inicialización y Configuración

- **`git init`**: Inicializa un repositorio Git en un directorio.
  
- **`git config --global user.name "Nombre"`**: Configura el nombre de usuario a nivel global.
  
- **`git config --global user.email "email@example.com"`**: Configura el correo electrónico del usuario a nivel global.

- **`git config --list`**: Muestra la configuración actual de Git.

- **`git config --global core.editor "editor"`**: Configura el editor de texto predeterminado.

## 📌 Ver Estado y Registro

- **`git status`**: Muestra el estado del repositorio actual.
  
- **`git log`**: Muestra el historial de commits.

- **`git log --oneline`**: Muestra el historial en una línea.

- **`git log --graph --decorate --all --oneline`**: Muestra el historial en forma gráfica.

- **`git log -p`**: Muestra los commits con parches (cambios).


## 📌 Seguimiento de Archivos

- **`git add <archivo>`**: Añade un archivo al área de staging.

- **`git add .`**: Añade todos los archivos modificados y nuevos.

- **`git rm <archivo>`**: Elimina un archivo del repositorio.

- **`git rm --cached <archivo>`**: Elimina un archivo de staging sin borrarlo.

- **`git mv <archivo>`**: Mueve o renombra un archivo.

## 📌 Commits

- **`git commit -m "mensaje"`**: Crea un commit con mensaje.

- **`git commit -a -m "mensaje"`**: Hace commit de todos los archivos modificados.

- **`git commit --amend`**: Editar el último commit.

- **`git commit --amend -m "mensaje nuevo"`**: Cambia el mensaje del último commit.

- **`git revert <commit>`**: Crea un nuevo commit que revierte otro.

## 📌 Deshacer Cambios

### RESET

> Para **modificar commits** o deshacer cambios en el historial de Git..

- **`git reset --hard <commit>`**: Revierte el repositorio a un commit, eliminando cambios posteriores.

- **`git reset --soft <commit>`**: Revierte el repositorio sin perder los cambios en **staging**.

- **`git reset HEAD <archivo>`**: Elimina un archivo de staging.

- **`git checkout -- <archivo>`**: Deshace cambios en un archivo no confirmado.

- **`git checkout -- <archivo> --path`**: Deshace cambios en un archivo no confirmado. Solo desaciendo cambios concretos.


### RESTORE (Git 2.23)

> Más nuevo que `git checkout --`
>
> Para descartar cambios **antes de hacer un commit**, sin tocar la historia de Git.
> 
> Su propósito principal es restaurar archivos en el working directory o el staging area (índice).

- `git restore`: Descartar cambios en archivos del **working directory**. Antes de hacer `git add`
  - Si el archivo es nuevo y no ha sido añadido con `git add`, se mantiene sin cambios.

- `git restore --stage <file>`: Quitar un archivo del staging (índice) sin perder los cambios en el working directory. 
  - Si agregaste un archivo con `git add`, pero todavía no hiciste un commit, puedes sacarlo del staging sin perder su contenido.
  - Esto quita el archivo del staging, pero mantiene los cambios en el working directory. Es equivalente a `git reset <file>`

- `git restore --source=<ID_DEL_COMMIT> <file>`: Restaurar un archivo desde un commit específico.
  - sto traerá la versión del archivo que estaba en el commit **ID_DEL_COMMIT**.

- `git restore --source=HEAD --stage --worktree <file>` or `git restore --stage --worktree <file>`: Descartar cambios en el 
  working directory y el staging al mismo tiempo.
  - Si quieres deshacer todos los cambios en un archivo, incluso si ya lo agregaste al staging
  - Si omites --source=HEAD, Git asume que quieres restaurar la última versión commitada.

- `git restore --force <file>`: Forzar la restauración de un archivo con cambios no guardados. 
  - Si tienes cambios en un archivo que Git considera "sin seguimiento" y quieres forzar la restauración.
  - ⚠️ Precaución: Esto eliminará cualquier cambio en el archivo. No hay forma de recuperarlo después.

#### Params

- `--source=HEAD` → Usa la versión del último commit.
- `--staged` → Quita el archivo del staging.
- `--worktree` → Descarta los cambios en el working directory.

| Comando                                  | ¿Qué hace? |
|------------------------------------------|-----------|
| `git restore archivo.txt`               | Restaura el archivo al último commit, descartando cambios en el working directory |
| `git restore --staged archivo.txt`      | Quita el archivo del staging, pero mantiene los cambios en el working directory |
| `git restore --staged --worktree archivo.txt` | Deshace cambios en el working directory y el staging |
| `git restore .`                         | Restaura todos los archivos modificados en el working directory |
| `git restore --staged .`                | Quita todos los archivos del staging |
| `git restore --staged --worktree .`     | Deshace todos los cambios en el repositorio (working directory + staging) |
| `git restore --source=<commit> archivo.txt` | Restaura la versión de un archivo desde un commit específico |
| `git restore --force archivo.txt`       | Fuerza la restauración de un archivo (⚠️ peligro: elimina cambios no guardados) |


### DIFF

| Comando             | ¿Qué hace? | ¿Cuándo usarlo? |
|--------------------|-----------|----------------|
| `git reset`       | Modifica el historial, elimina commits o saca archivos del staging | Cuando quieres deshacer commits o cambios preparados (`git add`) |
| `git restore`     | Descarta cambios en el working directory o saca archivos del staging | Antes de hacer un commit, si quieres descartar cambios en archivos |
| `git checkout --` | Antigua forma de hacer `git restore` | Se recomienda usar `git restore` en su lugar |


## 📌 Sincronización y Ramas

- **`git clone <url>`**: Clona un repositorio.

- **`git pull`**: Trae cambios de un remoto y los combina.

- **`git pull --rebase`**: Trae cambios y hace `rebase`.

- **`git push`**: Sube los cambios a un remoto.

- **`git push --force`**: Fuerza el push.

- **`git push -u origin <rama>`**: Establece una rama remota como predeterminada.

- **`git fetch`**: Descarga los últimos cambios del repositorio remoto, pero no los fusiona (merge) con tu rama local.
  Es útil para actualizar tu repositorio local con los últimos commits del remoto sin afectar tu trabajo actual.
- **`git fetch -f`**: _force_ Forzar la actualización de las referencias incluso si hay conflictos. 
  Útil si necesitas sobrescribir los cambios locales con la versión remota.
- **`git fetch -p`**: _prune_ Elimina las ramas remotas que ya no existen en el repositorio remoto. 
  Si alguien eliminó una rama en el remoto, este comando la eliminará de tus referencias locales.
- **`git fetch -P`**: _prune-tags_ Elimina los tags que ya no se usan.

## 📌 Ramas

### BRANCH

- **`git branch`**: Muestra las ramas locales.

- `git branch -a`: Listar todas las ramas del repositorio incluidos los remotos.

- **`git branch <nombre>`**: Crea una nueva rama.

- **`git branch -d <nombre-rama>`**: Elimina una rama local.

- **`git branch -D <nombre-rama>`**: Elimina una rama local de forma forzada.

### CHECKOUT & SWITCH

> Switch es como **checkout**, però menos potente.

- **`git checkout <nombre-rama>`**: Cambia a otra rama.
- `git switch`: Cambia a otra rama.

- **`git checkout -b <nombre>`**: Crea y cambia a una nueva rama.
- `git switch -c`: Crea y cambia a una nueva rama.

- `git switch --orphan`: Crea una nueva rama en blanco. Por ejemplo: para documentacion.

- `git switch --discard-changes`: Cambia a otra rama y me descarta los cambios que pueda tener en el working directori. 
  - Con **checkout** los cambios se mueven a la rama que nos movemos.

## 📌 Merging

- **`git merge <rama>`**: Fusiona una rama en la actual.

El merge se executa a través de distintas estrategias. A continuación te mostramos cuales:
* `Fast-forward`: Cuando no hay cambios en la rama de destino después de la separación. 
* `Recursive`: Fusión estándar cuando hay cambios en ambas ramas.
* `Octopus`: Para fusionar más de dos ramas a la vez.
* `Ours`: Mantiene los cambios de la rama actual, ignorando la otra.
* `Theirs`: Toma los cambios de la rama fusionada, ignorando los de la actual.

Como vemos el merge puede generar conflictos si dos o más usuarios han modificado el mismo fichero en distintas ramas.

Esto se resuelve con las estrategias de merge `ours`, `theirs` o de forma `manual`. Pero también es posible resolverlo con herramientas
externas como es el caso de las `IDE` que tienen la opcion de `mergetool` incorporadas. Estas constan de 3 paneles en los que 
nos muestran las 3 opcionas antes mencionadas.
Interactuando con los paneles podemos hacer el merge de forma visual.

### Fast-forward Merge

Este tipo de merge ocurre cuando la rama de destino no tiene ningún commit nuevo desde el punto en que ambas ramas se separaron. 
Es decir, si la rama que quieres fusionar tiene cambios que se pueden aplicar directamente al final de la rama de destino, Git 
simplemente **mueve el puntero** de la rama de destino hacia adelante, sin necesidad de un commit adicional. 

Es como si simplemente avanzaras la historia de la rama de destino. 

```bash
# Estás en la rama main y tienes la rama feature.
git merge feature
```


### Recursive Merge

El merge recursivo es el que se usa cuando Git necesita fusionar ramas que han avanzado de forma independiente. Es el tipo de merge 
por defecto cuando **ambas ramas tienen commits nuevos y han divergiendo**. 
En este caso, Git intenta fusionar ambas ramas de forma automática, y **si hay conflictos**, los muestra para que el usuario los 
resuelva manualmente. 

```bash
# Estás en la rama main y tienes la rama feature.
git merge feature
```


### Octopus Merge

Este tipo de merge es menos común y se usa **cuando se fusionan más de dos ramas al mismo tiempo**. Este merge intenta combinar varias ramas en una sola. 
Si las ramas no tienen conflictos, el merge será automático, pero si hay conflictos, se necesitarán resoluciones manuales. 

```bash
git merge rama1 rama2 rama3
```


### Ours Merge

La estrategia ours se usa para indicar que, **en caso de conflicto, se eligen los cambios de la rama actual**, ignorando los de las 
ramas a fusionar.

```bash
git merge -s ours feature
```


### Theirs Merge

La estrategia theirs es **lo opuesto a ours**, es decir, en caso de conflicto, Git elegirá los cambios de la rama que estás fusionando,
dejando de lado los de tu rama actual.

```bash
git merge -s theirs feature
```

## 📌 Tags

- `git tag`: Listar tags en ordern alfavetico.

- `git tag -l pattern`: Listar tags en ordern alfavetico de un **pattern** en concreto.

- `git fetch tag`: **Fetch** todos los tags del repositorio remoto.

- `git tag --sort=-version`: Ordenar los tags por si version.

- `git tag -n`: Mostrar las anotacions de los tags con su descripcion

## 📌 Remotos

Son las copias de tu repositorio que podemos tener en nuestro `PC`. Que significa esto. Que podemos tener el mismo repositorio 
varias veces en nuestro `PC` signandole un nombre distinto a cada copia.

- **`git remote -v`**: Muestra los remotos configurados.

- **`git remote add <nombre> <url>`**: Añade un remoto.

- **`git remote remove <nombre>`**: Elimina un remoto.

- **`git remote set-url <nombre> <nueva-url>`**: Cambia la URL de un remoto.


## 📌 Patching

### PATCH

- `git add --patch`: Recorre cada una de las diferencias que encuentra en el codigo sin tener en cuenta los ficheros nuevos y los va a
  passar a otra "Area" que no es ni stage ni working es otro universo (pero que forma parte de stage). Después de esto podremos hacer 
  commit solo de esta "Area
  - Nos ayuda en ordenar por distintos commits todo el codigo generado.
  - No permite añadir ficheros nuevos.

Para añadir los cambios lo haremos con un commit. Pero hay más.

Si queremos ver los cambio que hemos añadido no lo podemos hacer con `git diff`, ya que este solo nos va ha mostrar los que esten 
en el working directory. Tendremos que hacerlo con `git diff --stage` que nos mostrará los cambios que esta en el "Area" stage.

Si queremos desacer algun cambio el lo añadido con `-p` lo tendremos que hacer con `git restore --stage`, pudiendo también hacerlo 
con el atributo `--patch` para hacer lo solo por trocitos como lo hemos hecho al añadirlo.

### FORMAT-PATCH

- `git format-patch`: Se usa para generar parches con metadatos de commits completos.

- `git format-patch -n HEAD-3`: Esto generará 3 archivos de parche, uno por cada commit desde HEAD~3 hasta HEAD.
  - Los archivos tendrán nombres como: ["0001-Nombre-del-commit.patch", "0002-Otro-commit.patch"]
  - Se pueden enviar a otros desarrolladores, quienes pueden aplicarlos con `git am`.

- `git am <nombre_fichero>.patch|diff`: Mantiene historial y metadatos de los commits.

#### Opciones útiles:

* `-n`: → Número de commits a exportar.
* `--stdout`: → Genera la salida en un solo archivo en lugar de varios.
* `--cover-letter`: → Crea una carta de presentación con detalles de los parches.
* `--subject-prefix="PATCH"`: → Agrega un prefijo al asunto del parche.

```bash
# Esto genera un único archivo cambios.patch en vez de múltiples.
git format-patch -n HEAD~3 --stdout > cambios.patch
```

#### Cuándo usar git format-patch?

* Cuando necesitas enviar commits a alguien sin un repositorio remoto.
* Para contribuir a proyectos de código abierto que aceptan parches por correo.
* Para guardar cambios en formato de parches antes de hacer un `rebase` o `reset`.

### FORMAT-PATCH | MAIL

 - `git format-patch --stdout HEAD~3 | mail -s "Parche para revisión" usuario@example.com`: Esta variante permite enviar los 
   parches directamente por correo electrónico.
   - `--stdout`: Envía la salida del parche a la entrada estándar en lugar de generar archivos.
   - `mail -s "Parche para revisión" usuario@example.com`: Usa un cliente de correo en la terminal para enviarlo.

### DIFF

- **`git diff`**: Se usa para generar/mostrar diferencias entre versiones de archivos o commits.

- `git diff <ID_COMMIT>`: Muestra las diferencias entre el codigo que tengo en bruto y el commit seleccionado y los siguientes 
  hasta el último hecho. Así que el codigo que sera mucho mayor.

- `git diff <tag>...<tag_2>`: Nos mostrará la diferencia entre estas dos versiones.
  - `--stat`: [MODO RESUMEN] Añadiendo este parametro nos mostrará los nombres de los ficheros y el número líneas afectadas.

- **`git diff --staged`**: Muestra las diferencias entre archivos en staging y el último commit.

- `git diff > <nombre_fichero>.patch|diff`: Se guarda en un fichero.

- `git apply <nombre_fichero>.patch|diff`: Se usa para aplicar parches generados con `git diff`.
  - Se applica desde el fichero.  
  - **Limitación**: No incluye información de nuevos archivos ni commits, solo cambios dentro de archivos existentes
  - ****: No se si es necesario añadir `<` después del apply para desile que inserte el contenido de este fichero. Al congtrario 
    que el guardado del diff a un fichero.

- `git apply`: Este se queda a la espera del codigo que le entremos.
  - Nos permite aplicar codigo de un diff pegandolo directamente en la terminal.

### Diferencias Clave entre `git format-patch` y `git diff`

| Característica          | `git format-patch` | `git diff` |
|------------------------|-------------------|------------|
| Incluye metadatos de commit | ✅ | ❌ |
| Permite aplicar cambios con `git am` | ✅ | ❌ |
| Genera archivos de diferencias | ✅ | ✅ |
| Útil para compartir commits enteros | ✅ | ❌ |


### CRERRY-PICK

- `git cherry-pick <commit-hash>`: Se usa para aplicar un commit específico a otra rama.
  - **Ventaja**: Útil para mover cambios sin necesidad de crear un parche.

### REBASE

- `git rebase <rama>`: Se usa para reordenar, modificar o mover commits.
  - **Ventajas**: Mantiene la historia más limpia sin "merges" innecesarios.

#### ¿Cuál usar?

* **Para compartir cambios sin repositorio remoto**: `git format-patch` + `git am`

* **Para aplicar cambios locales sin commits**: `git diff` + `git apply`

* **Para aplicar un commit específico**: `git cherry-pick`

* **Para reordenar historia**: `git rebase`

### RESET

- **`git reset --hard <commit>`**: Revierte el repositorio a un commit, eliminando cambios posteriores.

- **`git reset --soft <commit>`**: Revierte el repositorio sin perder los cambios en **staging**.


## 📌 Debbugging

- **`git blame`**: Este comando muestra quién fue el autor de cada línea de un archivo y en qué commit se hizo ese cambio. 
  Es ideal para rastrear la historia de cambios en una línea específica de código
- **`git grep`**: Sirve para buscar texto específico en tu repositorio. 
  Es mucho más rápido y poderoso que usar un simple grep porque trabaja directamente con la base de datos de Git.
  - `-n`: Muestra el número de línea donde aparece el texto.
  - `--heading`: Agrupa los resultados por archivo.
  - `--count`: Muestra cuántas veces aparece el texto por archivo.
- **`git grep "console.log" HEAD~1`**: Esto buscará en el commit anterior al actual.

## 📌 Guardar Cambios Temporales

- **`git stash`**: Guarda temporalmente los cambios no confirmados.

- **`git stash pop`**: Aplica los cambios guardados y los elimina.

- **`git stash list`**: Muestra la lista de stashes guardados.

- **`git stash apply`**: Aplica un stash guardado sin eliminarlo.

- **`git stash drop`**: Elimina un stash guardado.

## 📌 Submódulos

- **`git submodule add <url> <directorio>`**: Añade un submódulo.

- **`git submodule update --init --recursive`**: Inicializa y actualiza submódulos.

- **`git submodule deinit <directorio>`**: Desinicializa un submódulo.

- **`git submodule foreach <comando>`**: Ejecuta un comando en cada submódulo.

## 📌 Buenas prácticas y herramientas avanzadas

- **`git commit --amend`**: Editar el último commit

- **`git rebase nombre-rama`**: Rebasing

## 📌 Otros Comandos Útiles

- **`git clean -f`**: Elimina archivos no rastreados.

- **`git reflog`**: Muestra el historial de todas las acciones de Git.

- **`git shortlog`**: Muestra un resumen de commits agrupados por autor.

- `git log`: Listado de commits.

- `git log --oneline`: Lista de commits en una sola linea mostrando solo su descripción.

- `git log --graph`: Lista en forma de grafica como las ramas actuan sobre si.