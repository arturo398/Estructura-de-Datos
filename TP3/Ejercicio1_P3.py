def palindromo(texto):
    texto_limpio=''
    texto=texto.lower()
    for letra in texto :
        if letra.isalnum():
            texto_limpio += letra

    return texto_limpio == texto_limpio[::-1]

texto= input("Ingrese una palabra que crea un palindromo: ")

if palindromo(texto):
    print(f"{texto} es un palindromo")
else:
    print(f"{texto} NO es un palindromo")
