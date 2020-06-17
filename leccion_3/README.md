# Leccion 3 - operadores logicos, relacionales, ciclo for e if y practica

* Operadores de asignacion
* Operadores aritmeticos
* Operadores logicos
* for
* if
* Katas en codewars [https://www.codewars.com/](https://www.codewars.com/)

### Operadores de asignacion

| **Operador** | **Descripcon**                                            | **Ejemplo**    |
| ------------ | --------------------------------------------------------- | -------------- |
| =            | asigna el valor a una variable                            | ``` x = 15 ``` |
| +=           | suma un valor a la variable                               | ``` x += 2 ``` |
| -=           | resta el valor a la variable                              | ``` x -= 4```  |
| *=           | multiplica el valor a la variable                         | ``` x *= 5 ``` |
| /=           | divide el valor de la variable, da como sultado **float** | ```x /= 15```  |
| **=          | calcula el exponente de la variable                       | ```x **= 2```  |
| //=          | divide el valor de la variable, da como resultado **int** | ```x // = 3``` |
| %=           | calcula el modulo del numero                              | ``` x %= 2```  |

En el siguiente codigo se observa el comportamiento de **x**
```
PS C:\Users\user1\Documents\101python> python38
Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> x = 15
>>> x += 2
>>> x
17
>>> x -= 4
>>> x
13
>>> x *= 5
>>> x
65
>>> x /= 15
>>> x
4.333333333333333
>>> x **= 2
>>> x
18.777777777777775
>>> x //= 3
>>> x
6
>>> x %= 2
>>> x
0.0
>>>
```
### Operadotes aritmeticos
| **Operador** | **Descripcion**   | **Ejemplo**    |
| ------------ | ----------------- | -------------- |
| +            | Suma              | ```5 + 8```    |
| -            | Resta             | ```10 - 9```   |
| *            | Miltiplicacion    | ```5 * 8```    |
| **           | Exponente         | ```2 ** 8```   |
| /            | Division flotante | ```150 / 18``` |
| //           | Division entera   | ```150 / 18``` |
| %            | Modulo            | ```80 % 17```  |
En el siguiente codigo implementamos los operadores
```
PS C:\Users\user1\Documents\101python> python38
Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 5 + 8
13
>>> 10 - 9
1
>>> 5 * 8
40
>>> 2 ** 8
256
>>> 150 / 18
8.333333333333334
>>> 150 // 18
8
>>> 80 % 17
12
>>>
```
### Operadores relacionales
Estos solo devuelven ```True``` o ```False```

| **Operador** | **Descripcion**         | **Ejemplo**      |
| ------------ | ----------------------- | ---------------- |
| ==           | Son iguales a y b?      | ```17 == 80```   |
| !=           | Son diferentes a y b?   | ``` 17  != 80``` |
| <            | Es a menor que b?       | ```17 < 80```    |
| >            | Es a mayor que b?       | ```17 > 80```    |
| <=           | Es a menor o igual a b? | ```17 <= 80```   |
| >=           | Es a mayor o igual a b? | ```17 >= 80```   |
En el siguiente codigo podemos ver el resultado de cada operador
```
PS C:\Users\user1\Documents\101python> python38
Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 17 == 80
False
>>> 17 != 80
True
>>> 17 < 80
True
>>> 17 > 80
False
>>> 17 <= 80
True
>>> 17 >= 80
False
>>>
```
### Operadores logicos
Nos sirven para trabajor con valores booleanos.<br>
El resultado de cada operador depende de la table de verdad del mismo.
| **Operador** | **Descripcion**      | **Ejemplo**                       |
| ------------ | -------------------- | --------------------------------- |
| and          | Son a y b verdadero? | ```True and False```              |
| or           | Son a o b verdadero? | ```True or False```               |
| not          | Niega el valor       | ```not False```<br>```not True``` |

### Ciclo for
La sentencia for en python es bastante versatil ya que nos permite iterar sobre cualquier objeto interable, ya sea una string, lista, tupla, diccionario, etc.

Su sintaxis es la sigueinte
```python
# donde valor es un item del objeto iterable
# donde iterable es cualquier objeto iterable de los ya mencionados

for valor in iterable:
    pass
```

### Sentencia if
Esta es conocida tambien como condicional y evalua una operacion logica, es decir todos aquellos resultados que duvuelvan ```True``` o ```False```

Ademas de la sentencia if existe:
- else
- elif
#### else
Nos permite ejecutar un bloque de codigo en caso que el if inicial sea ```False```
#### elif
Nos permite lo mismo que ```else``` pero con el plus de poder volver a evaluar una operacion logica

Todas estas sentencias se pueden combinar o anidar, esto ultimo quiere decir que se pueden usar dentro de si mismas.

Sintaxis del la sentencia
```python
#Sentencia if sin else
if True:
    #si es verdadero ejecuta el codigo aqui dentro
    pass

#if-else
if False:
    #en este caso como es False no ejecuta este bloque de codigo
else:
    #como es False ejecuta este bloque de codigo
#if-elif-else
if False:
    #Este bloque no se ejecuta
elif True:
    #este codigo se ejecuta cuando una nueva evaluacion es True
else:
    #Si todo es False se ejecuta este codigo.
```
### Kata en codewars
La Kata que resolvimos fue la sigueinte
[https://www.codewars.com/kata/53697be005f803751e0015aa](https://www.codewars.com/kata/53697be005f803751e0015aa)
