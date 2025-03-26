modulo = input("diga o numero pra dividir")

divisado = input("diga o numero pra ser dividido")

divisado = int(divisado)
modulo = int(modulo)

if modulo % divisado == 0:
    print(modulo,"é multiplo de", divisado)
else:
    print("nao é multiplo")