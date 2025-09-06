try:
    usuario = input("Digite o nome do usuário: ")
    senha = input("Digite a senha: ")

    if usuario == "Olegario" and senha == "1234":
        print("Bem-vindo ao Banco Sr.Olegario!")
        print("Deseja fazer alguma transação?")

        opcao = input("Digite 1-TRANSFERÊNCIA | 2-SALDO: ")

        if opcao == "2":
            escolha = input("Deseja ver seu saldo? SIM | NÃO: ")

            if escolha.upper() == "SIM":
                print("Seu saldo é de R$2500,00")
            elif escolha.upper() == "NÃO":
                print("Obrigado por usar nosso banco, volte sempre!")
            else: 
                valor = float(input("Qual o valor da transferência? R$"))
                if valor <= 2500:
                    print("Transferência realizada com sucesso!")
                else:
                    print("Saldo insuficiente para realizar a transferência.")
        else:
            print("Opção inválida, tente novamente.")
    else:
        print("Usuário ou senha incorretos. Tente novamente.")       

except ValueError:
    print("Erro: Entrada inválida. Certifique-se de digitar corretamente.")
