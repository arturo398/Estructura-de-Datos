print("========================================================")
print("--------------- Universidad Privada --------------------")
print("------------- Inscripción de Alumnos -------------------")
print("========================================================")

nombre = input("Ingrese su nombre completo: ")
edad = int(input("Ingrese su edad: "))
nacimiento = input("Ingrese su fecha de nacimiento (dd/mm/aaaa): ")

titulo_secundario = True

matricula = float(input("Ingrese el monto de la matricula: "))

cuota = matricula + 1000

arancel = 12000 / 4

costo_mensual = cuota + arancel
print(f"\nEl costo mensual (incluyendo 'Python I') es: ${costo_mensual:.2f}")

efectivo = input("¿Paga en efectivo? (si/no): ").lower()

if efectivo == "si":
    descuento = costo_mensual * 0.75
    print(f"El costo con un 15% de descuento es: ${descuento:.2f}")
else:
    print("No se aplicará descuento.")

print("\n----- Resumen de la Inscripción -----")
print("=======================================")
print(f"Nombre del alumno: {nombre}")
print(f"Edad: {edad}")
print(f"Fecha de nacimiento: {nacimiento} ({edad})")
print(f"Posee título secundario: {titulo_secundario}")
print(f"Monto de la matrícula: ${matricula:.2f}")
print(f"Cuota mensual (sin descuento): ${costo_mensual:.2f}")

if efectivo == "si":
    print(f"Cuota mensual (con descuento): ${descuento:.2f}")