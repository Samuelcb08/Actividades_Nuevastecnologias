# # Datos de usuarios almacenados en un diccionario (nombre de usuario: contraseña)
# usuarios = {"usuario1": "contraseña1" "usuario1@gmail.com", "usuario2": "contraseña2"}

# def login():
    
#         usuario = input("Ingrese su nombre de usuario: ")
#         contraseña = input("Ingrese su contraseña: ")

#         if usuario in usuarios and usuarios[usuario] == contraseña:
#             print("Inicio de sesión exitoso. ¡Bienvenido,", usuario, "!")
            
#         else:
    
#             print("Nombre de usuario o contraseña incorrectos. Intentos restantes: ")

# login(
# Datos de usuarios almacenados en un diccionario (nombre de usuario: contraseña y correo)
# usuarios = {
#     "usuario1": {"contraseña": "contraseña1", "correo": "usuario1@example.com"},
#     "usuario2": {"contraseña": "contraseña2", "correo": "usuario2@example.com"}
# }

# def login():
#     intentos = 3
#     while intentos > 0:
#         usuario = input("Ingrese su nombre de usuario: ")
#         contraseña = input("Ingrese su contraseña: ")

#         if usuario in usuarios and usuarios[usuario]["contraseña"] == contraseña:
#             print("Inicio de sesión exitoso. ¡Bienvenido,", usuario, "!")
#             break
#         else:
#             intentos -= 1
#             print("Nombre de usuario o contraseña incorrectos. Intentos restantes:", intentos)

#         if intentos == 0:
#             print("Se agotaron los intentos. Cierre el programa e intente de nuevo más tarde.")

# # Llamada a la función de inicio de sesión
# login()
# Datos de usuarios almacenados en un diccionario (nombre de usuario: contraseña y correo)
# usuarios = {
#     "Jeronimo": {"contraseña": "Jeronimo1", "correo": "jeronimo@gmail.com"},
#     "Samuel": {"contraseña": "1234", "correo": "samuel@gmail.com"},
#     "Alejo" : {"contraseña": "4321","correo": "Alejo@gmail.com"}
# }

# def login():
#         usuario = input("Ingrese su nombre de usuario: ")
#         contraseña = input("Ingrese su contraseña: ")
#         correo = input("Ingrese su correo electrónico: ")

#         if usuario in usuarios and usuarios[usuario]["contraseña"] == contraseña and usuarios[usuario]["correo"] == correo:
#             print("Inicio de sesión exitoso. ¡Bienvenido,", usuario, "!")
            
#         else:
            
#             print("Credenciales incorrectas. Intentos restantes:")

# # Llamada a la función de inicio de sesión
# login()
# Datos de usuarios almacenados en un diccionario (nombre de usuario: contraseña, correo y teléfono)
usuarios = {
    "usuario1": {"contraseña": "123", "correo": "123@example.com", "teléfono": "1234567890"},
    "usuario2": {"contraseña": "contraseña2", "correo": "usuario2@example.com", "teléfono": "9876543210"}
}

def login():
    intentos = 3
    while intentos > 0:
        credencial = input("Ingrese su correo electrónico o número de teléfono: ")
        contraseña = input("Ingrese su contraseña: ")

        for usuario, datos in usuarios.items():
            if (datos["correo"] == credencial or datos["teléfono"] == credencial) and datos["contraseña"] == contraseña:
                print("Inicio de sesión exitoso. ¡Bienvenido,", usuario, "!")
                return
            
        intentos -= 1
        print("Credenciales incorrectas. Intentos restantes:", intentos)

        if intentos == 0:
            print("Se agotaron los intentos. Cierre el programa e intente de nuevo más tarde.")

# Llamada a la función de inicio de sesión
login()
