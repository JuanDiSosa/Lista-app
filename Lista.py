
print("_____________________________________________________________")
print("/////////////////////////////////////////////////////////////")
print("_____________________________________________________________")
print("ListaDeCompras.app")
print("1 -- Ingresar compra a la lista")
print("2 -- Eliminar compra de la lista")
print("3 -- Ver la lista de compra")
x = input(print("numero de la operacion a hacer, o presiona Q para salir:"))
Lista=[]
def Ingreso(String):
    Lista.append(String)
    print("Se agrego con exito!")
    print(f"{Lista}")
def Eliminacion(String):
    Lista.append(String)
    print("Se elimino con exito!")
    
def Show(String):
    print("Se muestra con exito!")
while x != "Q":
    if x == "1":
        String = input(print("Que deseas ingresar: "))
        Ingreso(String)
        
        break
    elif x == "2":
        Eliminacion(Lista)
        break
    elif x == "3":
        Show(Lista)
        break
    else:
        print(f"{x} VALOR NO VALIDO")
        print("-------------------------------------------")
        x1 = input("Quieres reintentarlo? (y/n) ")
        while x1 != "y" or "n":
            if x1 == "y":
                x = input("Introduce el numero de la operacion a hacer, o presiona Q para salir:")
                break
            elif x1 == "n":
                print("Gracias por usar SAM")
                x = "Q"
                break
            else:
                print(f"{x1} valor no valido")
                x1 = input("Quieres reintentarlo? (y/n) ")

print("End")
