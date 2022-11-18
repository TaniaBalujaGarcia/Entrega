def find_one(list, needle):
    """
    Devuelve True si encuentra una o más ocurrencias de needle con la lista
    """
    # Inicializamos el booleano que representa la condición de haber encontrado o no y el indice
    found = False
    index = 0
    # Mientras no encontramos y no hayamos terminado con la lista
    while not found and index < len(list):
        # Miramos a ver si está en la posición actual y actualizamos la condición
        if needle == list[index]:
            found = True
        # Avanzamos al siguiente elemento
        index = index + 1
    # Devolvemos si hemos encontrado o no
    return found