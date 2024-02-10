# Pedir datos al usuario
nombre = input('Introduce tu nombre: ')
apellido = input('Introduce tu apellido paterno: ')
apellido_materno = input('Introduce tu apellido materno: ')

# Validar que la edad sea un dato numérico, no vacío
while True:        
    edad = input('Introduce tu Edad: ')
    try:
        edad = float(edad)
        if edad > 0:
            break
        else:
            print('Por favor introduce un número válido mayor que 0')
    except ValueError:
        print('Introduzca un valor numérico')

# Validar y convertir peso
while True:
    peso = input('Introduce un peso en kilogramos: ')
    try:
        peso = float(peso)
        if peso > 0:
            break
        else:
            print('Por favor introduce un peso válido mayor que 0')
    except ValueError:
        print('Introduce un valor numérico para el peso')

# Validar y convertir estatura
while True:
    estatura = input('Introduce tu estatura en metros (ejemplo 1.75): ')
    try:
        estatura = float(estatura)
        if estatura > 0:
            break
        else:
            print('Por favor introduce una estatura válida mayor a 0')
    except ValueError:
        print('Introduce un valor numérico para la estatura')

# Calcular IMC
imc = peso / (estatura ** 2)

print('Datos:')
print('Nombre: ' + nombre)
print('Apellido: ' + apellido)
print('Apellido Materno: ' + apellido_materno)  # Cambiado para claridad
print('Edad: ' + str(edad))  # Convertir a str para imprimir
print('Peso: ' + str(peso) + ' kg')  # Convertir a str y añadir unidad
print('Estatura: ' + str(estatura) + ' m')  # Convertir a str y añadir unidad

print(f'Hola {nombre}, tu IMC es de {imc:.2f}')