frase = "Vetores precisam Sumir"
frase2 = ''
print(frase)
tam = len(frase)
#ord() -> carac -> num
#chr() -> num-> car
for i in range(tam):

    num = ord(frase[i])
    #print(frase[i],num)
    #Letras maiusculas
    if num >= 65  and num <= 90:
        print(frase[i], num, num + 32, chr(num+32))
        num += 32
        letra = chr(num)

        frase2 += letra
    elif num >= 97  and num <= 122:
        print(frase[i], num, num - 32, chr(num-32))
        num -= 32
        letra = chr(num)
        frase2 += letra
    else:
        print(frase[i], num)
        frase2 += frase[i]

print(frase2)