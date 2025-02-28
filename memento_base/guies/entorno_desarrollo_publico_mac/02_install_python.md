# 02. Instalamos Python 2.7 i pyenv

<!-- TOC INICIO -->
- [02. Instalamos Python 2.7 i pyenv](#02-instalamos-python-27-i-pyenv)
- [02. Instalamos Python 2.7 i pyenv](#02-instalamos-python-27-i-pyenv)
  - [Install python 2](#install-python-2)
  - [Install MacPorts [???]](#install-macports-)
<!-- TOC FIN -->

# 02. Instalamos Python 2.7 i pyenv

El ERP se ejecuta sobre Python 2.7, aunque se espera que en un futuro no muy lejano se ejecute sobre Python 3. 
Eso obliga a que el Sistema Operativo cuente con una versión 2.7 de Python, aunque sea para poder crear entornos virtuales para desarrollar.

## Install python 2 

[Download python 2.7.18 - macOS 64-bit installer](https://www.python.org/downloads/release/python-2718/)

[Install pyenv](../programs/mac/pyenv.md)

* Install

```bash
# brew install openssl readline sqlite3 xz zlib tcl-tk
brew install openvpn network-manager-openvpn meld 
```

## Install MacPorts [???]

```bash
sudo port install pkgconfig gdbm tcl tk +quartz
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
