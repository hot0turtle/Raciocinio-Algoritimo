g = int(0)
j = 0 
c = 0
while g != 3:
    g = int(input("Quer vota em 1 Joao ou 2 Carlos?"))
    if g == 1:
        j += 1
    elif g == 2:
        c += 1
    
print(f"Carlos tem {c} votos, e Joao tem {j} votos")