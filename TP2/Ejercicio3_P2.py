def vuelto(total, gasto):
    if total< gasto:
        print('El dinero ingresado es insuficiente para la compra')
    else:
        billetes={500: 0,100: 0,50: 0,20 : 0,10 : 0,5 : 0,1 : 0}
        vuelto=total-gasto
        for billete in billetes:
            if vuelto>=billete:
                cantidad_billetes = vuelto // billete
                billetes[billete] += cantidad_billetes
                vuelto %= billete
        
        return billetes
    

caja = int(input("Ingrese la cantidad total de la compra: "))
cliente = int(input("Ingrese la cantidad total entregada por el cliente: "))

compra = vuelto(cliente, caja)
total_vuelto= 0
print("El vuelto que se le debe dar al cliente: ")
for i in compra:
    if compra[i] >0:
        print(f"{compra[i]} billetes de ${i}")
        total_vuelto += (i * compra[i])

print(f"El total del vuelto es: ${total_vuelto}")
