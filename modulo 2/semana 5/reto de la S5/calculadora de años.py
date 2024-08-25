# Funcion para manejo de entradas no validas
def obtener_fecha(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Por favor, introduce un dato numerico.")


# Solicitud de las fechas al usuario
fecha_actual = obtener_fecha("Introduce el año actual: ")
fecha_dos = obtener_fecha("Introduce otro año para calcular: ")


# Bloque de código que calcula resultados
"""con la funcion "abs" me ahorre muchas lineas de codigo"""
resta = abs(fecha_actual - fecha_dos)
if fecha_actual > fecha_dos:
    print("Han pasado " + str(resta) + " años.")
else:
    print("Faltan " + str(resta) + " años.")


# Bloque de código para comentarios basados en el valor de resta
if resta <= 1:
    print("Es muy fácil, podías calcularlo sin mí.")
elif 2 <= resta <= 5:
    print("Ok, no son muchos años lo que hacía falta, tenías dedos para contar.")
else:
    print("Han pasado bastantes años.")
