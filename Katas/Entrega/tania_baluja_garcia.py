from functools import reduce

def process_matrix(matrix):
    """
    Recibe como parámetro una matriz (lista de listas) de números y 
    devuelve otra, con el mismo tamaño y número de elementos. Los 
    elementos de la nueva matriz es el promedio del valor antiguo
    con el valor de sus vecinos
    """
    # Crear una lista vacía donde se irá acumulando
    processed_matrix = []

    if len(matrix) == 1:
        # Matriz de una columna
        processed_matrix = matrix
    else:
        # Obtener una lista con la posición de las columnas y sus valores
        for i, column in enumerate(matrix):
            # Obtener una lista con la posición de la fila y sus valores (para cada columna)
            new_list = []
            for j, value in enumerate(column):
                # Procesado
                new_list.append(process_value(i, j, matrix))
                # Añadir a la lista
            processed_matrix.append (new_list)
    # Devuelvo la nueva lista (matriz resultante)
        return processed_matrix


def process_value(i, j, matrix):
    """
    Recibe los índices del elemento y la matriz original, 
    y devolverá el nuevo valor promedio
    """
    # Obtener vecinos
    index = get_neighbour_index(i,j,matrix)
    values = get_neighbour_values(index, matrix)

    # Cálculo del promedio
    average = get_average_matrix(values)

    # Devolver valor final
    return average


def get_neighbour_index(i,j, matrix):
    """
    Devuelve la lista de columnas vecinas
    Se incluye a la propia columna
    """
    all_index = []
    n_columns = len(matrix)
    n_row = len(matrix[0])

    all_index.append((i-1,j)) #left-side
    all_index.append((i+1,j)) #right-side
    all_index.append((i,j+1)) #up
    all_index.append((i,j-1)) #down
    all_index.append((i,j)) #own-side

    selected_index = []
    for i,j in all_index:
        if i >= 0 and i<= (n_columns-1) and j >= 0 and j<= (n_row-1):
            selected_index.append((i,j))
    return selected_index


def get_neighbour_values(index, matrix):
    values = []
    for i ,j in index:
            values.append(matrix[i][j])
    return values


def get_average_matrix(numbers):
    """
    Recibe una lista de números y devuelve su promedio
    """
    return reduce(lambda accum,b: accum + b, numbers, 0)/len(numbers)


matriz = [[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]]


print(process_matrix(matriz))