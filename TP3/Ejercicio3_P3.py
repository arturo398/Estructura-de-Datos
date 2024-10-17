cola= []
'''def cargar ():
    nombre= input("Ingrese el nombre del cliente: ")
    return nombre
def atender(cola):
   ''' 
op=0
while(op!= 4):
    print(f"\n-----  Menu  ------")
    print("1- Cargar cliente")
    print("2- Atender cliente")
    print(f"3- Consultar clientes restantes")
    print(f"4- Cerrar sistema \n")
    op= int(input("Ingrese una opcion: "))
    if op== 1 :
        cliente= input("Ingrese nombre del cliente: ")
        cola.append(cliente)
        print(" ")
    elif op== 2 :
        print(f"\nTurno de {cola[0]}")
        del cola[0]
    elif op== 3 :
        print(f"Quedan {len(cola)} en la cola y son: ")
        print(cola,f'\n')
    elif op== 4 :
        print(f"Cerrando el sistema de atencion al cliente \n")
