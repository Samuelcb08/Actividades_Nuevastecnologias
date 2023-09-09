# #reciban por consola el valor de la compra 
# #que puedan ingresar el numero de cuotas
# #calcular el valor de la cuota
# #usando while que muestre que imprima el plan de pago y que muestre el cupo liberado con cada pago 

# def calcular_cuota(compra, cuotas):
#     tasa_interes = 0.05  # Tasa de interés del 5%
#     valor_cuota = compra / cuotas
#     valor_cuota_con_interes = valor_cuota + (valor_cuota * tasa_interes)
#     return valor_cuota_con_interes

# def main():
#     compra = float(input("Ingrese el valor de la compra: "))
#     cuotas = int(input("Ingrese el número de cuotas: "))
    
#     valor_cuota = calcular_cuota(compra, cuotas)
#     cupo_restante = compra
    
#     print("\nPlan de pago:")
#     pago_numero = 1
#     while cuotas > 0 and cupo_restante >= valor_cuota:
#         cupo_restante -= valor_cuota
#         print(f"Pago {pago_numero}: Cuota de ${valor_cuota:.2f}, Cupo restante: ${cupo_restante:.2f}")
#         pago_numero += 1
#         cuotas -= 1
    
#     print("\n¡Compra completada!")
    
# if __name__ == "__main__":
#     main()
# def main():
#     compra = float(input("Ingrese el valor de la compra: "))
#     cuotas = int(input("Ingrese el número de cuotas: "))
    
#     tasa_interes = 0.05  # Tasa de interés del 5%
#     valor_cuota = (compra / cuotas) * (1 + tasa_interes)
    
#     print("\nPlan de pago:")
#     cupo_restante = compra
#     pago_numero = 1
    
#     while cuotas > 0 and cupo_restante >= valor_cuota:
#         cupo_restante -= valor_cuota
#         print(f"Pago {pago_numero}: Cuota de ${valor_cuota:.2f}, Cupo restante: ${cupo_restante:.2f}")
#         pago_numero += 1
#         cuotas -= 1
    
#     print("\n¡Compra completada!")

# if __name__ == "__main__":
#     main()


# totalcompra = int(input("Ingrese el valor de la compra: "))
# cuotas = int(input("Ingrese el numero de cuotas: "))

# cuota= totalcompra  / cuotas
# cuota_num = 1

# while totalcompra > 0:
#     print("cuota", cuota_num,"a pagar:",cuota)
#     totalcompra -= cuota
#     cuota_num += 1
# print("Restante por pagar: ",totalcompra)

# print("¡el credito ha sido cancelado!")

valor =int(input("Ingrese el valor de la compra: "))
Cuotas = int(input("Ingrese cantidad de cuotas: "))
interes=valor*0.18
valor_cuota=(valor+interes)/Cuotas
numcuotas=1

while Cuotas !=0:
    print(f"El valor de la cuota,{numcuotas} es {valor_cuota}")
    numcuotas+=1
    Cuotas -= 1