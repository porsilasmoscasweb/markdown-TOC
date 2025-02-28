<!-- TOC INICIO -->
- [05. Instalación del cliente web](#05-instalación-del-cliente-web)
<!-- TOC FIN -->

# 05. Instalación del cliente web

> [WEBCLIENT](https://rfc.gisce.net/t/deploy-webclient-local-development/1248) (Configurar el servidor ERP)

*  Cal tener instalado el protocolo `MSGPACK`

> Nota: Cal assegurar-se d’instal·lar tot el següent l’Entorn Virtual relatiu al ERP

<details>
<summary>MSGPACK</summary>

Para activar en el servidor ERP la utilización del protocolo MsgPack 7 se puede hacer de la siguiente forma

Se deben tener instalados los siguiente paquetes:

* Sistema
```bash
sudo apt install libev-dev
```

* Python
```bash
pip install bjoern msgpack flask "flask-cors < 4.0"
```

* variables de entorno
```bash
OPENERP_MSGPACK=1
OPENERP_MSGPACK_HOST=0.0.0.0
OPENERP_MSGPACK_PORT=8068
```

</details>

Hem de tenir la variable d’entorn OPENERP_SECRET amb un string qualsevol

* Abrimos el fichero bashrc
```bash
vim ~/.bashrc
```

* Definimos la varible
```bash
OPENERP_SECRET="whatever"
```

* Reiniciamos el bash
```bash
source ~/.bashrc
```

* Comprobamos que se a creado correctamente
```bash
echo $OPENERP_SECRET
```

* Instalamos paquestes de python en la carpeta del repositorio `erp`
```bash
# cd ~/home/<usuario>/proyectos/erp
pip install -r server/bin/msgpackapi/requirements.txt
```

* Tenir instal·lat nodejs (ho podem fer amb nvm) amb l’usuari erp
```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
```

* Recarrergar la shell
```bash
exec $SHELL
```

* Instal·lar la versió de nodejs
```bash
nvm install v20.5.0
```

* Clonar el repositori
```bash
# cd /home/<usuario>/proyectos 
git clone git@github.com:gisce/webclient.git -b v2
cd webclient
```

* Si tenim el repositori clonat de fa temps, recordar de canviar-nos a la branca v2
```bash
git checkout v2
```

* Instal·lar dependències
```bash
npm ci
```

* Crear el fitxer de configuració .env fent els canvis que considerem
```bash
cp .env.sample .env
```

* Arrancar el client
```bash
npm start
```

Si al anar a iniciar sessió al client web, no us apareix el vostre host, l’heu de crear manualment amb el botó “Añadir host personalizado”. 
Poseu el nom que volgueu i com a “host” el servidor d’ERP que esteu corrent. http://localhost:8068/

