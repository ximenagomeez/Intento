"""Ejemplo de listas"""

#lista de puros números
from typing import List

lista: List[int] = [11,12,13,14,15]
print("lista", lista)

#agregar elementos

lista.append(50)
print("lista", lista)

#tamaño de la lista
print("tamaño de la lista", len(lista))

#consultar elementos
print("elemento 0", lista[0])
print("elemento 1", lista[1])
print("elemento 2", lista[2])

print("elemento -1", lista[-1]) #va en reversa

#lista de strings
listapalabras = ["hola","me","llamo","ximena"]
print("lista palabras", listapalabras )

#lista mixta
listamixta = ["soy", 1, "ximena"]
print("lista mixta", listamixta)

