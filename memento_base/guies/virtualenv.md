<!-- TOC INICIO -->
- [PYTHON](#python)
  - [ENTORN VIRTUAL (virtualenv)](#entorn-virtual-virtualenv)
  - [ENTORN VIRTUAL (Workon)](#entorn-virtual-workon)
<!-- TOC FIN -->

# PYTHON

## ENTORN VIRTUAL (virtualenv)

* Instal·lem entorns vistuals per python 3
```bash
sudo apt install python3.10-venv
```

* Des d'on tenim instal·lada la carpeta dels entorn virtuals
```bash
cd ~/.virtualenvs
```

* Borrar un entorn virtual
```bash
rm -rf ~/.virtualenvs/cchloader3/
```


* Crear un entorn virtual amb `python`
```bash
mkvirtualenv -p /usr/bin/python env_name
or
mkvirtualenv -p /usr/bin/python3 env_name
```

> Atributs:
> 
> * `-p`: interpreter based on what to create environment (path/identifier) 
>   * by default use the interpreter where the tool is installed - first found wins (default: [])
> * `/usr/bin/python`: Versió de python
> * `env_name`: Nom de l'entorn virtual


```bash
python -m venv env_name
or
python3 -m venv env_name
```

> Atributs:
> 
> * `python`: Versió de Python que utilizarem
> * `-m`: run library module as a script (terminates option list)
> * `venv`: tag per defecte
> * `env_name`: Nom de l'entorn virtual

## ENTORN VIRTUAL (Workon)

* Install pip3 and virtualenv
```bash
sudo apt-get install python3-pip
pip3 install virtualenv
```

* Install virtualenvwrapper
```bash
pip3 install virtualenvwrapper
```

* Set environment variables in your shell configuration file (usually ~/.bashrc or ~/.zshrc)
```bash
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_VIRTUALENV=/usr/local/bin/virtualenv
```

* Load virtualenvwrapper:
```bash
source ~/.local/bin/virtualenvwrapper.sh
```

* Verify the installation by activating a new virtual environment
```bash
mkvirtualenv myenv
```

This will create a new virtual environment named `myenv` and activate it. You can deactivate it with deactivate 
and list all available virtual environments with workon or lsvirtualenv.

> **NOTE:**
> 
> Make sure to replace /usr/local/bin/virtualenv with the actual path to the virtualenv executable on your system if it’s different.



