import sys

#Acceder a las variables de la lista/tupla
lista = []
tupla = ()

print(type(lista))
print(type(tupla))

#Saber el tamaño de una lista o tupla
print(f"Tamanio en memoria de la lista: {sys.getsizeof(lista)}")
print(f"Tamanio en memoria de la tupla: {sys.getsizeof(tupla)}")

#Acceder a los valores de una lista o tupla por medio de su índice
lista2 = [1, 2, "Panchito", 4, 5]
tupla2 = (6, 7, 8, 9, 10) #El índice en python comienza en 0, 1, 2, 3...

print(lista2[2])
print(tupla2[2])

#Acceder al último valor de una lista o tupla
print(lista2[-1])
print(tupla2[-1])
print(lista2[-2])

#len() es lo extenso de un objeto
print(len(lista2))
print(len(tupla2))

#Editar valores de una lista
lista3 = [6, 5, 10, 5, 4]
tupla3 = (9, 8, 2, 5, 10)

lista3[0] = 1
#tupla3[-1] = 9 (esto no se puede hacer, las tuplas no se pueden modificar)

print(lista3)
print(tupla3)

lista3.insert(2, 3) #Agrega elemento en la lista en la posición especificada

print(lista3)

lista3.append(9) #Agrega elemento en la lista en la última posición

print(lista3)