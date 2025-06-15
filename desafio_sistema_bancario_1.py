menu = """

[1] DEPOSITAR
[2] SACAR
[3] EXTRATO
[0] SAIR

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        print("Deposito")
    elif opcao == "2":
        print("Saque")
    elif opcao == "3":
        print("Extrato")
    elif opcao == "0":
        break
    else:
        print("X Operação invalida X - Selecione novamente a opção desejada.")
    