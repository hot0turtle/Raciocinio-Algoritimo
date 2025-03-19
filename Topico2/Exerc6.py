ano = input("Diga o ano")
ano = int(ano)
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print("É um ano Bisexto")
else:
        print("Não é um ano bissexto")