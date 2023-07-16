# Importamos el móduclo de random al principio para usarlo a la hora de rellenar la matriz
import random

# Función para crear una matriz
def randomMatrix(number):
    # Si el parametro introducido no es válido
    matrix = []
    if (number < 1) or (isinstance(number, int) == False):
        matrix = ['No funciona']
        # raise ValueError
    # Matriz vacía
    # Ciclo for para rellenar la matriz de números aleatorios
    for i in range(number):
        a = []
        for j in range(number):
            # se añade un número al array entre 0 y 9
            a.append(random.randrange(10))
        # Introducimos el array en la matriz
        matrix.append(a)
    # Se devuelve la matriz al final de la función
    return matrix

# Función para imprimir la matriz
def printMatrix(matrix):
    # Por cada linea del tamaño de la matriz, se le da un valor de un número, separado por espacio
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            number = matrix[i][j]
            print(number, end = ' ')
        print()