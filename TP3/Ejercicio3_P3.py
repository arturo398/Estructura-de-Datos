cola= []
'''def cargar ():
    nombre= input("Ingrese el nombre del cliente: ")
    return nombre
def atender(cola):
   ''' 
op=0
while(op!= 4):
    print("-----  Menu  ------")
    print("1- Cargar cliente")
    print("2- Atender cliente")
    print("3- Consultar clientes restantes")
    op= int(input("Ingrese una opcion: "))
    if op== 1 :
        cliente= input("Ingrese nombre del cliente: ")
        cola.append(cliente)
    elif op== 2 :
        
        del cola[0]
    elif op== 3 :
        print(f"Quedan {len(cola)} en la cola y son: ")
        print(cola)
    elif op== 4 :
        print("Cerrando el sistema de atencion al cliente")
