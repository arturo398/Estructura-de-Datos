print("-------Registro de notas de examenes--------")
nota1=float(input("Ingrese la nota del primer examen: "))
nota2=float(input("Ingrese la nota del segundo examen: "))

promedio= (nota1+nota2)/2
print(f"El promedio de las notas es: {promedio}")

if nota2>=7:
    print("El alumno aprobo el segundo examen")
else:
    print("El alumno desaprobo el segundo examen")

if nota2>nota1:
    print("Mejoro su desempeño")
elif nota2 == nota1:
    print("Mantuvo la nota")
else:
    print("Empeoro su desempeño")

if promedio>=7:
    print("Promociono la materia")
elif promedio >=4 :
    print("Debe rendir el final")
else: 
    print("Debe recursas la materia")