#!/usr/bin/python3
import sys
import base64

def decode(texto_encoded):
    decoded = texto_encoded
    contador = 0
    while contador < 50:
        decoded = base64.b64decode(decoded)
        contador += 1
        pass
    return decoded
    pass

def encode(texto_plano):
    encoded = texto_plano
    for value in range(50):
        encoded = base64.b64encode(encoded)
        pass
    return encoded
    pass

def makeFile(content,opc):
    if opc == '2':
        f = open('codificado.txt', 'ab')
        pass
    else:
        f = open('decodificado.txt', 'ab')

    f.write(content)
    f.close()
    pass

archivo = open(sys.argv[1], 'rb')

text = archivo.read()
opcion = sys.argv[2]

if opcion == '2': #esto es para codificar
    codificado = encode(text)
    makeFile(codificado, opcion)
    print('exito')
    pass
elif opcion == '1': #decodificar
    decodificado = decode(text)
    makeFile(decodificado, opcion)
    print('exito')
    pass
else:
    print('opcion incorrecta')

archivo.close()
