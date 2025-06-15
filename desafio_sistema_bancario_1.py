menu = """

[1] DEPOSITAR
[2] SACAR
[3] EXTRATO
[0] SAIR

"""

saldo = 0.0
limite = 500.0
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":

        valor = float(input("VALOR PARA DEPOSITO: "))
        saldo += valor
        extrato += f"DEPOSITO: R$ {valor:.2f}\n"
        print(f"\nSALDO ATUAL: R$ {saldo:.2f}")

    elif opcao == "2":

        if numero_saques < LIMITE_SAQUES:

            valor = float(input("VALOR DO SAQUE:"))

            if valor <= saldo and valor <= limite:

                saldo -= valor
                numero_saques += 1
                extrato += f"SAQUE: R$ {valor:.2f}\n"
                print(f"\nSALDO ATUAL: R$ {saldo:.2f}")

            elif valor > saldo:
                print(f"\nERRO -> Sem saldo suficiente.\nSALDO ATUAL: R$ {saldo:.2f}")
            else:
                print(f"\nERRO -> Valor maior que o limite autorizado.\nLIMITE: R$ {limite:.2f}")
            
        else:
            print("\nERRO -> Limite de saques atingido.")

    elif opcao == "3":
        
        if not extrato:
            print("EXTRATO VAZIO -> SEM OPERAÇÕES")
        else:
            print("--- EXTRATO DAS OPERAÇÕES ---")
            extrato += "-----------------------------\n"
            extrato += f"SALDO ATUAL: R$ {saldo:.2f}"
            print(extrato)

    elif opcao == "0":
        break
    else:
        print("Operação invalida - Selecione novamente a opção desejada.")
    