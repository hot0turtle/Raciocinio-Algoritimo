N = input()
N = int(N)

m = N % 365  

s = N // 365
h = m // 30
mes = m % 30

print(f'{s} ano(s)\n{h}mes(es)\n{mes}dia(s)')


