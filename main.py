# Importa las funciones del archivo matrix.py
import matrix
# Importa las funciones del archivo sums.py
import sums

# Un bucle infinito que pide un número entero para crear la matriz
while True:
    try:
        number = int(input('Introduzca el número de filas y columnas para la matriz: '))
        # Si el número introducir un número negativo o 0 lanza un error
        if number < 1:
            raise ValueError 
        # En caso de introducir un número correcto, el bucle se rompe
        else:
            break
    # En caso de error imprime un mensaje y reinicia el bucle
    except:
        print('Debe introducir un número entero y positivo. Por favor, inténtelo de nuevo.')
    
# Crea una matriz según la función 
matriz_1 = matrix.randomMatrix(number)

# Imprime la matriz según la función
matrix.printMatrix(matriz_1)

# Suma las filas de la matriz
sumRows = sums.addsRows(matriz_1)

# Suma las columnas de la matriz
sumColums = sums.addsColumns(matriz_1)

# Imprimir el array de la suma de las filas de la matriz
print()
for i in range(number):
    print(f'La suma de la fila {i+1} es {sumRows[i]}')

# Imprimir el array de la suma de columnas de la matriz
print()
for j in range(number):
    print(f'La suma de la columna {j+1} es {sumColums[j]}')