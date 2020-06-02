# Leccion 1 - Temario

* [Instalacion de python y agregar al path, documentacion](#instalacion)
* Python en terminal
* VSCODE editor de texto, configuracion
* Tipos de datos
* Strings o cadenas de caracteres
* Modulos, como funcionan, primer import
* [Bonus](#bonus)

### Instalacion de python y agregar al path, mas documentacion

1. Python ultma vertsion para windows [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Agregar al path python [https://www.kyocode.com/2019/10/agregar-python-path-windows/](https://www.kyocode.com/2019/10/agregar-python-path-windows/)
3. Documentacion oficial ultima version ptyhon [https://docs.python.org/3/](https://docs.python.org/3/)

### Python en terminal
Despues de haber agregado correctamente al path la ruta del ejecutable de python podremos abrir en la terminal un interprete, pude ser en CDM o PowerShell, para esto en la terminal escribimos simplemente python o el nombre de su ejecutable
```
PS C:\Users\user1> python38
Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
En mi caso el ejecutable se llama python38, que es la ultima version de python, esto sucede porque ya tengo versiones previas de python instaladas en mi sistema.
Dentro de este interprete podremos escribir codigo de python simplemente para probar o hacer operaciones sencillas
```
Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 1+1
2
>>> "this is a string"
'this is a string'
>>>
```
### VScode editor de codigo
1. Link de descarga [https://code.visualstudio.com/](https://code.visualstudio.com/)

### Tipos de datos
Para esta parte veremos la utilidad de la funcion ```type()``` que viene incluida en el core de python, este metodo nos retorna el tipo de clase del argumento.
```
Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 1+1
2
>>> "this is a string"
'this is a string'
>>> 1.56
1.56
>>> type('this is a strings')
<class 'str'>
>>> type(1+5)
<class 'int'>
>>> type(1.5+2.64)
<class 'float'>
>>>
```
### Strings o cadenas de caracteres
Los sitrings en python son secuencias inmutables esto quiere decir que los strings como tal no se pueden modificar, a continuacion veremos como podemos escribir una string en python
```
Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 'esto es una cadena'
'esto es una cadena'
>>> "esto tambien es una cadena"
'esto tambien es una cadena'
```
En python podmeos escribir de 2 formas una cadena, la primera es con comillas simples **''** y la segunda con comillas dobles **""**, la diferencia radica en que si nosotros queremos usar comillas simples dentro de un strings deberiamos usar comillas dobles
```
Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> "esto es una cadena con 'comillas simples'"
"estos es una cadena con 'comillas simples'"
```
Automaticamente vemos como python cambia el output y nos lo muestra con comillas dobles, tambien se puede usar el caracter de escape **\\'** para imprimir comillas simple dentro de comillas simples, lo veremos mejor en el siguiente ejemplo
```
Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 'comillas simples \'\' dentro de comillas simples'
"comillas simples '' dentro de comillas simples"
```
Como vemos con la diagonal invertida se escapa el caracter y se vuelve imprimible

Las cadenas son arreglos de caracteres por lo tanto podemos seleccionar cierto rango o cierto caracter conociendo su indice, recordemos que la cuenta siempre empeiza en 0.
Operaciones con cadenas
```
Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>"hola " + " mundo!" #el simbolo + concatena las cadenas de caracteres
'hola mundo!'
>>> 'esto es una cadena'[1] #queremos el indice 1 de la cadena y como output nos da la s
's'
>>> 'esto es una cadena'[1:15] # podemos indicar un rango de inicio y fin para traernos un pedazo de esa cadena
'sto es una cad'
>>> 'esto es una cadena'[-5] #podemos usar numeros negativos para inicar de derecha a izquierda
'a'
>>> 'esto es una cadena'[-6:-2] #de igual forma podemos utilizar inicio y fin
'cade'
>>> 'esto es una cadena'[::-1] #de esta forma pones una cadena al reves
'anedac anu se otse'
>>> len('esto es una cadena') #esta funcion nos trae el largo de una secuencia, cadena, tubla, etc
18
```

### Modulos, como funciona, import
Para usar librerias o modulos que nos faciliten la programacion o agreguen utilidades o funcionalidades a nuestros scripts podemos importar modulos de 2 maneras:
Para este caso usaremos el **string module de python** documentacion [https://docs.python.org/3/library/string.html](https://docs.python.org/3/library/string.html)

**Los imports siempre van al inicio de un archivo por convencion pero se pueden hacer en cualquier parte del codigo siempre y cuando se importe antes de usar el modulo y sus caracteristicas**
```python
import string #con esta primer forma importamos todo el modulo como tal, esto quiere decir con todos sus metodos, constantes, etc

import string as st #esta forma es igual que la anterior, solo que la palabra as le agrega un alias, de esta forma podemos personalizar su llamada

from string import ascii_uppercase #con esta forma decimos que del modulo string import solo la constante ascii_uppercase, de esta manera solo tendremos acceso a eso que importamos

from srting import * #de esta forma le decimos que importe todo
```

### Bonus
En python se utiliza el **#** como simbolo antes de un comenrario esto quiere decir que esa linea el interprete no la leera

la implementacion de ocmentarios con comillas triles esta erronea

```python
# comentario en una sola linea

print('Hola mundo!') #comentario en linea de codigo, esta funcion imprime a pantalla

'''
comentado bloques de codigo con triple comilla simple, este tipo de comentario no es uno como tal, python lo toma como una literal string de varias lineas, asi que lo interpreta
'''
"""
o triple comilla doble, lo mismo con esto
"""

```
