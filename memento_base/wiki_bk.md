[//]: <> (order:asc)

<!-- TOC INICIO -->
- [WIKI](#wiki)
  - [SSH (Secure Shell)](#ssh-secure-shell)
      - [Características clave](#características-clave)
      - [Uso común](#uso-común)
  - [SWAP](#swap)
      - [Funcionamiento](#funcionamiento)
  - [NUCLEOS DE UN ORDENADOR](#nucleos-de-un-ordenador)
      - [Funcionamiento](#funcionamiento)
      - [VISUALIZACIÓN DE LOS PROCESOS EN UN ORDENADOR](#visualización-de-los-procesos-en-un-ordenador)
  - [POSTGIS (la extensión para datos espaciales)](#postgis-la-extensión-para-datos-espaciales)
      - [Sierve para](#sierve-para)
  - [WAYLAND](#wayland)
  - [NGINX](#nginx)
    - [FITXER CONFIG](#fitxer-config)
  - [X11 (x.org)](#x11-xorg)
  - [CLUSTER](#cluster)
  - [SABT (supervisión avanazada de baja tensión)](#sabt-supervisión-avanazada-de-baja-tensión)
  - [PIP](#pip)
    - [PIPCOVERALL](#pipcoverall)
    - [SETUPTOOLS](#setuptools)
  - [RTU](#rtu)
  - [CINI](#cini)
  - [RECORE](#recore)
  - [SERVEI AUXILIAR RECORE](#servei-auxiliar-recore)
  - [COVERAGE](#coverage)
  - [ERP](#erp)
    - [Cómo funcionan los sistemas de ERP](#cómo-funcionan-los-sistemas-de-erp)
  - [TRAFO](#trafo)
  - [TIMESCALE](#timescale)
  - [psycopg2](#psycopg2)
  - [PYTHON](#python)
    - [Us](#us)
    - [Python es caracteritza per ser un llenguatge:](#python-es-caracteritza-per-ser-un-llenguatge)
    - [Conceptes fundementals](#conceptes-fundementals)
  - [GITHUB](#github)
  - [virtualenvwrapper (LIB)](#virtualenvwrapper-lib)
  - [TMUX](#tmux)
  - [CNEA](#cnea)
  - [CYTHON](#cython)
  - [OOJS-UI.js](#oojs-uijs)
  - [POWERERPjs](#powererpjs)
  - [MESSAGEAPCK (MsgPack)](#messageapck-msgpack)
  - [GTK](#gtk)
  - [XML-RPC](#xml-rpc)
  - [PANDAS](#pandas)
    - [Pandapower](#pandapower)
  - [PYPOWER](#pypower)
  - [NETWORK](#network)
  - [STAND-ALONE _(autónomo)_](#stand-alone-_autónomo_)
  - [PUDB](#pudb)
  - [PEP8](#pep8)
  - [ERPPEEK](#erppeek)
  - [LOOPBACK](#loopback)
  - [DIRECCIÓ IP](#direcció-ip)
  - [Border Gateway Protocol _(BGP)_](#border-gateway-protocol-_bgp_)
  - [INTERFAZ](#interfaz)
  - [TCP/IP](#tcpip)
<!-- TOC FIN -->

# WIKI

## E-SIOS

[WEB](https://www.esios.ree.es/es/pvpc)

...

## SSH (Secure Shell)

SSH (Secure Shell) es un protocolo de comunicación seguro que permite acceder de forma remota a servidores y sistemas informáticos,
garantizando la integridad y confidencialidad de la información durante el proceso de conexión. Fue creado en 1995 por Tatu Ylonen 
como respuesta a un robo de contraseñas en un servidor de la Universidad de Finlandia, donde el tráfico viajaba sin cifrar.

#### Características clave

* **Cifrado**: SSH cifra todos los datos que se envían entre el cliente y el servidor, lo que evita que terceros intercepten y accedan a la información.
* **Autenticación**: Requiere autenticación para conectar al servidor, lo que garantiza que solo los usuarios autorizados puedan acceder.
* **Conexión segura**: SSH establece una conexión segura entre el cliente y el servidor, protegiendo contra ataques de tipo “man-in-the-middle” y evitando la manipulación de datos en tránsito.

#### Uso común

SSH se utiliza comúnmente para:

* Acceder a servidores remotos para realizar tareas de administración y mantenimiento.
* Transferir archivos de manera segura.
* Realizar desarrollo y depuración de aplicaciones en servidores remotos.
* Configurar y modificar servidores y sistemas informáticos.

En resumen, SSH es un protocolo de acceso remoto seguro que garantiza la integridad y confidencialidad de la información
durante el proceso de conexión, permitiendo a los usuarios acceder y administrar servidores y sistemas informáticos de forma segura y remota.

## SWAP

El swap, también conocido como espacio de intercambio, es un área en el disco duro que se utiliza como un sustituto de 
la memoria virtual (RAM) cuando la memoria física (RAM) del ordenador se encuentra llena. Es un espacio en el disco duro 
que se utiliza para almacenar datos temporales cuando la memoria RAM no está disponible.

#### Funcionamiento

Cuando un programa o proceso requiere más memoria que la disponible en la RAM, el sistema operativo utiliza el swap 
para almacenar los datos temporales en el disco duro. Esto permite que el programa o proceso continúe ejecutándose, 
aunque no esté utilizando la memoria RAM. Cuando la memoria RAM se libera, los datos almacenados en el swap se recuperan 
y se vuelven a cargar en la memoria RAM.


## DIFENTES PARTES DEL SISTEMA

### CPU (Central Processing Unit)

La CPU, o Unidad Central de Procesamiento, es el componente central de un dispositivo electrónico que actúa como su cerebro, 
encargándose de ejecutar instrucciones y realizar operaciones de procesamiento de datos. 

Esta unidad es fundamental para que los ordenadores, servidores, teléfonos móviles y otros dispositivos electrónicos funcionen correctamente. 

La CPU gestiona el flujo de electricidad a través de los circuitos integrados y ejecuta las instrucciones de los programas, 
incluyendo las relacionadas con la gráfica y la inteligencia artificial

### GPU (graphics Processing Unit)

Una GPU, o unidad de procesamiento gráfico, es un circuito electrónico especializado en el procesamiento de gráficos y operaciones de coma flotante. 

Su función principal es aliviar la carga de trabajo de la unidad central de procesamiento (CPU) en aplicaciones que requieren alto rendimiento gráfico, 
como videojuegos o aplicaciones 3D interactivas. Las GPUs son excelentes para el procesamiento en paralelo, 
lo que las hace ideales para tareas complejas como la inteligencia artificial, la simulación científica y la minería de criptomonedas.

### ALMACENAMIENTO

#### ALMACENAMIENTO PRIMARIO RAM (Memoria de Acceso Aleatorio)

Es la memoria principal de un dispositivo donde se almacenan de forma temporal los datos de los programas que estás utilizando en 
este momento. La RAM, que significa Memoria de Acceso Aleatorio, es un tipo de memoria que se encuentra en cualquier dispositivo, 
desde ordenadores de sobremesa hasta teléfonos móviles. Cuanta más RAM tenga tu equipo, mejor será su rendimiento ya que podrás gestionar más aplicaciones a la vez.

Existen dos tipos principales de memoria RAM: 
* Las memorias DDR (Double Data Rate) [Mejor]
* Las SDR (Single Data Rate)

#### ALMACENAMIENTO SECUNDARIO

Es no volátil y permite la conservación de datos a largo plazo. 

Incluye dispositivos como:
* Discos duros (HDD): Un dispositivo de almacenamiento de datos que almacena información de forma magnética. Aunque son 
  dispositivos confiables, los HDD pueden volverse lentos y son más susceptibles a los daños físicos en comparación con las SSD.
* Unidades de estado sólido (SSD): Utiliza memoria flash para almacenar datos y es más rápida, duradera y silenciosa que los HDD. 
  Las SSD son ideales para mejorar el rendimiento de los ordenadores portátiles y de escritorio.
 
Las SSD son más rápidas que los HDD, ofreciendo mejoras considerables en la transferencia de datos.

#### ALMACENAMIENTO EN LA NUBE

Es una opción moderna que permite almacenar y acceder a datos a través de Internet, ofreciendo una alternativa flexible y segura para el almacenamiento de datos.

### SWAP (ESpacio de Intercambio)

El espacio de intercambio, también conocido como swap, es una parte de la memoria virtual del sistema que se utiliza para almacenar 
temporalmente los procesos que no están en uso activo en la memoria RAM. Este espacio puede tomar la forma de una partición de disco o un archivo en el disco duro. 
El uso del espacio de intercambio permite al sistema operativo liberar memoria RAM para cargar otros procesos, lo que es especialmente útil cuando la memoria RAM se agota.


#### Recomendaciones para la Tamaño del Espacio de Intercambio

* Mínimo de 1 GB: Para sistemas con menos de 1 GB de RAM.
* 4 a 8 GB: Independientemente de la cantidad de memoria RAM disponible, el sistema puede trabajar normalmente con de 4 a 8 GB de 
  espacio de intercambio.

## CUELLOS DE BOTELLA

Para solventar los cuellos de botella en programación, es importante identificar primero dónde se encuentran estos problemas. 
Los cuellos de botella pueden surgir en diferentes partes del sistema, como la CPU, la GPU, la memoria RAM o el almacenamiento. 

Aquí te presento algunas estrategias para abordar estos problemas:

* **Tecnologia LOW CODE**: La tecnología Low Code puede ser una herramienta clave para resolver cuellos de botella, ya que permite a 
  los equipos de cualquier área formarse para no depender exclusivamente de IT para resolver bloqueos.
* **Automatización**: Automatizar procesos puede ayudar a reducir la carga de trabajo y evitar cuellos de botella.
* **Monitoreo y diagnóstico**: Utiliza herramientas de monitoreo para detectar y diagnosticar cuellos de botella en tiempo real. Esto 
  te permitirá tomar medidas rápidas para resolverlos.


## NUCLEOS DE UN ORDENADOR

En informática, los núcleos (también conocidos como cores) son la unidad básica de procesamiento de un procesador (CPU). 
Es la parte más importante del procesador, donde se procesa la información del sistema computacional y se envían 
instrucciones a los demás componentes del sistema.

#### Funcionamiento

Un núcleo es una unidad de procesamiento que realiza determinadas acciones. Cada acción que ejecutas en tu ordenador 
es procesada por tu CPU, sin importar lo pequeña o grande que sea la tarea. Los núcleos trabajan en paralelo, 
lo que significa que pueden realizar varias tareas al mismo tiempo, lo que mejora el rendimiento general del sistema.

#### VISUALIZACIÓN DE LOS PROCESOS EN UN ORDENADOR

Para ver el funcionamiento de los nucleos de nuestro ordenador lo podemos hacer desde `terminal` con el comando `htop`.

## TECNOLOGIA LOW CODE  

Forma de crear applicaciones de forma rápida y barata. 

Es un proceso accesible que permite a personas sin conocimientos avanzados de programación desarrollar aplicaciones rápidamente. 

Como el **Dreamweaber** de la epoca. Creación de aplicaciones a través de `drag and grop` Arrastramos la funcionalidad que queremos 
usar y esta se escrive.

Para empresas pequeñas que necessitan desarrollar muchao app de forma rapida es aconsejable.

Para empresas grandes no es aconsejable porque tiene mucho bug de seguridad

## SENTRY

## POSTGIS (la extensión para datos espaciales)

Uno de los puntos más relevantes es la capacidad de almacenar y trabajar con datos de tipo geométrico. Para ello surge PostGIS: la extensión espacial para PostgreSQL, una herramienta impulsada por OsGEO.

Se trata de un módulo de ampliación indispensable para PostgreSQL a la hora de trabajar en proyectos GIS.

La extensión PostGIS permite dotar a la base de datos relacional PostgreSQL de una serie de ventajas. Entre otros, destacan:

soporte para archivos GIS ráster y vectoriales.
provee funciones de análisis, transformación y consulta espaciales.
velocidad de procesamiento gracias a índices espaciales.
herramientas de geocodificación, 3D, topología, cálculo de rutas…

#### Sierve para

La extensión PostGIS habilita el soporte para trabajar con objetos geográficos localizados en el espacio.

En otras palabras: convierte PostgreSQL en una base de datos espacial, que en la práctica funciona 
(quitando el apartado gráfico) exactamente como un auténtico Sistema de Información Geográfica de escritorio.

## WAYLAND

> [WIKI](https://victorhckinthefreeworld.com/2023/09/19/wayland-vs-x11-en-linux/)

Wayland es un conjunto de protocolos que rigen cómo un compositor gráfico de un sistema operativo dibuja cosas en la pantalla (ventanas, botones, etc) y cómo las aplicaciones interactúan con la infraestructura de dibujo en la pantalla del compositor.

Es similar a los protocolos HTTP y SMTP que rigen cómo los navegadores web y los clientes de correo electrónico envían y reciben páginas web y datos.

Wayland también incluye una implementación de esos protocolos en un conjunto de bibliotecas extremadamente livianas llamadas libwayland-client y libwayland-server que ofrecen API estables y versionadas. Aplicaciones y compositores como KWin de KDE y Mutter de GNOME utilizan esas API para hacer cosas.

## WSGI

WSGI significa Web Server Gateway Interface. Es una especificación común para servidores web que permite que diferentes 
servidores web y frameworks de aplicaciones interactúen según una API común, 
permitiendo así la comunicación entre el servidor web y la aplicación web.

En otras palabras, WSGI es un estándar que define cómo se comunica un servidor web con una aplicación web, 
y cómo se pueden encadenar diferentes aplicaciones web para procesar una solicitud o petición (o request). 
Esto permite a los desarrolladores crear aplicaciones web que sean compatibles con diferentes servidores web, 
como Apache, Nginx, Microsoft IIS, entre otros.

En resumen, WSGI es un estándar que facilita la comunicación entre servidores web y aplicaciones web en Python, 
permitiendo la compatibilidad y la escalabilidad de las aplicaciones web.


## NGINX



### FITXER CONFIG

> [WIKI](https://linuxconfig.org/how-to-enable-disable-wayland-on-ubuntu-22-04-desktop)

* Editar el fitxer
```
sudo nano /etc/gdm3/custom.conf
```

* Habilitar o no el `wayland`
```
WaylandEnable=true
```

* Reiniciar
```
sudo systemctl restart gdm3
```

## X11 (x.org)


## CLUSTER


## SABT (supervisión avanazada de baja tensión)


## PIP

Lo que vindria a ser (ARCHIVA de JAVA)

PIP es un sistema de gestión de paquetes utilizado para instalar y administrar paquetes de software escritos en Python. 
Muchos paquetes pueden ser encontrados en el Python Package Index (PyPI). Python 2.7.9 y posteriores (en la serie Python2), 
Python 3.4 y posteriores incluyen pip (pip3 para Python3) por defecto.

### PIPCOVERALL



### SETUPTOOLS

Nos proporciona todo lo necesario para distribuir nuestros propios módulos e incluso nos permite publicar paquetes en el respositorio público PyPI (Python Package Index) de forma directa desde la propia terminal.

## RTU

## CINI

## RECORE

Activitat de producció d’energia elèctrica, de no més de 50 MW de potència, a partir de fonts d’energia:

Renovable
Cogeneració
Residus

## SERVEI AUXILIAR RECORE

Contracta per consum mínim d'un RECORE. 

Tot RECORE té un mínim consum per fer anar les màquines que generen l'electriciat. Pel que ens necessari que tinguin un contracta associat.

## COVERAGE

Percentage de codi que forma part d'un TEST.

## ERP

El término ERP, o software ERP, se refiere a Enterprise Resource Planning, que significa “sistema de planificación de recursos empresariales”. El software ERP sirve para hacerse cargo de distintas operaciones internas de una empresa, desde producción a distribución o incluso recursos humanos. Un paquete ERP automatiza los procesos empresariales, aumentando la productividad y reduciendo los costes. Los datos actuales sobre producción, compras y ventas, logística y administración pueden enlazarse para que los procesos se controlen automáticamente y funcionen así con mayor eficacia.

### Cómo funcionan los sistemas de ERP

Un sistema de ERP –también llamado "suite de ERP"– está compuesto por módulos integrados o aplicaciones de negocio que se hablan entre sí y comparten una base de datos común.

Cada módulo de ERP generalmente se enfoca en un área del negocio, pero todos trabajan juntos usando los mismos datos para cumplir con las necesidades de la empresa. Finanzas, contabilidad, recursos humanos, ventas, procurement, logística y cadena de suministro son puntos de partida populares. Las empresas pueden elegir el módulo que deseen y agregar y escalar según sea necesario.

Los sistemas de ERP también admiten requisitos específicos de la industria, ya sea como parte de la funcionalidad central del sistema o a través de extensiones de aplicaciones que se integran fluidamente con la suite.

## TRAFO

Vulgarment dit "Transformador".


## TIMESCALE

Timescale es una base de datos de series temporales creada para manejar grandes volúmenes de datos que cambian con el tiempo. Las series temporales son datos que están indexados por tiempo, como registros de sensores, datos financieros, registros de eventos, etc.

Timescale combina las ventajas de una base de datos relacional con la escalabilidad y flexibilidad necesarias para trabajar con datos temporales a gran escala. Está construida como una extensión de PostgreSQL, lo que significa que se puede utilizar con las herramientas y el lenguaje SQL que ya conoces y aprovechar la robustez de PostgreSQL.

## psycopg2

Psycopg2 es un adaptador de base de datos para PostgreSQL diseñado para ser compatible con la mayoría de las versiones de Python. Permite a los desarrolladores de Python interactuar con bases de datos PostgreSQL de manera eficiente y sencilla.

Psycopg2 es una extensión del lenguaje de programación Python que proporciona acceso a las bases de datos PostgreSQL. Permite ejecutar consultas SQL, gestionar transacciones, trabajar con tipos de datos específicos de PostgreSQL y manejar errores de manera efectiva.

## PYTHON

Python es un lenguaje de programación de código abierto, creado por Guido van Rossum en 1991. Se trata de un lenguaje orientado a objetos, fácil de interpretar y con una sintaxis que permite leerlo de manera semejante a como se lee el inglés. Es un lenguaje interpretado, esto significa que el código de programación se convierte en bytecode y luego se ejecuta por el intérprete, que, en este caso, es la máquina virtual de Python.

> Treballar amb el “ipython” de l’entorn visual “enviromenterp” `workon <repo>`.

### Us

* Strips i automatització.
* Desenvolupament de software.
* Anàlisis de dades.
* AI & maching learning.
* Blockchain.

### Python es caracteritza per ser un llenguatge:

* **Multiparadigma**: la programació imperativa, orientada a objectes i funcional.
* **Multiplataforma**: els sistemes operatius més populars tenen el seu propi intèrpret de Python, per la qual cosa es pot fer servir el mateix codi en Windows, Linux i macOS.
* **Tipat dinàmic**: les variables poden prendre valors de diferents tipus.
* **Interpretat**: el codi de Python no es compila en el llenguatge del processador, al seu lloc es necessita un programa intèrpret que l'executi.
            
### Conceptes fundementals

* **Encapsulació**: consisteix a empaquetar les variables i les funcions en un objecte únic, definint-les com una classe. Això ajuda a protegir les dades i evitar que el codi pugui ser alterat per tercers.
* **Abstracció**: és summament útil quan el programador vol bloquejar certes funcions i mètodes de la resta del codi. A més, redueix el nombre de funcions i mètodes necessaris, en simplificar el codi i minimitzar els efectes dels canvis.
* **Herència**: ajuda a reduir la redundància, ja que permet aplicar un conjunt de propietats i mètodes a múltiples objectes, en lloc d'haver de repetir aquestes propietats i mètodes cada vegada. Els objectes poden heretar la informació, reduint així la quantitat total de codi que el programador ha d'escriure.## Workon
* **Polimorfisme**: aporta flexibilitat, ja que, en comptes d'aplicar un mètode a un grup d'elements o objectes, els mètodes s'apliquen a objectes individuals i es poden executar de maneres diferents en funció del tipus d'objecte.The Workon command is a feature provided by the virtualenvwrapper tool for managing Python environments. It allows you to easily switch between different Python environments, and it also provides tab completion for the environment names.

## GITHUB

GitHub, Inc. és una plataforma de desenvolupadors impulsada per IA que permet als desenvolupadors crear, emmagatzemar i gestionar el seu codi. Utilitza programari Git, proporcionant el control de versions distribuït de Git més control d'accés, seguiment d'errors, sol·licituds de funcions de programari, gestió de tasques, integració contínua i wikis per a cada projecte.


## virtualenvwrapper (LIB)

virtualenvwrapper és un conjunt d'extensions de l'eina "virtualenv" d'Ian Bicking. Les extensions inclouen embolcalls per crear i suprimir entorns virtuals i, d'una altra manera, gestionar el vostre flux de treball de desenvolupament, de manera que és més fàcil treballar en més d'un projecte alhora sense introduir conflictes en les seves dependències.

* Per crear el venv 
```bash
mkvirtualenv <nom> -a <direcció del projecte>
```                     

* Eliminar venv 
```bash
rmvirtualenv <nom> 
```                          

* Per activar/desactivar venv 
```bash
# Activa
workon <enviroment>

# Desectiva
deactivate 
```            


## TMUX

Tmux és el que es coneix com un multiplexor de terminals que et permet crear, administrar i personalitzar sessions a la terminal de Linux. Amb TMUX, pots dividir el teu terminal en panells i finestres, mantenir sessions persistents fins i tot després de tancar la terminal, i accedir a múltiples sessions simultàniament. Aquesta flexibilitat i personalització fan de TMUX una de les meves eines preferides per millorar el meu flux de treball a la terminal.

## CNEA

Comisión Nacional de Energía Atómica

## CYTHON

La naturalesa fonamental de Cython es pot resumir de la següent manera: `Cython és Python amb tipus de dades C`.

Cython és Python: Gairebé qualsevol tros de codi Python també és vàlid. (Hi ha algunes limitacions, però aquesta aproximació servirà de moment.) El compilador de Cython el convertirà en codi C que fa trucades equivalents a l'API Python/C.

Però Cython és molt més que això, perquè es pot declarar que els paràmetres i les variables tenen tipus de dades C. El codi que manipula els valors de Python i els valors C es pot barrejar lliurement, i les conversions es produeixen automàticament sempre que sigui possible. El manteniment del recompte de referències i la comprovació d'errors de les operacions de Python també és automàtic, i tot el poder de les instal·lacions de gestió d'excepcions de Python, incloses les declaracions try-except i try-finally, està disponible per a vostè, fins i tot enmig de la manipulació de dades C.

## OOJS-UI.js

> [GITHUB](https://github.com/wikimedia/oojs-ui)

OOUI permet als desenvolupadors crear aplicacions i interfícies d'usuari web adaptables.

Està preparat per a l'internacionalització amb suport complet d'idiomes de dreta a esquerra, és accessible d'acord amb les Directrices d'Accessibilitat per al contingut web, i funciona de manera consistent en una multitud de navegadors.

La biblioteca OOUI conté:

widgets, dissenys i finestres llestes per utilitzar que es poden instanciar directament o ampliar fàcilment, una sortida compatible del servidor PHP per als casos en els que JavaScript no està disponible,
elements que es poden barrejar i combinar fàcilment per crear interfícies d'usuari a mesura OOUI està disponible a MediaWiki Core, així com a npm, Composer i a través de cdnjs.

OOUI implementa un tema "WikimediaUI", conforme a la guia d'estil de disseny de la Fundació Wikimedia. Les interfícies creades dins de MediaWiki utilitzen aquest tema de forma predeterminada, 
encara que diferents apariències de MediaWiki es poden anul·lar. 

La biblioteca es va crear originalment per a la interfície d'usuari de VisualEditor, además de OOjs primer (JavaScript orientat a objects, en inglés "Object-Oriented JavaScript," d'aquí el nom anterior de OOUI "OOjs UI") . Més tard s'amplià per servir a MediaWiki Core amb widgets implementats en PHP o interfícies adaptables en el projecte Contribucions avançades en mòbil.

## POWERERPjs

## MESSAGEAPCK (MsgPack)

MessagePack és un format de serialització binari eficient. Us permet intercanviar dades entre diversos idiomes com JSON. Però és més ràpid i petit. Els nombres enters petits es codifiquen en un únic byte, i les cadenes curtes típiques només requereixen un byte addicional a més de les pròpies cadenes.

## GTK

Oferint un conjunt complet d'elements d'interfície d'usuari, GTK és adequat per a projectes que van des de petites eines puntuals fins a suites d'aplicacions completes.


## XML-RPC

XML-RPC (Extensible Markup Language - Remote Procedure Call) és una especificació de protocol per a realitzar trucades RPC (trucades remotes en xarxes informàtices) amb l'ajuda del protocol de xarxa sense estat HTTP i el llenguatge de marcat XML que, en aquest cas , otorga el seu nom.
Mentre HTTP regula el transport de dades, XML s'utilitza per a la presentació de les dades. En la determinació de l'estàndard XML-RPC es va valorar, sobre tot, el fet de que es podia implementar sense gran esforç en diferents llenguatges de programació i plataformes de sistemes.


## PANDAS

[pandas.pydata.org](https://pandas.pydata.org/)

Pandas és una biblioteca de programari escrita per al llenguatge de programació Python per a la manipulació i anàlisi de dades. En particular, ofereix estructures de dades i operacions per manipular taules numèriques i sèries temporals. És programari lliure publicat sota la llicència BSD de tres clàusules.

### Pandapower

Pandapower es basa en la biblioteca d'anàlisi de dades pandas i la caixa d'eines d'anàlisi del sistema d'energia PYPOWER per crear un programa de càlcul de xarxa fàcil d'utilitzar destinat a l'automatització de l'anàlisi i l'optimització dels sistemes d'alimentació. 

El que va començar com un embolcall de comoditat al voltant de PYPOWER s'ha convertit en una caixa d'eines d'anàlisi de sistemes d'alimentació autònom amb una àmplia biblioteca de models de sistemes d'alimentació, un solucionador de flux d'energia millorat i moltes altres funcions d'anàlisi de sistemes d'alimentació.

## PYPOWER

## NETWORK

Es una red formada por un conjunto de ordenadores y programas de gestión que se conectan para compartir recursos e intercambiar información.

## STAND-ALONE _(autónomo)_

En el ámbito de los programas de software sería eso mismo, un programa que puede trabajar de manera autónoma, es decir, que se puede instalar y ejecutar, o simplemente ejecutar, en un sistema sin necesidad de nada más.

> NO LO ÉS

Para entender standalone podríamos hablar de qué no sería un programa standalone. Pensemos en una aplicación frontend que necesita del servidor para funcionar. Eso no sería una aplicación standalone porque aunque tú la tengas instalada en el sistema necesita de otro sistema para que funcione, por lo tanto necesitarías tener conexión a Internet para poder conversar con el servidor. Por tanto, no sería capaz de funcionar de manera autónoma. Todo software distribuido por tanto no sería standalone.

> ÉS

Un programa standalone sería entonces aquel que puedes ejecutar en un computador y que funciona por él mismo sin ningún otro requisito. Puedes desconectar Internet y sigue funcionando, y no necesita de acceso a otros sistemas en la red local, etc. por ejemplo un programa que no necesita de sistema operativo para poder funcionar, o una aplicación portable, que no necesita ser instalada para que funcione en un ordenador.

También otro uso podría ser un programa que no necesita ser interpretado para funcionar, ya que ese interpretador sería como otro software que tendría que estar instalado en el ordenador y por tanto el sistema no sería totalmente autónomo. Si ya se compila el software, por ejemplo, el código de C y se crea el ejecutable, entonces podría ser un programa standalone, si es que no requiere una vez compilado de otros sistemas para funcionar.

## PUDB

Pudb es un depurador de Python que destaca por su énfasis en la manipulación de excepciones y la navegación sencilla e intuitiva utilizando comandos de teclado. Ofrece una interfaz de línea de comandos (CLI) en lugar de una interfaz gráfica, lo que lo hace más ligero y adecuado para su uso en terminales.

Las características clave de Pudb incluyen:

* Control del depurador desde un terminal separado.
* Soporte para Python 3.6 y versiones más recientes, así como para Python 2.7 en versiones anteriores a 2019.2.
* Modo de post-mortem que facilita rastrear los últimos pasos de un programa que se bloquea o falla.
* Navegación por el código fuente utilizando teclas de cursor y comandos Vi.
* Compatibilidad con teclas de acceso rápido para realizar acciones comunes sin tener que escribir comandos completos.
* La posibilidad de enviar solicitudes de ayuda y parches a través de una lista de correo o como solicitudes de extracción en el repositorio de GitHub.

## PEP8

PEP8 és una guia d'estil per escriure codi Python. Proporciona convencions per anomenar variables, utilitzar espais en blanc, 
organitzar el codi i donar-li format per a la seva llegibilitat. Les directrius no són obligatòries, però ajuden a escriure 
codi que sigui fàcil de llegir i entendre

## ERPPEEK

ERPpeek és una biblioteca versàtil que us permet interactuar amb un servidor `Odoo` o `OpenERP` mitjançant la interfície 
estàndard XML-RPC o la interfície JSON-RPC. Podeu utilitzar ERPpeek per realitzar diverses tasques, com ara consultar dades 
o crear registres en un servidor Odoo.

## LOOPBACK

El dispositivo de red loopback es una interfaz de red virtual. Las direcciones del rango '127.0.0.0/8' son direcciones 
de loopback, de las cuales se utiliza, de forma mayoritaria, la '127.0.0.1' por ser la primera de dicho rango, añadiendo 
'::1' para el caso de IPv6 ('127.0.0.1::1'). Las direcciones de loopback pueden ser redefinidas en los dispositivos, 
incluso con direcciones IP públicas, una práctica común en los routers y son usualmente utilizadas para probar la capacidad 
de la tarjeta interna si se están enviando datos BGP.


## DIRECCIÓ IP 

Una dirección IP _(Internet Protocol)_ es una etiqueta numérica que identifica de manera lógica y jerárquica 
a una interfaz —habitualmente un dispositivo (computadora, laptop, teléfono inteligente)— conectada a la red, que utilice 
el protocolo de internet o que corresponda al nivel de red del modelo TCP/IP.1​ En principio se usa en la red global, 
aunque también para aplicaciones locales (como la identificación de un router en una red cerrada).

Una dirección IP tiene dos funciones principales: identificación de la interfaz de red y direccionamiento para su ubicación.

## Border Gateway Protocol _(BGP)_

Protocolo mediante el cual se intercambia información de encaminamiento entre sistemas autónomos. 

Por ejemplo, los proveedores de servicio registrados en Internet suelen componerse de varios sistemas autónomos y 
para este caso es necesario un protocolo como BGP.

## INTERFAZ
Una interfaz se utiliza en informática para nombrar a la conexión funcional entre dos sistemas, programas, dispositivos 
o componentes de cualquier tipo, que proporciona una comunicación de distintos niveles, permitiendo el intercambio de información. 
Esto es un ejemplo de la realidad virtua

## TCP/IP

El modelo TCP/IP es usado para comunicaciones en redes y, como todo protocolo, describe un conjunto de guías generales 
de operación para permitir que un equipo pueda comunicarse en una red. TCP/IP provee conectividad de extremo a extremo 
especificando cómo los datos deberían ser formateados, direccionados, transmitidos, enrutados y recibidos por el destinatario.