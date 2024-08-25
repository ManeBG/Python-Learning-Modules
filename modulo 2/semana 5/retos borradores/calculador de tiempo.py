# Solicitud de las fechas al usuario.
fecha_actual = int(input("Introduce el año actual: "))
fecha_dos = int(input("Introduce otro año para calcular: "))

# Bloque de codigo que calcula resultados
if fecha_actual > fecha_dos:
    resta = fecha_actual - fecha_dos
    print("Han pasado " + str(resta) + " años.")
else:
    resta = fecha_dos - fecha_actual
    print("Faltan " + str(resta) + " años")

# bloque de codigo por si el usuario es muy burro.
if resta <= 1:
    print("es muy facil podias calcularlo sin mi")
elif 2 <= resta <= 5:
    print("Ok, no son muchos años lo que hacía falta, tenías dedos para contar.")


# Vi la funcion abs se me hizo interesante
