import pickle

senha_gerente = 0

with open('TDE\Trabalho2\dados.pkl', 'rb') as f:
    d_load = pickle.load(f)



def menu():
    global account_type
    account_type = int(input("Bem-vindo ao Sistema Bancário!\nEscolha uma opção:\n1. Acessar como Cliente\n2. Acessar como Gerente\n3. Sair\n"))
    
    if account_type == 1:
        login_cliente()
    elif account_type == 2:
        login_gerente()


def login_cliente():
    menu_options = int(input("Menu Cliente:\n1. Consultar Saldo\n2. Depositar\n3. Sacar/Pix\n4. Simular Rendimento\n5. Voltar ao Menu Principal\n"))
    if menu_options == 1:
        print(d_load["balance"])
    elif menu_options == 2:
        dep = int(input("Quer depositar quanto?"))
        update_balance = int(d_load["balance"]) + dep
    elif menu_options == 3:
    
    elif menu_options == 4:

    elif menu_options == 5:
        menu()


def login_gerente():
    global contado
    contado = 0
    while contado < 3:
        senha = int(input("Digite a senha para acessar o modo gerente:"))
        if senha == senha_gerente:
            int(input("Menu Gerente:\n1. Cadastrar ou Trocar Nome do Clientez\n2. Corrigir Saldo do Cliente\n4. Consultar Status do Cliente\n5. Voltar ao Menu Principal"))
        elif senha != senha_gerente and contado < 3:
            contado += 1  
            print("Tentativa Incorreta")



menu()
