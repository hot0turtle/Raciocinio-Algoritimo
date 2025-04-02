tot = int(input("Qual o valor da venda"))
com = 0
if tot > 1000:
    com = tot * 0.08
elif tot <= 1000 and tot > 500:
    com = tot * 0.07
elif tot <= 500 and tot > 100:
    com = tot * 0.06
elif tot <= 100:
    com = tot * 0.05

print(com)