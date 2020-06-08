#Python 101 - leccion 2 - script
#Title: solver.py
#Author: n0tM4l4f4m4


#las variables son palabras definidas por el progra,ador

variable_1 = 34
variABLE_2 = "hello world!"
_variable_3 = 789.65

#las constantes tambien van definidas por el programador
IP = '127.0.0.1'
PORT = 8089

#datos de entrada

var1 = input()

var2 = input('introduce un dato')
var3 = input('introduce otro dato\n')

#tuplas
tupla_1 = (1,2,3,4,5)
tupla_2 = ('a', 'x', 'z')
tupla_3 = (1,2,3,'x','y', 'z')

#lista

lista_1 = []
lista_2 = [1,2,3, ('alo', 'cio', 'salut', 'hello'), 8.9, 'strings', [99, 10,80]]
lista_2.append('elemento al final')
lista_2.count(2)
lista_2.extend(('mas', 'y', 'mas', 'elementos', 'al', 'final'))
lista_2.index('strings')
lista_2.insert('insertado')
lista_2.pop()
lista_2.reverse()
lista_2.sort()
lista_2.sort(revserse=True)
lista_2.remove(3)

lista_3 = list(tupla_3)

print(range(100))
