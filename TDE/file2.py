a,b,c = input().split()

a = int(a)
b = int(b)
c = float(c)

i,j,l = input().split()

i = int(i)
j = int(j)
l = float(l)

total = float(b * c + j * l)

print("Valor a pagar: R$","%.2f" % total)
