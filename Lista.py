
print("_____________________________________________________________")
print("/////////////////////////////////////////////////////////////")
print("_____________________________________________________________")
print("ListaDeCompras.app")
print("1 -- Ingresar compra a la lista")
print("2 -- Eliminar compra de la lista")
print("3 -- Ver la lista de compra")
x = input("numero de la operacion a hacer, o presiona Q para salir:")
Lista=[]

def cambio():
    y = input("Continuar? (s/n):  ")
    if y == "n" or y == "N":
        print("_____________________________________________________________")
        print("ListaDeCompras.app")
        print("1 -- Ingresar compra a la lista")
        print("2 -- Eliminar compra de la lista")
        print("3 -- Ver la lista de compra")
        global x
        x = input("numero de la operacion a hacer, o presiona Q para salir:")
        return x 
    else:
        print("Se repite la accion")

def Ingreso(String):
    Lista.append(String)
    print("Se agrego con exito!")
    print(f"{Lista}")
    
def Eliminacion():
    Show()
    z = int(input("Indica que numero de la lista deseas borrar: "))
    if z-1 in range(0,len(Lista)):
        Lista.pop(z-1)
        print("Se elimino con exito!")
    else:
        print("Error: valor no valido!")
        z = int(input("Indica que numero de la lista deseas borrar: "))
    
def Show():
    print("Se muestra la lista hasta ahora: ")
    print("____________________________")
    print("****************************************")
    rangolista = len(Lista)
    for i in range(0,rangolista):
        print(f"{i+1} -- {Lista[i]}")
    print("____________________________")
    print("****************************************")
    
    print("Se muestra con exito!")
while x != "Q":
    if x == "1":
        String = input("Que deseas ingresar: ")
        Ingreso(String)
        cambio()
        
    elif x == "2":
        Eliminacion()
        cambio()

        
    elif x == "3":
        
        Show()
        cambio()
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
