import string
import string as st
from string import ascii_letters as let
from string import *
#unos strins literal dentro del codigo
'this is a string'

"esto tambien es una cadena"
#numero literal dentro del codigo y una operacion
1
3
5+5

#imperime type int
print(type(10))
#imprime type float
print(type(15.5))
#imperime type string
print(type('hola mundo!'))

#esto si es un comentario

"""
esto es un bloque de 'comentario', python lo toma coomo un string literal, asi que no es un
comentario como tal
"""
'''
otro bloque de comentario, lo mismo que el de arriba
'''


#imprime las comillas simples
print("Imprime comillas simples '' dentro de comillas dobles")

#imprime las comillas simples usando como caracter de escape \' dentro de comillas simples
print('Imprime comillas simples \'\' dentro de comillas simples')

#concatena 2 strings de comillas dobles
print("hola " + "mundo!")

#concatena 2 strings de comillas simples
print('hola ' + 'mundo!')

#concatena 2 strings literales, comillas dobles y simples
print("hola " + 'mundo!')


#imprime un carcater del array indicado por el index
print("esto tambien es una cadena"[1])

#imprime a partir del carcater 5 hasta el final
print("esto tambien es una cadena"[5:])

#imprime a partir del indice de inicio hasta el 5
print("esto tambien es una cadena"[:5])

#imperime a partir del indice 0 hasta el -5, contando de derecha a izquierda
print("esto tambien es una cadena"[:-5])

#imprime del indice -5 al  -2
print("esto tambien es una cadena"[-5:-2])

#imprime la cadena al reves
print("esto tambien es una cadena"[::-1])





print(let)
