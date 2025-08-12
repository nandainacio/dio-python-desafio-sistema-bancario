menu = '''
==== SISTEMA BANCÁRIO ===

[D] Depósito
[S] Saque
[E] Extrato
[Q] Sair

'''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3

while True:

    opcao = input(menu)

    if opcao.upper() == "D":
        valor_deposito = float(input("Digite o valor para depósito: R$"))
        if valor_deposito <= 0:
            print("Valor inválido para depósito.")
        else:
            saldo += valor_deposito
            extrato += f'Depósito: R${valor_deposito:.2f}\n'
    elif opcao.upper() == "S":
        if numero_saques == LIMITE_SAQUE:
            print("Você ultrapassou o limite de 3 saques por dia!")
        else:
            valor_saque = float(input("Digite o valor para saque: R$"))
            if valor_saque > 500:
                print("Você pode sacar até R$500,00")
            elif valor_saque <= 0:
                print("Digite um valor válido para saque")
            elif valor_saque > saldo:
                print(f"Saldo insuficiente para saque. SALDO {saldo:.2f}")
            else:
                saldo -= valor_saque
                numero_saques += 1
                extrato += f'Saque: R${valor_saque:.2f}\n'
    elif opcao.upper() == "E":
        if extrato == '':
            print("Não foram realizadas movimentações")
        else:
            print("====== EXTRATO BANCÁRIO ======")
            print(extrato)
            print(f"Seu saldo é R${saldo:.2f}")
    elif opcao.upper() == "Q":
        break
    else:
        print("Operação inválida. Digite a operação desejada")
