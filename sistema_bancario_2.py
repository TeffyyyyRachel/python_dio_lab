def saque(*,saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_limite = valor > limite
    excedeu_saldo = valor > saldo
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_limite:
        print("\n\tOPERAÇÃO FALHOU!!! Saque excede o limite diário de R$500.00.")
    elif excedeu_saldo:
        print("\n\tOPERAÇÃO FALHOU!!! Saque excede o saldo disponível.")
    elif excedeu_saques:
        print("\n\tOPERAÇÃO FALHOU!!! Saque excede o limite diário de 3 saques.")
    
    elif valor > 0:
        saldo -= valor
        print(f"\n\t=== Saque de R${valor} realizado com sucesso! ===")
        extrato += f"\n\t=== Saque de R${valor}\t==="
        numero_saques += 1

    else: 
        print("\n\tOPERAÇÃO FALHOU!!!\tValor inválido.")

    return saldo, extrato, numero_saques

def deposito(saldo, valor, extrato,/):
    saldo += valor
    print(f"\n\t=== Depósito de R${valor} realizado com sucesso! ===")
    extrato += f"\n\t=== Depósito de R${valor}\t==="
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    if not extrato:
        print("Nenhuma operação ainda realizada.")
    else:
        print("\n\t  ====== EXTRATO ======")
        print(extrato)
        print(f"\n\tO saldo atual é de {saldo}")
        print("\n\t  =====================")

    return saldo, extrato

def cadastrar_usuario(usuarios):
    cpf = input("\n\tDigite os números de cpf sem pontuação: ")
    nome = input("\n\tNome completo: ")
    data_nascimento = input("\n\tData de nascimento (dd-mm-aaaa): ")
    endereco = input("\n\tInforme o endereço (logradouro, nro - bairro - cidade/Sigla estado): ")

    usuarios.append({"cpf":cpf, "nome":nome, "data_nascimento":data_nascimento, "endereco":endereco})

    print("\n\t=== Usuário criado com sucesso! ===")

def cadastrar_conta_corrente(agencia, numero_conta, usuario):
    
    return None

def listar_contas():
    return None

def menu():
    menu = """

    ==== MENU ====

    1 - Depositar
    2 - Sacar
    3 - Extrato
    4 - Cadastrar usuário
    5 - Criar nova conta
    0 - Sair

    ==============

    Operação desejada: """
    return input(menu)

def main():
    AGENCIA = "0002"
    LIMITE_DIARIO = 3

    saldo = 0
    numero_saques = 0
    limite_diario = 500
    extrato = ""
    usuarios = []
    contas = []

    while True:
        operacao_escolhida = menu()
        
        if operacao_escolhida == "1": # depósito
        
            while True:
                deposito_desejado = float(input("\n\tQual o valor deseja depositar? R$"))
                aviso_deposito = input(f"\n\tDeseja depositar R${deposito_desejado}? [S/N]").upper()
                if aviso_deposito == "S":
                    break
            
            saldo, extrato = deposito(saldo, deposito_desejado, extrato)
            print(f"\n\tO Saldo atual é de R${saldo}.")
        
        elif operacao_escolhida == "2": # saque
            while True:
                saque_desejado = float(input("\n\tQual valor deseja sacar? R$"))
                aviso_saque = input(f"\n\tDeseja sacar R${saque_desejado}? [S/N]").upper()
                if aviso_saque == "S":
                    break
            
            saldo, extrato, numero_saques = saque(saldo=saldo, valor=saque_desejado, extrato=extrato, limite=limite_diario, numero_saques=numero_saques, limite_saques=LIMITE_DIARIO)
            print(f"\n\tO Saldo atual é de R${saldo}.")
                        
        elif operacao_escolhida == "3": # extrato
            exibir_extrato(saldo, extrato=extrato)

        elif operacao_escolhida == "4": # cadastro de usuário
            cadastrar_usuario(usuarios)
            print(usuarios)

        elif operacao_escolhida == "5": # criação de nova conta
            cadastrar_conta_corrente(contas)
        
        elif operacao_escolhida == "0":
            break

        else:
            print("Escolha um número válido, entre 0 e 5.")

main()