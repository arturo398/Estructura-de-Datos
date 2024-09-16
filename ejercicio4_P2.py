
def descuentos(moneda:str,total:float):
    divisas={"dolares": 0.05, "yenes" : 0.15, "guaranies" : 0.20, "pesos" : 0.10 }
    descuento: float
    moneda=moneda.lower()
    descuento=0 
    if moneda in divisas:
        print(f"Las compras en {+moneda} tiene un descuento del {int(divisas[moneda]*100)}%: ")
        descuento =total - (total * divisas[moneda])
    else:
        print(f"No hay ningun descuento para las compras en {moneda} ")
        descuento=total
    return descuento


billete=str(input("Ingrese con que divisa realizara la compra: "))
compra=float(input("Ingrese el monto de la compra: "))

print(f"EN total deberia pagar {descuentos(billete, compra)}")