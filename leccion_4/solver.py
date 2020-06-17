# print("imprime del 1 al 100")
# x = 1
# while True:
#     if x < 101:
#         print(x)
#         x += 1
#         pass
#     else:
#         print('x llego a 100')
#         break
# x = 1
# while x < 101:
#     print(x)
#     x += 1
### funciones
# def imprimePantalla(salida):
#     print(salida)
#     pass

# imprimePantalla("hola mundo!")
# # definicion de funcion, estros parametros por orden
# def potencia(x, y):
#     if isinstance(x, int) and isinstance(y, int):
#         return x ** y
#         pass
#     else:
#         return "Error en el tipo de entrada"
#     pass

# print(potencia(2, 8))
# print(potencia(8, 2))
# print(potencia('a', 5))

# def pontencia_2(x, y):
#     if isinstance(x, int) and isinstance(y, int):
#         return x ** y
#         pass
#     else:
#         return "Error en el tipo de entrada"
#     pass
#     pass

# print(pontencia_2(x=15, y=2))
# print(pontencia_2(y=2, x=15))

def crear2listas():
    lista1 = list(['a','b', 'c'])
    lista2 = list([9,8,7])
    return lista1, lista2
    pass

nuevalista1, nuevalista2 = crear2listas()

print(nuevalista1, nuevalista2)

print(type(nuevalista1), type(nuevalista2))

entero, cadena, flotante = 178, 'hola mundo!', 89.8

print(entero, cadena, flotante)

funcion_anon = lambda x, y: x ** y

print(type(funcion_anon))

print(funcion_anon(6, 6))