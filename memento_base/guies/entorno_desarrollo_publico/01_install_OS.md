<!-- TOC INICIO -->
- [01. Instalar S.O.](#01-instalar-so)
  - [Paquetes del Sistema](#paquetes-del-sistema)
  - [Instal·lació OpenVPN network manager](#installació-openvpn-network-manager)
<!-- TOC FIN -->

# 01. Instalar S.O.

Recomendamos el uso de Ubuntu, ya que es el que utilizamos nosotros. Esta guía debería servir para todas las distribuciones Debian.

Una vez instalado, actualizaríamos el listado de paquetes y actualizaríamos:

```bash
sudo apt update
sudo apt upgrade
```

## Paquetes del Sistema

Se requieren los siguientes paquetes, para empezar:

- openvpn, para conexiones en la red de la empresa
  - Paquetes: `openvpn, network-manager-openvpn` i possiblemente `network-manager-openvpn-gnome`
- python, necessario para desarrollar en Python
  - Paquetes: `python, python-dev, python-pip`
- tmux, multiplexor de terminal
  - Paquete: `tmux`, `terminator`
- git, necesario para el control de versiones y el desarrollo contínuo
  - Paquete: `git`

Ejecutaríamos:

```bash
sudo apt install git vim htop curl openssh-server
```

## Instal·lació OpenVPN network manager

> [MD](../VPN.md)
> 
> [RFC](https://rfc.gisce.net/t/manual-configuracio-de-vpn-amb-el-network-manager/898)


```bash
sudo apt-get install openvpn network-manager-openvpn network-manager-openvpn-gnome
```

Això ens permet poder afegir VPNs compatibles amb OpenVPN.

**Configuració VPN a Ubuntu**

* Obrim Settings > Network (Red)
  * Fem click a afegir una VPN 
    * Triem la opció de importar-la des d'un arxiu.

* Seleccionem el `.ovpn` que ens interessi 
  * Hi escribim la contrasenya a la pestanya `Identity` amb la opció `Certificates (TLS)`.

* Dins la pestanya IPv4 seleccionem la opció:
  * `Use this connection only for resources on this network` per tal de poder tenir més de una VPN activa a la vegada.

* A l'hora de connectar-la només cal clicar-hi a sobre o utilitzar:
```bash
nmcli con up id NomDeLaConnexio
```