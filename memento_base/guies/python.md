# PYTHON

<!-- TOC INICIO -->
- [PYTHON](#python)
- [PYTHON](#python)
  - [PIP](#pip)
  - [CODIFICACIÓN](#codificación)
  - [CREAR FICHERO EJECUTABLE](#crear-fichero-ejecutable)
  - [BYTEIO o STRINGIO](#byteio-o-stringio)
  - [PALABRAS RESERVADAS](#palabras-reservadas)
  - [VAR _](#var-_)
  - [VAR local y global](#var-local-y-global)
  - [ORD() Y CHR()](#ord-y-chr)
  - [EVAL()](#eval)
  - [EXEC()](#exec)
  - [INPUT](#input)
  - [PRINT](#print)
    - [Exemplos desconocidas](#exemplos-desconocidas)
  - [STYLE LOG](#style-log)
    - [Text style](#text-style)
    - [Text color](#text-color)
  - [FUNCIONS](#funcions)
    - [Parametros](#parametros)
    - [Con un número variable de parámetros](#con-un-número-variable-de-parámetros)
    - [Con parámetros que contienen diccionarios](#con-parámetros-que-contienen-diccionarios)
    - [Generadas a partir de otras](#generadas-a-partir-de-otras)
    - [Orden superior](#orden-superior)
    - [Generadores](#generadores)
    - [Decorador](#decorador)
  - [TIPADOS](#tipados)
    - [FUNCIONES](#funciones)
    - [TIPOS COMPLEJOS](#tipos-complejos)
    - [ALIAS](#alias)
    - [FUNCIONES CON MÚLTIPLES VALORES DE ENTORNO](#funciones-con-múltiples-valores-de-entorno)
    - [ANOTACIONES PARA VARIABLES CON VALORES DE DISTINTOS TIPOS](#anotaciones-para-variables-con-valores-de-distintos-tipos)
<!-- TOC FIN -->

# PYTHON

## PIP

Lo que vindria a ser (ARCHIVA de JAVA)

PIP es un sistema de gestión de paquetes utilizado para instalar y administrar paquetes de software escritos en Python. 
Muchos paquetes pueden ser encontrados en el Python Package Index (PyPI). Python 2.7.9 y posteriores (en la serie Python2), 
Python 3.4 y posteriores incluyen pip (pip3 para Python3) por defecto.

Només és pot installa llibreries des de `pip` sino que també es pot realitzar a través de `github` de la següent manera:

```bash
pip install <link_html>
```

## CODIFICACIÓN

Todos los archivos de python tienen estar comentados con alguna codificación. Un ejemplo sería:

```python
# -*- coding: utf-8 -*-
```

## CREAR FICHERO EJECUTABLE

Es necesario añadir el PATH en nuestro archivo `./bashrc`. `export PATH=$PATH:/home/carpetaprograma`
Para que le documento sea ejecutable se necesitarà dar permisos a este `chmod +x <filename>.py`

* En la primera línea del documento se indica cual es la ruta de python.
* En la segunda linea definimos en que `encoding` esta el fichero.

```python
#!/home/egarriga/.virtualenvs/erp/bin/python
# -*- coding: utf-8 -*-

val = input('insert')
a = val*10
print(a)
```

## BYTEIO o STRINGIO

Segons el fitxer amb el que estiguem treballan haurem de tenir en compte si aquest es encoding o byte a l'hora de l'importar

```python
# b'' Byte
from io import BytesIO

# u'' String
try:
    # Python 2
    from cStringIO import StringIO
except ImportError:
    # Python 3
    from io import StringIO
```

## PALABRAS RESERVADAS

PAara ver cuales son podemos ejecutar:

```python
import keyword
print(keyword.kwlist)
```

Resultado:

['and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'exec', 'finally', 
'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'not', 'or', 'pass', 'print', 'raise', 'return', 
'try', 'while', 'with', 'yield']


## VAR _

seria como usar i o x o z en los loop, cualquier iteracion puede ser usada

for _ in range(0,10)

a, *_, b[1,2,3,4,5,6,7]

en python >>> la podemos usar para guardar el utlimo valor obtenido en una operación en la que no se asigno el valor a ninguna variable

5+5
_
10

## VAR local y global

Una variable local se declara en su ámbito de uso (en el programa principal y dentro de una función) y 
una global fuera de su ámbito para que se pueda utilizar en cualquier función que la declare como global.

```python
# Define función
def acelerar():
    # Declara la variable 'km' como global
    # Ahora se podrá utilizar dentro de la función
    global km
    
    # Declara variable local (ámbito función)
    tiempo = 1

    # Se incrementa la velocidad en 5 km
    km+= 5

# Define variable local (ámbito programa principal)
km = 10

# Muestra variable 'km'
print('Velocidad:', km)  # velocidad: 10

# Llama a la función acelerar()
acelerar()

# Muestra variable 'km'
print('Velocidad:', km)  # velocidad: 15

# Intenta mostrar la variable 'tiempo'
# Se produce una excepción (error) de tipo NameError
# porque la variable no pertenece a este ámbito:
# NameError: name 'tiempo' is not defined
print('Tiempo:', tiempo)
```

## ORD() Y CHR()

La función ord() devuelve el ordinal entero del carácter indicado y justo lo contrario hace 
la función chr() que devuelve el carácter (Unicode) que representa al número indicado.


ord('$')  # 36

chr(36)  # '$'

## EVAL()

La función eval() se utiliza para evaluar cadenas de texto que pueden contener expresiones o distintos tipos de 
estructuras de datos que pueden utilizarse con Python, tales como listas, tuplas, diccionarios y otros objetos que admiten asignación.

cadena1 = "Cuba"
cadena2 = "Costa Rica"
print(cadena1.isalpha())   # True
print(cadena1.isalnum())   # True
print(cadena1.isdecimal())   # False
print(cadena1.isspace())   # False
print(cadena2.istitle())   # True
if cadena1.isalpha():
    print("Todos los caracteres que contiene son alfabéticos")

## EXEC()

La función exec() permite ejecutar código Python contenido en una cadena o en un archivo. Si el código no cumple con las reglas del lenguaje producirá una excepción. 

```python
exec('secreto = input("Introducir clave secreta: ")')
exec('if secreto == "1234": print("¡Eureka!")')
exec('print("Clave secreta:", secreto)')
```

> El término exec en Python 2.x forma parte del conjunto de palabras reservadas del lenguaje. 
> Sin embargo, en Python 3.x exec() es una función y ya no forma parte de tan distinguido grupo


## INPUT

Assosiar valor dinamic a una variable

```python

try:
    articulos = int(input('Teclear articulos: '))
    precio = int(input('Teclear precio: '))
    print('Pagar ', str(articulos*precio), '€')
except:
    print('Error, deben ser números') 
```

## PRINT

### Exemplos desconocidas

```python
# muestra redondeo con 2 y 3 decimales
val1 = 8.56767  # asigna flotante
val2 = 9.45548  # asigna flotante
print('{0:.3} {1:.4}'.format(val1, val2))

# muestra: Valor aproximado
valor = 2.34565676  # asigna flotante 
print('Valor aprox. {0:.3f}'.format(valor))  # 2.346

# rellena con guiones bajos
print('{0:_^30}'.format('Sevilla'))

# rellena con ceros a la izquierda:
codpais = 34  # asigna número
print(str(codpais).zfill(4))  # 0034

# declara diccionario
correos = {'SJ' : 300, 'LR': 309, 'B': 310}
for loc, cp in correos.items():  # recorre diccionario
    # muestra lista de pares con formato
    print('{0:5}:{1:4d}'.format(loc, cp))

# Utilizando comodines: 
# %s (cadena), %i (entero), %f (número con decimales)
nombre = 'Claudio'
edad = 35
altura = 1.82
print('Tiene %i años' %edad)
print('%s tiene %i años y mide %1.2f' %(nombre, edad, altura))

# tabulado de datos
personas = [('Claudio', 35, 1.826),
            ('Elena', 24, 1.84),
            ('Manuel', 9, 1.449),
            ('Isabel', 34, 1.72)]
for persona in personas:
    nombre = persona[0]
    edad = persona[1]
    altura = persona[2]
    print('%-12s tiene %2i años y mide %1.2f' %(nombre, edad, altura))
```

## STYLE LOG

### Text style 

| Estilos* | Cod. ANSI |
|--------|-----------|
| Sin efecto	| 0 |
| Negrita	| 1 |
| Débil	| 2 |
| Cursiva	| 3 |
| Subrayado	| 4 |
| Inverso	| 5 |
| Oculto	| 6 |
| Tachado	| 7 |

### Text color
                         
| Colores | Texto | Fondo |
|--------|------|----|
| Negro | 30 | 40 |
| Rojo | 31 | 41 |
| Verde | 32 | 42 |
| Amarillo | 33 | 43 |
| Azul | 34 | 44 |
| Morado | 35 | 45 |
| Cian | 36 | 46 |
| Blanco | 37 | 47 |

<details>
<summary>Taula ejemplo</summary>

```python
def construye_tabla_formatos():
    for estilo in range(8):
        for colortexto in range(30,38):
            cad_cod = ''
            for colorfondo in range(40,48): 
                fmto = ';'.join([str(estilo), 
                                 str(colortexto),
                                 str(colorfondo)]) 
                cad_cod+="\033["+fmto+"m "+fmto+" \033[0m" 
            print(cad_cod)
        print('\n')

construye_tabla_formatos()
```
</details>


## FUNCIONS

### Parametros

Si queremos que los parámetros deban indicarse sin nombre pondremos los pondremos a la izquierda de la barra '/'.
Si no es así se producirá una excepción de tipo TypeError:

```python
# x, y se declaran sin nombre
# z se puede declarar con nombre
def funcion2(x, y, /, z):
    return x + y + z
```

AL contrario. Si queremos que los paramatros se declaren con nombre los declararemos a la derecha del estarisco '*'.

```python
# x, y se pueden declarar sin nombre
# z es obligado que se declare con nombre
def funcion4(x, y, *, z):
    return x + y + z
```

### Con un número variable de parámetros

```python
def distancia(*tramos): # define función con nº variable de parámetros
    ''' Suma distancia de tramos '''  # cadena de documentación
    total = 0  # inicializa variable numérica 
    for distancia in tramos:  # recorre, uno a uno, los tramos...
        total = total + distancia  # … y acumula la distancia
    return total  # devuelve la suma de todos los parámetros

tramo1 = 10
print(distancia(tramo1, 20, 30, 40))  # la función devuelve 100 
print(distancia())  # la función retornará el valor 0
```

### Con parámetros que contienen diccionarios

```python
def porc_aprobados(aprobados, **aulas):
    ''' Calcula el % de aprobados '''
 
    total=0
    for alumnos in aulas.values():
        total += alumnos
 
    return aprobados * 100 / total

porcentaje_aprobados = porc_aprobados(48, A = 22, B = 25, C = 21)
print(porcentaje_aprobados)
```

### Generadas a partir de otras

```python
def area_triangulo(base, altura):  # define función con dos parámetros
    ''' Calcular el área de un triangulo'''  # cadena de documentación
    return base * altura / 2  # devuelve el resultado de la expresión
print(area_triangulo(6, 4))  # la función retornará el valor 12
print(area_triangulo(3.5, 2.4))  # la función retornará el valor 4.2

at = area_triangulo  # la función calcula área de un triángulo  
print(at(10,4))  # la nueva función usa los argumentos base y altura
```

### Orden superior

Estas tienen en su interior otras funciones definidas que se seran llamadas por parametro y los paramtro de estas mismas 
esteran entre parentesis.

Podemos crear la nuestras o usa las ya existentes como serian:
* `map()`: map(function_superior, parametros)
* `filter()`: filter(function_superior, parametros)
* `reduce()`: reduce(function_superior, parametros)
* `lambda`: lambda x: x*x
* `comprencion_list`: [valor ** 3 for valor in range(1,11)]

```python
# Funcion superior
def conversor(sis):
    """"
    El parametro es el que dara valor de funcion a la clave del dict() `sis_func`
    """
    def sis_bin(numero):
        print('dec:', numero, 'bin:', bin(numero))
 
    def sis_oct(numero):
        print('dec:', numero, 'oct:', oct(numero))
   
    def sis_hex(numero):
        print('dec:', numero, 'hex:', hex(numero))
  
    sis_func = {'bin': sis_bin, 'oct': sis_oct, 'hex': sis_hex}
    return sis_func[sis]

# Crea una instancia del conversor hexadecimal
conversorhex = conversor('hex')

# Convierte 100 de decimal a hexadecimal. Executando la funcion `sis_hex(numero)`
conversorhex(100)

# Otro modo de usar el conversor. 
# Convierte 9 de decimal a binario
conversor('bin')(9)
```

### Generadores

Los generadores funcionan de forma parecida a la comprensión de listas pero no devuelven listas sino generadores.
Un generador es una clase especial de función que genera valores sobre los que iterar. 
La sintaxis usada es como la usada en la comprensión de listas pero en vez de usar corchetes se utilizan paréntesis. 
Para devolver los valores se utiliza yield en vez de return.

```python
# Define generador
def generador(inicio, fin, incremento):
    while(inicio <= fin):
        yield inicio  # devuelve valor
        inicio += incremento

# Recorre los valores del generador
for valor in generador(0, 6, 1):
    # Muestra valores, uno a uno:
    print(valor)  # 0 1 2 3 4 5 6

# Obtiene una lista del generador
lista = list(generador(0, 8, 2))

# Muestra lista
print(lista)  # [0,2,4,6,8]
```

### Decorador

Es una función que recibe una función como parámetro y devuelve otra función como valor de retorno. 
Se utiliza cuando es necesario definir varias funciones que son muy parecidas. 
La función devuelta actúa como un envoltorio (wrapper) resolviendo lo que sería común a todas las funciones. 
También se aplica a clases.

```python
# Define decorador
def decorador1(funcion):
    # Define función decorada
    def funciondecorada(*param1, **param2):
        print('Inicio', funcion.__name__)
        # Funcio creidada amb el decorador
        funcion(*param1, **param2)
        print('Fin', funcion.__name__)
    return funciondecorada

@decorador1
def suma(a, b):
    print(a + b)
    
@decorador1
def producto(arg1, arg2):
    print(arg1 * arg2)

suma(1,2)
producto(5,5)
```

## TIPADOS

Python no tiene tipado como tal peró se puede documentar una variable para un mejor seguimiento del codigo.
El intérprete de Python almacena las anotaciones de tipo en el atributo especial `__annotations__`:

```python
repetir: int = 3
cadena: str

cadena = repetir * 'Hola'
print(repetir)   # 3
print(cadena)   # HolaHolaHola
```

```python
print(__annotations__)  # {'repetir': class int, 'cadena': class str}
```

### FUNCIONES

Para anotar los tipos en una clase se aplica a sus atributos la misma sintaxis que a las variables y a las constantes; y a sus métodos la misma que a las funciones:

```python
class Juego:
    tiempo: int = 40
    
    def __init__(self, nom: str, nivel: int, jug: int = 1) -> None:
        self.nom= nom
        self.nivel = nivel
        self.jug = jug
                 
    def duracion(self) -> int:
        return self.jug * Juego.tiempo
    
partida = Juego('Ajedrez', 1, 2)
print(partida.duracion())  # 80
```

### TIPOS COMPLEJOS

Para anotar tipos más complejos como listas, tuplas, diccionarios, conjuntos y otros es necesario utilizar el módulo typing 
e importar los tipos que correspondan, como en el ejemplo que sigue. Para describir el tipo de una lista se importa List y 
entre corchetes se anota el tipo "[tipo]" de los elementos a contener, en este caso str. Para el tipo del diccionario se 
importa Dict y entre corchetes "[tipo_clave, tipo_valor]" se indica los tipos de las claves y de los valores separados por una coma ",". 
Para describir un conjunto se importa Set y entre corchetes se indica el tipo "[tipo]" de los valores a contener. 
También, se pueden utilizar en otro ámbito, como en la función del ejemplo imprime_rios(), para indicar que el argumento rios recibe una lista de cadenas str:

```python
from typing import List, Dict, Set

apellidos: List[str] = ['Alcantara', 'Alonso', 'Blanco']
referencias: Dict[str, int] = {'Mesa': 121, 'Silla': 485}
serie: Set[int] = {1, 1, 1, 2, 2, 3, 3, 5, 5, 5, 5, 5, 6}


def imprime_rios(rios: List[str]) -> None:
    for rio in rios:
        print(rio)

imprime_rios(['Guadalquivir', 'Tinto', 'Odiel', 'Segura'])
```

### ALIAS

Los alias permiten la creación de anotaciones de tipo con denominaciones propias para mejorar la comprensión del código

```python
from typing import Tuple

Color = Tuple[int, int, int]

def pintar(color: Color) -> None:
    r: int
    v: int
    a: int
    r, v, a = color
    print('Color Rojo:', r, 'Verde:', v, 'Azul:', a)

pintar((100, 200, 120))
```

### FUNCIONES CON MÚLTIPLES VALORES DE ENTORNO

Cuando una función devuelve múltiples valores el tipo del retorno se anota como una tupla con los tipos de sus valores 
separados por comas, o por un tipo personalizado basado en la misma construcción: Tuple[tipo, tipo, ...]

```python
from typing import Tuple

Coordenada = Tuple[int, int]

def coordenada_inicial() -> Coordenada:
    return 0, 0

print(coordenada_inicial())
```

### ANOTACIONES PARA VARIABLES CON VALORES DE DISTINTOS TIPOS

Para variables que pueden tener valores de distinto tipo existen las anotaciones predefinidas Optional y Union. 
Optional se utiliza con variables que pueden ser de un tipo concreto o de ninguno (None). 
Y Union es apropiado para variables cuyos valores pueden ser de tipos diferentes, excepto None.

```python
from typing import Optional

Votos = Optional[int]
Representantes = Optional[int]

def representantes(votos: Votos) -> Representantes:
    if votos:
        return votos // 5000
    else:
        return None

print(representantes(None))  # None
print(representantes(3409))  # 0
print(representantes(11231))  # 2
```

```python
# En la función recuento() el valor de retorno es de tipo Optional[str, float]. 
# Esto significa que el valor que retorna la función puede ser de tipo str o float: 

from typing import Union

Recuento = Union[str, float]

def recuento(inicio: bool, actual: int, final: int) -> Recuento:
    if not inicio:
        return 'Escrutinio no iniciado'
    else:
        return round((actual * 100 / final), 2)

print(recuento(False, 0, 0))  # Escrutinio no iniciado
print(recuento(True, 4560, 9800))  # 46,53
```

> VER MÁS EN: [Mypy source](https://github.com/python/mypy)
> 
> EJEMPLO EN: [Sample source](./mypy.py)

