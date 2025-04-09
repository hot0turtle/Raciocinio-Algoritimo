import random
g = 0
tentativa = 0
x = random.randint(1,100)
while x != g:
    g = int(input("Qual valor de x|?"))
    if g != x and tentativa < 5:
        print(f"vc esta { g - x} errado")
        tentativa += 1
    elif tentativa >=5:
        print("perdeu todas as vidas")
        break
    elif x == g:
        print(f"Parabens o numero era {x}")
        break