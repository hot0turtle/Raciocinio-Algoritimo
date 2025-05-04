import pickle
import os
contado = 0
senha_gerente = 0

if not os.path.exists("dados.pkl"): #caso dados n exista crie e gere o dicionario dentro dele se nao so continua
    dados = {"cliente": {"saldo": 0, "nome" : "John Bank"}}
    with open("dados.pkl", "wb") as arquivo:# pra salvar no arquivo pkl
        pickle.dump(dados, arquivo)
    print("Arquivo criado com saldo inicial de 0.")
else:
    print("Arquivo encontrado, carregando dados...")

while True: #pra garantir que voce sempre possa voltar pro menu tudo dentro de um while
    print("Bem-vindo ao sistema bancário!")
    print("Escolha uma opção: 1 Acessar como cliente  / 2 Acessar como gerente / 3 Sair")

    escolha = input("Digite o número da opção: ")

    if escolha == "3":
        exit()
    elif escolha == "1":
        while True: # todo menu do cliente
            print("Menu cliente: \n1-Consultar saldo \n2-Depositar \n3-Sacar/Pix \n4-Simular Rendimento \n5-Voltar ao menu principal")
            escolha_cliente = input("Digite o número de sua escolha: ")

            with open("dados.pkl", "rb") as arquivo:
                dados_carregados = pickle.load(arquivo) # pra ler o arquivo pkl

            if escolha_cliente == "1":
                print(f"Você possui {dados_carregados['cliente']['saldo']} reais.")

            elif escolha_cliente == "2":
                print("Deseja depositar quanto?")
                valor_deposito = int(input())
                dados_carregados["cliente"]["saldo"] += valor_deposito
                with open("dados.pkl", "wb") as arquivos:
                    pickle.dump(dados_carregados, arquivos)
                print(f"Você depositou R${valor_deposito:.2f}. Seu saldo atual é R${dados_carregados['cliente']['saldo']:.2f}.")

            elif escolha_cliente == "3":
                print("Deseja sacar quanto?")
                valor_saque = int(input())
                if valor_saque <= dados_carregados["cliente"]["saldo"]:
                    dados_carregados["cliente"]["saldo"] -= valor_saque
                    with open("dados.pkl", "wb") as arquivos:
                        pickle.dump(dados_carregados, arquivos)
                    print(f"Você sacou R${valor_saque:.2f}. Seu saldo atual é R${dados_carregados['cliente']['saldo']:.2f}.")
                else:
                    print("Saldo insuficiente para o saque.")

            elif escolha_cliente == "4":
                meses = 1
                saldo_atual = dados_carregados["cliente"]["saldo"]
                taxa_juros = 0.011

                while meses <= 12:
                    saldo_atual *= (1 + taxa_juros)
                    print(f"Mês {meses}: R${saldo_atual:.2f}")
                    meses += 1

                print(f"\nValor final após 12 meses: R${saldo_atual:.2f}")

            elif escolha_cliente == "5":
                print("Saindo da conta do cliente...")
                break

            else:
                print("Função inexistente. Tente outra opção.")

            input("\nPressione Enter para continuar...")
        
    elif escolha == "2":
        

        # checa a senha e para o codigo se errar 3 vezes
        while True:
            senha = int(input("Digite a senha para acessar o modo gerente:"))
            if senha == senha_gerente:
                break
            else:
                contado += 1
                if contado >= 3:
                    print("Bloqueando Acesso\n")
                    break
                print("Tentativa Incorreta\n")

        if senha == senha_gerente:
            while True: # todo menu do gerente
                escolha_gerente = int(input("Menu Gerente:\n1 Trocar Nome do Cliente\n2 Corrigir Saldo do Cliente\n4 Consultar Status do Cliente\n5 Voltar ao Menu Principal\n"))

                if escolha_gerente == 1:
                    with open("dados.pkl", "rb") as arquivo:
                        dados_carregados = pickle.load(arquivo)
                    novo_nome = input("Qual vai ser o novo nome do Cliente?")
                    dados_carregados["cliente"]["nome"] = novo_nome

                    with open("dados.pkl", "wb") as arquivo:
                        pickle.dump(dados_carregados, arquivo)
                    
                    print(f"Nome do cliente alterado para {dados_carregados["cliente"]["nome"]}.")
                
                elif escolha_gerente == 2:
                    with open("dados.pkl", "rb") as arquivo:
                        dados_carregados = pickle.load(arquivo)
                    print(f"O saldo atual do cliente é R${dados_carregados['cliente']['saldo']:.2f}.")
                    print("Qual e o saldo Correto?")
                    saldo_correto = int(input())
                    dados_carregados["cliente"]["saldo"] = saldo_correto
                    with open("dados.pkl", "wb") as arquivos:
                        pickle.dump(dados_carregados, arquivos)
                    print(f"Você alterou o saldo.O saldo atual do cliente é R${dados_carregados['cliente']['saldo']:.2f}.")
                
                elif escolha_gerente == 4: # como na atividade voce foi de 2 pra 4 eu tbm botei aqui so pra garantir
                    with open("dados.pkl", "rb") as arquivo:
                        dados_carregados = pickle.load(arquivo)
                    print(f"O Cliente {dados_carregados["cliente"]["nome"]} atualmente possui: R${dados_carregados['cliente']['saldo']:.2f}.")
                
                elif escolha_gerente == 5:
                    print("Voltando ao menu principal...")
                    break
                
                else: # pra evitar que o codigo saia se digitar algo errado
                    print("Opção inválida. Tente novamente.")
    
    if contado >= 3: # para funcionamento se senha for errada 3 vezes
                    break

