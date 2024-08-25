# Uso de la sentencia continue en un ciclo for

# for numero in range(1, 11):
#     if numero % 2 == 1:
#         continue
#     print(f'{numero} es un par')

# # Uso de la sentencia continue en un ciclo while

# numero = 0
# while numero < 11:
#     numero + - 1
#     if numero % 2 == 0:
#         continue
#     print(f'{numero} es un numero inpar')

###################################################################

# Uso de la sentencia break

# numero = int(input('Ingrese un digito: '))
# limite_inferior = 0
# limite_superior = 10
# buscado = 5
# intentos = 0

# while True:
#     intentos += 1
#     if numero == buscado:
#         print(f'El numero {numero} fue encontrado en {intentos} intentos')
#         break
#     elif numero < buscado:
#         limite_superior = buscado
#         buscado = (buscado + limite_inferior) // 2
#     else:
#         limite_inferior = buscado
#         buscado = (buscado + limite_superior) // 2

# print('Fin del programa')

##############################################################################

# Uso de la funcion exit

# numero = int(input('Ingrese un digito: '))
# limite_inferior = 0
# limite_superior = 10
# buscado = 5
# intentos = 0

# while True:
#     intentos += 1
#     if numero == buscado:
#         print(f'El numero {numero} fue encontrado en {intentos} intentos')
#         exit()
#     elif numero < buscado:
#         limite_superior = buscado
#         buscado = (buscado + limite_inferior) // 2
#     else:
#         limite_inferior = buscado
#         buscado = (buscado + limite_superior) // 2

# print('Fin del programa')
# print('Impresion despues de la sentencia break')
# print('Impresion despues del uso de la funcion exit()')

intentos = 0
while True:
    intentos += 1
    print(f'intento{intentos}')
    if intentos == 20:
        print('Fin del programa')
        exit()

print('Impresion despues de la funcion exit()')
