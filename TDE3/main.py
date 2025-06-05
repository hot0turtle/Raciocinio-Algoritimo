import math

data = [[120, 10, 3, 250, 'P1'],
        [200, 25, 5, 400, 'P2'],
        [80, 5, 2, 180, 'P1'],
        [300, 30, 6, 500, 'P3'],
        [250, 40, 7, 600, 'P3'],
        [150, 12, 4, 320, 'P2'],
        [90, 8, 3, 200, 'P1'],
        [310, 35, 6, 520, 'P3'],
        [170, 15, 4, 350, 'P2'],
        [85, 6, 2, 190, 'P1'],
        [220, 18, 5, 410, 'P2'],
        [305, 38, 6, 510, 'P3'],
        [130, 11, 3, 270, 'P1'],
        [260, 42, 7, 580, 'P3'],
        [160, 14, 4, 330, 'P2'],
        [100, 9, 2, 210, 'P1'],
        [240, 28, 6, 460, 'P3'],
        [180, 16, 4, 370, 'P2'],
        [95, 7, 2, 195, 'P1'],
        [270, 40, 6, 590, 'P3']]

def calcularPerfil():
    dow = int(input("Criando novo Usuario insira as seguintes informacoes:\nMb de dowload Diario\n"))
    upl = int(input("Upload medio Diario\n"))
    simult = int(input("Numero de acessos simult\n"))
    conexao = int(input(" Tempo medio de conexao min\n"))
    delt = 99999
    for item in data:
        d = math.sqrt((dow - item[0])**2 + (upl - item[1])**2 + (simult - item[2])**2 + (conexao - item[3])**2)
        if d < delt:
            delt = d
            new_p = item[4]

        new_user = [dow, upl, simult, conexao, new_p]
        
    data.append(new_user)
    print(data)
    cont = int(input("Quer criar um novo usuario?\n1 = Sim\n2 = Nao"))
    if cont == 1:
        calcularPerfil()
    else:
        print("ate a proxima")
        


calcularPerfil()