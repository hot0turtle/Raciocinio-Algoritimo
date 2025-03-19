semana = ['blank', 'Domingo','Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabádo']

a = input("digite um numero de 1 a 7")
a = int(a)
if a < 7 or a >= 1:
    a = semana[a]
    print(a)
else:
    print("Insira um valor valido")