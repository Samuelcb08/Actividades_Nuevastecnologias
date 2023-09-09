# las listas son estructuras de datos lineales
# se crean usando brackes ejemplo: My_list =[]
# las listas son ordenadas(orden de insersion) esto quiere decir que el ultimo dato ingresado ocupara la ultima posicion
# emplea metodos para manipular los items de la misma.
#permite items duplicados, es decir podemos agregar,actualizar o remover items
# puede tener distintos tipos de datos 

nombres = ["juan", "Maria","Pepito","Lisa"]
print(len(nombres))
print(type(nombres))

listaDatos = ["pepito", "perez", 1017923248, 1.80,True]
print(f"el numero de doc es: {listaDatos[2]}")
#Slicing de datos
print(listaDatos[1:4])
print(listaDatos[:4])
print(listaDatos[3:])
print(listaDatos[:-1])
print(listaDatos[-4:-1])
print(listaDatos[1:4])