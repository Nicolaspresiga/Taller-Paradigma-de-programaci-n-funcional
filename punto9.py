def agregar_elemento_funcional(set1, elemento):
    return set1 | {elemento}

def eliminar_elemento_funcional(set1, elemento):
    return set1 - {elemento}

conjunto = {1, 2, 3}
resultado = eliminar_elemento_funcional(agregar_elemento_funcional(conjunto, 4), 2)
print(resultado)  # {1, 3, 4}


#1. ¿Qué retorna el bloque de código?
    # No retorna nada explícitamente. 
    # Las funciones agregar_elemento y eliminar_elemento no tienen sentencia return, por lo tanto, retornan None de forma implícita.
    # Sin embargo, modifican directamente el conjunto set1 que se pasa como argumento (por referencia).
    # Esto viola el principio de inmutabilidad del paradigma funcional, ya que altera el objeto original.

#2. ¿Cuántas funciones se declararon?
    # Se declararon 2 funciones:
    # agregar_elemento(set1, elemento)
    # eliminar_elemento(set1, elemento)
    # Ambas realizan operaciones sobre conjuntos mutables (set).

#3. ¿Qué imprime en consola?
    # El código no contiene ningún print(), por lo que no imprime nada en consola.
    # Sin embargo, si agregáramos: print(resultado)
    # El resultado mostrado sería: {1, 3, 4}
    # Explicación paso a paso:
        # Conjunto inicial: {1, 2, 3}
        # Se agrega 4 → {1, 2, 3, 4}
        # Se elimina 2 → {1, 3, 4}

#Conclusión funcional:
    # Aunque el código funciona correctamente, no sigue el paradigma funcional porque:
        # Modifica directamente el conjunto (set), lo que introduce efectos secundarios.
        # Para hacerlo funcional, debería devolver un nuevo conjunto sin alterar el original.
        # Ejemplo versión funcional:

def agregar_elemento_funcional(set1, elemento):
    return set1 | {elemento}

def eliminar_elemento_funcional(set1, elemento):
    return set1 - {elemento}

conjunto = {1, 2, 3}
resultado = eliminar_elemento_funcional(agregar_elemento_funcional(conjunto, 4), 2)
print(resultado)  # {1, 3, 4}