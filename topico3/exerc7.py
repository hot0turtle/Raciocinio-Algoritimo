r1 = input(" Telefonou para a vítima? [S/N]")

c = 0

if r1 == 's':
    c += 1

r1 == input("Já trabalhou com a vítima? [S/N]")

if r1 == 's':
    c += 1

r1 = input("Mora perto da vítima? [S/N]")


if r1 == 's':
    c += 1
    
r1 = input("Tinha algum dívida com a vítima? [S/N]")

if r1 == 's':
    c += 1

r1 = input("Esteve no local do crime? [S/N]")

if r1 == 's':
    c += 1

print(c)