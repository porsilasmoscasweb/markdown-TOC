<!-- TOC INICIO -->
- [Instal·lació OpenVPN network manager](#installació-openvpn-network-manager)
<!-- TOC FIN -->

# Instal·lació OpenVPN network manager


```bash
sudo apt-get install network-manager-openvpn-gnome
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
