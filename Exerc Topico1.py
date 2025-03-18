#Exerc1

num1 = 10 

num2 = 7

print("a soma dos numeros é: ", num1 + num2)

#exer2

ante = num1 - 1

afte = num1 + 1 

print(ante, num1, afte)

#exerc3

total = 100

recebido= 120

troco = recebido - total
print(troco)

#exerc4

t = 354
g = t * 0.1

print("a gorjeta é:",g)

#exerc5

larg = 9.5
profu = 57

mq= larg * profu

print(mq,"metros quadrados")

#exerc6 

pav= 4

mq2 = larg * profu * pav

print(mq2,"metros quadrados no quarto")

#exerc7
def average(arr):
    return sum(arr) / len(arr)  

idades = [12,15,17,18,41]
print("A média de idades é:",average(idades))

#exerc8

nasc = 1984
atual = 2025

print("a idade atual é",atual - nasc)
