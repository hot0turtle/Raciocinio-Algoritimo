a = int(input("Fale 1 numero"))
b = int(input("Fale 1 numero"))
c = int(input("Fale 1 numero"))

if a > b and a > c:
    if b > c:
        print(a, b, c)
    elif c > b:
        print(a, c, b)
elif b > a and b > c:
    if a > c:
        print(b, a, c)
    elif c > a:
        print(b, c, a)
elif c > a and c > b:
    if a > b:
        print(c, a, b)
    elif b > a:
        print(c, b, a)
