#Encuentra el cuadrante. En este caso, si se ponen 2 numeros positivos, el resultado va a ser el cuadrante I. Si se pone x.y(+,-), va a decir cuadrante IV, si se pone x.y(-,+), va a decir cuadrante II, si se pone x.y(-,-), va a decir cuadrante Iii. Si se pone 0, 0 va a decir que estoy en el origen. 

def encontrar_cuadrante(x, y):
    if x > 0 and y > 0:
        return 'Cuadrante I'
    elif x < 0 and y > 0:
        return 'Cuadrante II'
    elif x < 0 and y < 0:
        return 'Cuadrante III'
    elif x > 0 and y < 0:
        return 'Cuadrante IV'
    elif x == 0 and y != 0:
        return 'Sobre el eje Y'
    elif y == 0 and x != 0:
        return 'Sobre el eje X'
    else:
        return 'Origen'
    
try:
    x = int(input('Ingrese la coordenada X: '))
    y = int(input('Ingrese la coordenada Y: '))
    cuadrante = encontrar_cuadrante(x, y)
    print(f'La coordenada ({x}, {y}) se encuentra en {cuadrante}')
except ValueError:
    print('Por favor, ingrese coordenadas válidas (números enteros).')