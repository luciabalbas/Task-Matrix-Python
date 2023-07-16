import matrix

# Creamos un bucle infinito que pide un número entero para crear la matriz
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
    
matriz = matrix.randomMatrix(number)

matrix.printMatrix(matriz)

