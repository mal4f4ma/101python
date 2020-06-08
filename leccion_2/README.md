# Leccion 2 - Variables, ingresar desde taclado, secuencias inmutables y mutables

* Variables, constantes
* Ingresar datos por teclado
* Inmutables
  * Strings, si de nuevo
  * Tuples
* Mutable
  * List
  * range

### Variables, constantes
Las variables en python pueden ser cualquier palabra o convinacion de mayusculas, minusculas, numeros o guion bajo, solo deben de cumplir con lo siguiente:
* Empezar por una letra o guion bajo
* Nunca use símbolos especiales como !, @, #, $, %, etc.
* No ser una palabra reservada de python

Las constantes son variables con valor fijo que preferiblemente no se deben de modificar, se forman con la misma reglas de las variables, pero por convencion van en mayusculas

### Datos por teclado
para ingresar datos por teclado tenemos la funcion integrada ```input()```, esta siempre nos dara el valor ingresado como string, por lo que hay que tener cuidado al momneto de operar con dicho valor

### Tipos de datos y estructuras inmutables
Esto quiere decir que sus valores no pueden ser rememplazados o tener una asignacion

#### Tupla
La tupla es un objeto, tipo de dato o estrutura de datos del tipo secuencias, es decir una lista inmutable, ya que no puede modificarse despues de su creacion

### Mutables

#### Lista
Uno de los objetos mas versatiles son las listas, que almacenan objetos y estos pueden ser de distintos tipos.
a su vez cuentan con distinas funciones
- append - agrega un elemnto al final
- count - cuenta los elemntos que recibe como argumento
- extend - agrega todos los elemntos de un iterable al final de la lista
- index - devuelve el indice de la primera ocurrencia del argumento
- insert - agrega un elemento a la lista en el indice dado, recibe 2 params y los demas se recorren
- pop - saca el ultimo elemnto de la listas- remove - borra la primera ocurrencia del elemnto que recibe como parametro
- reverse - invierte el orden de la lista
- sort - ordena de manera ascendente, con el argumento reverse=True lo ordena descendente
- list - convierte a lista un objeto iterable
- remove - elimina de la lista el elemento que se le es pasado por parametro,

#### Range
La función range() devuelve una lista conteniendo una progresión aritmética de enteros.
