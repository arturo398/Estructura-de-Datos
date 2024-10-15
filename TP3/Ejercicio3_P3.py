cola= []
'''def cargar ():
    nombre= input("Ingrese el nombre del cliente: ")
    return nombre
def atender(cola):
   ''' 
do {
print("-----  Menu  ------")
print("1- Cargar cliente")
print("2- Atender cliente")
print("3- Consultar clientes restantes")
op= int(input("Ingrese una opcion: "))
match op:
    case '1':
        cola.append(cargar())
    case '2':
        cola[0].pop()
    case '3':
         print(f"Quedan {len(cola)} en la cola y son: ")
         print(cola)

    }while(op!= 'S' or 's')