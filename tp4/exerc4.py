import random
g = 0
x = random.randint(1,100)
while x != g:
    g = int(input("Qual valor de x|?"))
    if g != x:
        print(f"vc esta { g - x} errado")




print(f"Parabens o numero era {x}")