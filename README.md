# Banco Simples em Python

Um pequeno programa em Python que simula um sistema de login e transações bancárias simples.

## Funcionalidades

- Login de usuário com nome e senha.
- Verificação de saldo.
- Realização de transferências, com verificação de saldo suficiente.
- Tratamento de entradas inválidas.

## Regras

- Usuário válido: `Olegario`
- Senha válida: `1234`
- Saldo inicial: R$2500,00

## Código

```python
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
                print("Opção inválida.")

        elif opcao == "1":
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

```

## Como usar

1. Clone este repositório ou baixe o arquivo Python.
2. Execute o programa:
   ```bash
   python nome_do_arquivo.py
   ```
3. Digite seu usuário e senha.
4. Escolha a opção desejada:
   - `1` - Transferência
   - `2` - Ver saldo
5. Siga as instruções na tela para completar a ação.

## Exemplo de Uso

```
Digite o nome do usuário: Olegario
Digite a senha: 1234
Bem-vindo ao Banco Sr.Olegario!
Deseja fazer alguma transação?
Digite 1-TRANSFERÊNCIA | 2-SALDO: 2
Deseja ver seu saldo? SIM | NÃO: SIM
Seu saldo é de R$2500,00
```

## Observações

- O programa trata entradas inválidas e informa erros quando necessário.
- Para transferências, o valor digitado não pode ultrapassar o saldo disponível.
