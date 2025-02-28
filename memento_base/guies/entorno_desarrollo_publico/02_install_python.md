<!-- TOC INICIO -->
- [02. Instalamos Python 2.7](#02-instalamos-python-27)
<!-- TOC FIN -->

# 02. Instalamos Python 2.7

El ERP se ejecuta sobre Python 2.7, aunque se espera que en un futuro no muy lejano se ejecute sobre Python 3. 
Eso obliga a que el Sistema Operativo cuente con una versión 2.7 de Python, aunque sea para poder crear entornos virtuales para desarrollar.


* Instalamos repositorios necesarios para Pyenv
```bash
sudo apt install -y make build-essential libssl-dev \
zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev \
wget curl llvm libncursesw5-dev xz-utils tk-dev \
libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev libpq-dev
```

* Descargamos Pyenv y lo ejecutamos
```bash
curl https://pyenv.run | bash
```

* Exportamos Pyenv al PATH del sistema
```bash
echo -e 'export PYENV_ROOT="$HOME/.pyenv"\nexport PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo -e 'eval "$(pyenv init --path)"\neval "$(pyenv init -)"' >> ~/.bashrc
```

* Refrescamos la ventana del terminal
```bash
exec "$SHELL"
```

* Install python2
```bash
sudo apt install python2
```

* Comprobamos la versión de Pyenv
```bash
pyenv --version
```

* (Opcional) Es posible actualizar Pyenv con el siguiente comando
```bash
pyenv update
```

* Instalamos la versión de Python 2.7
```bash
pyenv install 2.7.18
```

* Establecemos la versión de Python 2.7 como el Python por defecto
```bash
pyenv global 2.7.18
```

* El siguiente comando devería mostrar que el sistema usa la  versión deseada
```bash
python --version
```

* Descargamos e instalamos pip
```bash
curl https://bootstrap.pypa.io/pip/2.7/get-pip.py --output get-pip.py
python get-pip.py
```

* [Opcionales] (utilizados por GISCE-TI)
```bash
sudo apt install tmux openvpn network-manager-openvpn meld terminator
```

<details>
<summary>Para distribuciones de Ubuntu desde 20.04 hasta 21.10 "python-pip" debe instalarse de forma alternativa, pues no viene incluido en los paquetes.</summary>

https://linuxize.com/post/how-to-install-pip-on-ubuntu-20.04/#installing-pip-for-python-2

```bash
sudo add-apt-repository universe
sudo apt update 
sudo apt install python2
sudo apt install python python-dev
```

</details>

<details>
<summary>Para Ubuntu 22.04 en adelante, python 2.7 tiene por nombre python</summary>

```bash
sudo apt install python2 python2-dev
```

* Instalamos el pip

```bash
curl https://bootstrap.pypa.io/pip/2.7/get-pip.py --output get-pip.py
sudo python2 get-pip.py
```

</details>
