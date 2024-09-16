def mayor(num1: int, num2: int, num3: int):
    if num1 == num2 == num3:
        return f'Son todos los numeros iguales a {num1}, no hay mayores'
    
    max=num1
    if num2>max:
        max=num2
    if num3>max:
        max=num3
    
    return max

a= int(input('Ingrese un numero: '))
b= int(input('Ingrese un numero: '))
c= int(input('Ingrese un numero: '))

print(mayor(a,b,c))