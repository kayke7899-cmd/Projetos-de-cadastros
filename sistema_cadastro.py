# Programa de cadastro de nomes, CPF e telefone

nomes_cadastrados = []
cpf_cadastrados = []
telefone_cadastrados = []
# Loop principal do programa
while True:
    print("===MENU===")
    print("1. Cadastrar informações")
    print("2. Listar nomes cadastrados")
    print("3. Sair")
    
    opcao = input("Escolha uma opção: ")

    #Cadastrar informações
    if opcao == "1":
        nome = input("Digite nome:")
        cpf = input("Digite o CPF:")
        telefone = input("Digite o telefone:")
        nomes_cadastrados.append(nome)
        cpf_cadastrados.append(cpf)
        telefone_cadastrados.append(telefone)
        print(f"Informações de '{nome}' cadastradas com sucesso!")

    #Listar informarçoes cadastras
    elif opcao == "2":
       print("\n===INFORMAÇÕES CADASTRADAS===")
       if not nomes_cadastrados:
           print("Nenhum nome cadastrado.")
       for i in range(len(nomes_cadastrados)):
           print(f"Nome: {nomes_cadastrados[i]},\n CPF: {cpf_cadastrados[i]},\n Telefone: {telefone_cadastrados[i]}")

    #Sair do programa
    elif opcao == "3":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")
