

names = ['João', 'Pedro', 'Rafael', 'Larissa', 'Laura', 'Ana']

n = input("qual o seu nome?")

names.insert(6,n)
x = names.count(n)    

if x > 1:
    print("Esse nome ja esta ocupado")
    names.remove(n)

else:
    print("Nome adicionado com sucesso")

