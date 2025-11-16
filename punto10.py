#DATOS A USAR.
listal = [1,2,3]
lista2 = [4,5,6]
lista3 = [7,8,9]

#OPERACION CON "map()" Y "lambda".
resultado = map(lambda x, y, z: x + y + z, listal, lista2, lista3)

print(list(resultado))

"""
a. [12, 15, 18]

b. La función map() aplica la función lambda a los elementos de las tres listas al mismo tiempo.
En cada iteración toma un elemento de lista1, uno de lista2 y uno de lista3, los suma y devuelve el resultado.
Así, obtiene los valores [12, 15, 18] al sumar posición por posición los elementos de las tres listas.

"""