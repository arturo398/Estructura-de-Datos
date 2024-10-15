def parentesis(texto):
    cont_1=0
    cont_2=0
    for caracter in texto:
        if caracter == '(':
            cont_1 += 1
        elif caracter == ')':
            cont_2 += 1

    return cont_1==cont_2
            

texto= input("Ingrese un texto que contenga parentesis:")

if parentesis(texto):
    print("Hay la misma cantidad de parentess de apertura que de cierre")
else:
    print("Los parentesis no estan equilibrados")