lista = []

alumnos = 0
max_alumnos = 15  # Define la cantidad máxima de alumnos

while alumnos < max_alumnos:
    opcion = input('Agregar alumno (1) o terminar (2): ')
    if opcion == '1':
        nombre = input('Ingrese el nombre del alumno: ').capitalize()
        calificaciones = []

        # Solicitar la primera calificación (obligatoria)
        while True:
            calificacion1 = input(
                f'Ingrese la primera calificacion de {nombre}: ')
            if calificacion1.isdigit():  # metodo para verificar que sean numeros enteros
                calificaciones.append(int(calificacion1))
                break  # Sale del bucle si la entrada es válida
            else:
                print("Debe ingresar una calificación válida.")

        # Solicitar la segunda calificación (opcional)
        calificacion2 = input(f'Ingrese la segunda calificacion de {
                              nombre} (o presione Enter para omitir): ')
        if calificacion2.isdigit():
            calificaciones.append(int(calificacion2))

        # Solicitar la tercera calificación (opcional)
        calificacion3 = input(f'Ingrese la tercer calificacion de {
                              nombre} (o presione Enter para omitir): ')
        if calificacion3.isdigit():
            calificaciones.append(int(calificacion3))

        alumno = [nombre] + calificaciones
        lista.append(alumno)
        alumnos += 1
    elif opcion == '2':
        print(f'El programa ha terminado con {alumnos} alumnos.')
        break
    else:
        print('Se ha ingresado una opcion invalida.')
        continue

# Mostrar la lista de alumnos con sus calificaciones y promedio
print('La lista de alumnos es:')
for alumno in lista:
    nombre = alumno[0]
    calificaciones = alumno[1:]
    promedio = sum(calificaciones) / len(calificaciones)
    print(f'{nombre}: Calificaciones = {
          calificaciones}, Promedio = {promedio:.2f}')
