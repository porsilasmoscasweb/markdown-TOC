# TOC

Generamos un TOC sobre la ruta proporcionada.

* Argumentos _(OPCIONALES)_:
  * `--toc`: **BOOLEAN** generará el TOC de la ruta definida (Esta puede depender si algun otro parametro varia la ruta de destino 
    como es el caso de _copy_ o _output_dir_).
  * `--copy`: **???** Hará una copia del directorio base y sateará el destino de toda acció a la nueva dirección.
    * Esta se genera de dos maneras:
      * Con una ruta pasada por parametro.
      * En caso de no pasar ruta por parametro, añade el sufijo **_copy** al final de la _ruta base_.
  * `--output_dir`: **???** Hará una copia del directorio base y sateará el destino de toda acció a la nueva dirección.
    * Esta se genera de tres maneras:
      * Con una ruta pasada por parametro.
      * En caso de no pasar ruta por parametro, pero si se ha definido el parametro **--copy** no se hara nada.
      * En caso de no pasar ruta por parametro, añade el sufijo **_copy** al final de la _ruta base_.
  * `--toc_files`: **BOOLEAN** generará un TOC por cada uno de los archivos `.md` que encuentre dentro de la ruta proporsionada.
  * `--ignorar`: **LISTA** separado por espacios, le podemos indicar directorios y/o archivos, los cuales van a ignorarse al 
    generar tanto el TOC general como el de cada archivo `.md` en caso de usar el parametro `--files`.
  * `--toc_sort`: **BOOLEAN** los archivos `.md` pueden incluir una cabezera `[//]: <> (order:asc|desc)` indicando que esta va a ser 
    ordenada en la forma elegida previamente antes de generarse el TOC del archivo. 
    * En caso de que no se pase el parametro `--files` solo se ejecutará el sort **y la creación del nuevo TOC en caso de existir** 
      en los archivos donde se encuentre la cabezera.
  * `--html`: **STRING** HAcemos una copia de los archivos `.md` en formato HTML. Se generará una ruta de salida nueva que podrá 
    ser parte del parametro o en su ausencia crearse a través de la ruta proporcionada añadiendole un sufijo `_hmtl`.
    * :warning: Se intentará darle estilo al HTML a demás de que el TOC de cada archivo en caso de existir genere un nuevo estilo de 
      slug adecuado a HMTL.

## Requerimientos

Para poder correr los scripts será necessario tener instalados estos programas y librerias:

* python = 3.11.9
  * pytest 
  * pytest-mock
