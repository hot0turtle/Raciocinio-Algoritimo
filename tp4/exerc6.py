n = int(input("fale um numero"))
s = int(0)
r = int(0)

while n > 0:
    r = n % 10
    s += r
    n //= 10

print(f"A soma dos digitos é {s}")
