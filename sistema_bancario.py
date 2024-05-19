menu = """

    ==== MENU ====

    1 - Depositar
    2 - Sacar
    3 - Extrato
    0 - Sair

    ==============

    Operação desejada: """

saldo = 0
limite = 500
extrato = """

            ==== EXTRATO ====

"""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        deposito = float(input('''

            ==== DEPÓSITO ====

            Quanto gostaria de
                depositar?

            VALOR: R$ '''))
        saldo += deposito
        extrato += f"           Depósito de R$ {deposito:.2f} \n"
        print(f"""
            === Seu novo saldo é de R$ {saldo:.2f} ===""")

    elif opcao == "2":
        if saldo > 0:
            saque = float(input('''

                ==== SAQUE ====

                Quanto gostaria de
                    sacar?

                VALOR: R$ '''))
            saldo -= saque
            extrato += f"           Saque de    R$ {saque:.2f} \n"
            print(f"""
                === Seu novo saldo é de R$ {saldo:.2f} ===""")
        else:
            print(f"""
            === Saldo insuficiente para o saque, conta zerada. ===""")

    elif opcao == "3":
        if extrato == """

            ==== EXTRATO ====

""":
            
            print(f"""{extrato}           
            
            Não foram realizadas
            movimentações.
            =================
            """)

        else:
            print(f"""{extrato}           
                
           O saldo atual é de R$ {saldo:.2f}
            =================
            """)

    elif opcao == "0":
        break

    else:
        print("\n             Comando não reconhecido! Tente novamente.")