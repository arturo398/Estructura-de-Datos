def fecha(num1, num2, num3):
    dia=0
    mes=0
    año=0
    if num1>0 and num1<=30:
        dia=1
    else:
        print('Esta mal el dia')
        
    if num2>0 and num2<=12:
        mes=1
    else:
        print('Esta mal el mes')
    
    if num3<=2024:
        año=1
    else:
        print('Esta mal el año')

    if dia==mes==año:
        return True

dia=int(input('Ingrese un dia valido: '))
mes=int(input('Ingrese un mes valido: '))
año=int(input('Ingrese un año valido: '))

fecha(dia,mes,año)