x = input("Digite uma letra")
vogais = ['a', 'e', 'i' ,'o', 'u']

while (len(x) > 1):
    x = input("Digite somente UMA letra")
else:
        
    if (x in vogais):
        print("é uma vogal")
    else:
        print("é uma consoante")
