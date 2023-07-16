# Función que suma las columnas de una matriz
def addsColumns(matrix):
    # Array que contendrá las sumas de cada columna
    sums = []
    # Ciclo que recorre la matriz
    for column in range(len(matrix[0])):
        # Variable a la que se sumarán cada número de las columnas
        add = 0
        # Por cada linea, se suma a la variable add el número de se haya en esa posición
        for row in matrix:
            add += row[column]
        # Al final de las sumas, se añade ese valor al array sums
        sums.append(add)
    return sums

# Función que suma las filas de una matriz
def addsRows(matrix):
    # Array que contendrá las sumas de cada fila
    sums = []
    # Ciclo que recorre la matriz
    for row in matrix:
        # Variable a la que se irá sumando las filas
        add = 0
        # Por cada columna, se suma a la variable add el número en esa posición
        for column in range(len(matrix[0])):
            add += row[column]
        sums.append(add)
    return sums