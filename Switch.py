# print("1. Registro\n 2.Login\n 3.salir")
# opc=0

# if opc == 1:
#     print("Registro")
# elif opc == 2:
#     print("Login")
# elif opc == 3:
#     print("Salir")
# else:
#     print("Seleccione una opcion valida")    

#  generar un programa que permita hacer el registro e iniciar sesion dentro del while, debe imprimir el menu usando la implementacion de if,elif,else,else(selector multiple). cuando inicie sesion que implemetne la solucion del calculo de cuotas creada en el reto anterior    
def calcular_cuota(compra, cuotas):
    tasa_interes = 0.05  # Tasa de interés del 5%
    valor_cuota = (compra / cuotas) * (1 + tasa_interes)
    return valor_cuota

def main():
    usuarios = {}  # Diccionario para almacenar usuarios y contraseñas

    while True:
        print("1. Registrarse")
        print("2. Iniciar Sesión")
        print("3. Salir")
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 1:
            usuario = input("Ingrese un nombre de usuario: ")
            contraseña = input("Ingrese una contraseña: ")
            usuarios[usuario] = contraseña
            print("Usuario registrado exitosamente.")
        elif opcion == 2:
            usuario = input("Ingrese su nombre de usuario: ")
            contraseña = input("Ingrese su contraseña: ")
            if usuario in usuarios and usuarios[usuario] == contraseña:
                print("Inicio de sesión exitoso.")
                compra = float(input("Ingrese el valor de la compra: "))
                cuotas = int(input("Ingrese el número de cuotas: "))
                valor_cuota = calcular_cuota(compra, cuotas)
                cupo_restante = compra
                
                print("\nPlan de pago:")
                pago_numero = 1
                while cuotas > 0 and cupo_restante >= valor_cuota:
                    cupo_restante -= valor_cuota
                    print(f"Pago {pago_numero}: Cuota de ${valor_cuota:.2f}, Cupo restante: ${cupo_restante:.2f}")
                    pago_numero += 1
                    cuotas -= 1
                
                print("\n¡Compra completada!")
            else:
                print("Nombre de usuario o contraseña incorrectos.")
        elif opcion == 3:
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
