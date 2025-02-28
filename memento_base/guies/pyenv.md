# PYENV

<!-- TOC INICIO -->
- [PYENV](#pyenv)
- [PYENV](#pyenv)
<!-- TOC FIN -->

# PYENV

* Descargamos Pyenv y lo ejecutamos
```bash
curl https://pyenv.run | bash
```

* Exportamos Pyenv al PATH del sistema
```bash
export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

* Refrescamos la ventana del terminal
```bash
exec "$SHELL"
# or
bash
```

* Install python*
```bash
# List versions
pyenv install -l

# Install version
pyenv install *.*.**

# :warning: Si queremos utilizar PyInstaller debemos utilizar la siguiente opción
env PYTHON_CONFIGURE_OPTS="--enable-shared" pyenv install 3.11.9

# Make --global [NOT USE]
pyenv virtualenv *.*.** {name}

# Activar entorno virtual
pyenv activate {name}
```

* Upgrade

```bash
brew upgrade pyenv

brew uninstall pyenv
brew install pyenv --head
```

* Update

```bash
pyenv update

cd $(pyenv root)
git pull

cd $(pyenv root)
git fetch
git tag
git checkout v0.1.0
```

* Uninstall

```bash
rm -rf $(pyenv root)

brew uninstall pyenv
```

* Verificar

```bash
which pyenv
echo $PATH | grep --color=auto "$(pyenv root)/shims"
```

* Add interpreter
  * Para pyenv
    * Settings
      * Python Interpreter
        * Dropdown menu 
          * show all 
            * click on `+` 
              * search (Base interpreter ...) 
                * /Users/emiligarriga/.pyenv/versions
