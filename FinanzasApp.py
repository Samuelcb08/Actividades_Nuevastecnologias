# la aplicacion debe permitir registrar ingresos y contar el saldo de estos
# debe permitir registrar egresos y mostrar el saldo
# si el ingreso es mayor que el saldo no debe permitir el retiro y mostrara un mensaje de saldo insuficiente
# la aplicacion llevara registros de los movimientos indicando el numero de ingresos y de egresos
 
Saldo = 0
acumIngresos = 0
acumEgresos = 0

IsOn = int(input("Ingrese 1 para inicializar el servicio: "))

while IsOn !=0:
    opc =int(input(" 1.Ingrese Registro: \n 2. Egreso \n 3.Salir \n "))

    if opc == 1:
        ingreso = int(input("Registro el ingreso: "))

        Saldo = Saldo + ingreso

        print(f"Su Saldo es {Saldo}")
        acumIngresos+=1
        print(acumIngresos)
    elif opc==2:  
        egreso = int(input("Registre el metodo a retirar: "))

        Saldo = Saldo - egreso
        if Saldo < 0:
            print("Saldo Insuficiente")
            Saldo = Saldo + egreso
            print(Saldo)
            acumEgresos += 1
            print(acumEgresos)
        else:
            print(f"Su total de saldo es: ${Saldo}")
        acumEgresos+=1
        print(acumEgresos)
    elif opc== 3:
        print("Usted Salio del Aplicativo")
        IsOn=0
    else:
        print("Ingrese una opcion valida") 