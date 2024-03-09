#Longitud de una frase. En este caso, creamos un programa donde se solicita ingresar una palabra entre 4 y 8 letras. Si se ingresa una palabra con menos de 4 letras, va a tirar un mensaje que diga "Hacen falta letras. Solo tiene x cantidad de letras (la cantidad de letras de la palabra que se haya ingresado). Si se ingresa una palabra con mas de 8 letras, va a tirar un mensaje que diga "Sobran letras. Tiene x cantidad de letras (la cantidad de letras de la palabra que se haya ingresado). Y si se ingresa una palabra entre 4 y 8 letras, va a tirar un mensaje que diga que la palabra es correcta. 

def verificar_longitud(palabra):
    longitud = len(palabra)

    if 4 <= longitud <= 8:
        print('La palabra es correcta.')
        return True
    elif longitud < 4:
        print(f'Hacen falta letras. Solo tiene {longitud} letras.')
    else:
        print(f'Sobran letras. Tiene {longitud} letras.')
    return False

while True:
    palabra = input('Introduce una palabra entre cuatro y ocho letras: ')
    if verificar_longitud(palabra):
        break