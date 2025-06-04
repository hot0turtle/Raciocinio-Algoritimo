n = input()

M = []
for i in range(12):
    row = []
    for j in range(12):
        value = float(input())
        row.append(value)
    M.append(row)


soma = 0
media = 0
count = 0

if n == 'S':
    for i in range(12):
        for j in range(12):
            if i > j:
                soma += M[i][j]
    print(f"{soma:.1f}")

elif n == 'M':
    for i in range(12):
        for j in range(12):
            if i > j:
                media += M[i][j]
                count += 1
    media = media / count
    print(f"{media:.1f}")
