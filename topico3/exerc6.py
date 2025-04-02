a = input("Digite R pra Rock T pra Tesoura  P pra papel")
b = input("Jogador 2 Digite R pra Rock T pra Tesoura  P pra papel")

if a == b:
    print("Empate")
elif a == 'r' and b == 't':
    print("Jogador 1 Ganhou")
elif a == 'p' and b == 'r':
    print("Jogador 1 Ganhou")
elif a == 't' and b == 'p':
    print("Jogador 1 Ganhou")
elif b == 'r' and a == 't':
    print("Jogador 2 Ganhou")
elif b == 'p' and a == 'r':
    print("Jogador 2 Ganhou")
elif b == 't' and a == 'p':
    print("Jogador 2 Ganhou")