def process_matrix():
    def _process_matrix():
        def sum():
            # Calcula el average de cada valor de la matrix
            # Contempla todas las opciones de matrix(una o más columnas) y todas las posiciones de valores:
            suma = 0
            # Una sola columna, extremo superior:
            if len(matrix) == 1 and j == 0:
                suma += matrix[0][j] + matrix[0][j + 1]
                return suma / 2
            # Una sola columna, medios:
            elif len(matrix) == 1 and j != 0 and j != len(matrix[0]) - 1:
                suma += matrix[0][j] + matrix[0][j + 1] + matrix[0][j - 1]
                return suma / 3
            # Una sola columna, extremo inferior:
            elif len(matrix) == 1 and j == len(matrix[0]) - 1:
                suma += matrix[0][j] + matrix[0][j - 1]
                return suma / 2
            # Esquina superior izquierda
            elif i == 0 and j == 0:
                suma += matrix[i][j] + matrix[i][j + 1] + matrix[i + 1][j]
                return suma / 3
            # Borde superior:
            elif i == 0 and j < len(matrix[i]) - 1:
                suma += matrix[i][j] + matrix[i][j + 1] + matrix[i][j - 1] + matrix[i + 1][j]
                return suma / 4
            # Esquina superior derecha:
            elif i == 0 and j == len(matrix[i]) - 1:
                suma += matrix[i][j] + matrix[i][j - 1] + matrix[i + 1][j]
                return suma / 3
            # Borde izquierdo
            elif i != 0 and i != len(matrix) - 1 and j == 0:
                suma += matrix[i][j] + matrix[i][j + 1] + matrix[i + 1][j] + matrix[i - 1][j]
                return suma / 4
            # Borde derecho
            elif i != 0 and i != len(matrix) - 1 and j == len(matrix[i]) - 1:
                suma += matrix[i][j] + matrix[i][j - 1] + matrix[i + 1][j] + matrix[i - 1][j]
                return suma / 4
            # Esquina inferior izquierda:
            elif i == len(matrix) - 1 and j == 0:
                suma += matrix[i][j] + matrix[i - 1][j] + matrix[i][j + 1]
                return suma / 3
            # Borde inferior:
            elif i == len(matrix) - 1 and j < len(matrix[i]) - 1:
                suma += matrix[i][j] + matrix[i][j + 1] + matrix[i][j - 1] + matrix[i - 1][j]
                return suma / 4
            # Esquina inferior derecha:
            elif i == len(matrix) - 1 and j == len(matrix[i]) - 1:
                suma += matrix[i][j] + matrix[i - 1][j] + matrix[i][j - 1]
                return suma / 3
            # Resto:
            else:
                suma += matrix[i][j] + matrix[i][j + 1] + matrix[i][j - 1] + matrix[i + 1][j] + matrix[i - 1][j]
                return suma / 5

        output = []
        # Para la opción de una sola columna:
        if len(matrix) == 1:
            for j in range(len(matrix[0])):
                # Llama la función sum para calcular el average:
                average = sum()
                # Agrega cada average a una nueva lista:
                output.append(round(average, 2))
        # Para la opcion de más de una columna:
        else:
            r = len(matrix)
            c = len(matrix[0])
            for i in range(r):
                for j in range(c):
                    # Llama la función sum para calcular el average:
                    average = sum()
                    # Agrega cada average a una nueva lista:
                    output.append(round(average, 2))
        # Divide la nueva lista en una matriz con la misma cantidad de columnas que matrix:
        n = len(matrix[0])
        new_matrix = [output[i:i + n] for i in range(0, len(output), n)]
        return new_matrix
    # Chequea que solo haya ints o floats en la matrix:
    for i in range(len(matrix)):
        for j in matrix[i]:
            if type(j) != int and type(j) != float:
                raise ValueError("Your matrix values are not numbers.")
    # Chequea que la matrix tenga al menos una columna:
    if len(matrix) == 0:
        print("Your matrix is empty.")
    # Chequea que la matrix tenga al menos dos números
    elif len(matrix) == 1 and (len(matrix[0]) == 1 or len(matrix[0]) == 0):
        print("Your matrix has not enough numbers.")
    # Chequea que la matrix sea una matrix:
    elif type(matrix) != list:
        print("This is not a matrix.")
    # Llama al _process_matrix():
    else:
        new_matrix = _process_matrix()
        return new_matrix


matrix = [[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]]

print(process_matrix())