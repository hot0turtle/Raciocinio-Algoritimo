a = input("Escolha um desses canais \n 2 BANDEIRANTES \n 4 SBT \n 6 CNT \n 7 RECORD \n 9 CULTURA \n12 GLOBO  \n      ")
int(a)
b = False
while b != True:
    if a == 2:
        print("Canal bandeirantes")
        
    elif a == 4:
        print("Canal SBT")
        break
    elif a == 6:
        print("Canal CNT")
        break
    elif a == 7:
        print("Canal Record")
        break
    elif a == 9:
        print("Canal Cultura")
        break
    elif a == 12:
        print("Canal Globo")
        break
    else:
        print("Canal sem sinal escolha um disponivel\n")