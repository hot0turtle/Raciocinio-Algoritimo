n1 = int(input("Coloque notas de 0 a 10: "))
n2 = int(input("Coloque notas de 0 a 10: "))
n3 = int(input("Coloque notas de 0 a 10: "))
med = (n1+n2+n3)/3

if med >= 10 and med <=9:
    print("Parabens nota A, Aprovado")
elif med < 9 and med >= 7.5:
    print("Nota B, Aprovado")
elif med >= 6 and med < 7.5:
    print("Nota C , Aprovado")
elif med >= 4 and med < 6:
    print("Nota D, Reprovado")
elif med < 4:
    print("Nota E, Reprovado")