def solicitar_contraseña():
    intentos = 0

    while intentos < 3:
        # Solicitar la contraseña
        contraseña = input("Ingrese una contraseña que inicie con un número: ")
        
        # Verificar que la contraseña inicie con un número
        if not contraseña[0].isdigit():
            print("La contraseña debe iniciar con un número.")
            intentos += 1
            continue
        
        # Solicitar la contraseña nuevamente para verificación
        verificacion = input("Ingrese nuevamente la contraseña para verificar: ")
        
        # Verificar que las contraseñas coincidan
        if contraseña == verificacion:
            print("Contraseña verificada correctamente.")
            return
        else:
            print("Las contraseñas no coinciden.")
            intentos += 1

    print("Has cometido tres errores. El programa se cerrará.")

# Llamar a la función para ejecutar el programa
solicitar_contraseña()