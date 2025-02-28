# 01. Instalar S.O.

<!-- TOC INICIO -->
- [01. Instalar S.O.](#01-instalar-so)
- [01. Instalar S.O.](#01-instalar-so)
  - [Paquetes del Sistema](#paquetes-del-sistema)
<!-- TOC FIN -->

# 01. Instalar S.O.

## Paquetes del Sistema

* brew
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install wget

or 

brew update
```

* iTerm2 [OPCIONAL]
```bash
brew install --cask iterm2
```

* Basicos
```bash
brew install curl git vim tmux openssh-server

# Install MacPorts if you don't already have it, then:
sudo port install git htop
```

* conexions VPN

<details>
<summary>Open VPN</summary>

***

* Openvpn
  * Go to System Preferences -> Sharing, enable Remote Login
  * [Source](https://openvpn.net/connect/)
  * Ejecutar
  * Importar file *_mac.ovpn

<details> 
<summary>Comentar las siguientes líneas en fichero "*_mac.ovpn"</summary>

```bash
# SSL/TLS parms.
# See the server config file for more
# description.  It's best to use
# a separate .crt/.key file pair
# for each client.  A single ca
# file can be used for all clients.
#ca ca.crt
#cert client.crt
#key client.key
# Verify server certificate by checking that the
# certicate has the correct key usage set.
# This is an important precaution to protect against
# a potential attack discussed here:
#  http://openvpn.net/howto.html#mitm
#
# To use this feature, you will need to generate
# your server certificates with the keyUsage set to
#   digitalSignature, keyEncipherment
# and the extendedKeyUsage to
#   serverAuth
# EasyRSA can do this for you.
remote-cert-tls server
# If a tls-auth key is used on the server
# then every client must also have the key.
#tls-auth ta.key 0
```

</details>



* Openssh [???]
```bash
# Install OpenSSH
brew install openssh

# Generate a New SSH Key
ssh-keygen -t rsa

# Configure the SSH Configuration File
vim ~/.ssh/config

# Add the following lines to the file
Host * StrictHostKeyChecking no

# Create a New SFTP User
sudo dscl . -create /Users/sftpuser sudo dscl . -create /Users/sftpuser UserShell /usr/bin/false sudo dscl . -create /Users/sftpuser RealName "SFTP User" sudo dscl . -create /Users/sftpuser UniqueID 550 sudo dscl . -create /Users/sftpuser PrimaryGroupID 20 sudo dscl . -create /Users/sftpuser NFSHomeDirectory /Users/sftpuser sudo dscl . -create /Users/sftpuser Password "*"

# Configure SFTP
sudo vim /etc/ssh/sshd_config

# Add the following lines to the file
Match User sftpuser ChrootDirectory /Users/sftpuser ForceCommand internal-sftp AllowTcpForwarding no

# Start the OpenSSH SFTP Server
sudo launchctl load -w /System/Library/LaunchDaemons/ssh.plist
```

***

</details>

<details>
<summary>TUNNEL BLICK</summary>

***

* Descargar i instal·lar [Source](https://tunnelblick.net/downloads.html)
* Ejecutar
* Botó dret sobre file *_mac.ovpn 
  * obre amb tunnerblinck

***

</details>