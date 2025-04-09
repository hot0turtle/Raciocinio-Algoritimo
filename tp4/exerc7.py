n = int(input("Digite o número de elementos da sequência de Fibonacci: "))
anterior = 0
atual = 1
i = 1

while i <= n:
    print(atual)
    proximo = anterior + atual
    anterior = atual
    atual = proximo
    i += 1