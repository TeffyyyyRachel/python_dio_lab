def saque(*,saldo, valor, extrato, limite, numero_saques, limite_saques):
    return saldo, extrato

def deposito(saldo, valor, extrato,/):
    return saldo, extrato

def extrato(saldo, /, *, extrato):
    return saldo, extrato

def cadastrar_usuario(nome, data_nascimento, cpf, endereco, usuario):
    return None

def cadastrar_conta_corrente(agencia, numero_conta, usuario):
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
    valor_sacado_dia = 0
    numero_saques = 0
    limite_diario = 500
    extrato_mensagens = ""
    usuario = []
    contas = []

    while True:
        operacao_escolhida = menu()
        

        if operacao_escolhida == "1": # depósito
            deposito()
        
        elif operacao_escolhida == "2": # saque
            if saldo == 0:
                print("\n     == Conta zerada. Faça um depósito antes de sacar. ==")
            else:
                saque()
        
        elif operacao_escolhida == "3": # extrato
            extrato()

        elif operacao_escolhida == "4": # cadastro de usuário
            cadastrar_usuario()

        elif operacao_escolhida == "5": # criação de nova conta
            cadastrar_conta_corrente()
        
        elif operacao_escolhida == "0":
            break

        else:
            print("Escolha um número válido, entre 0 e 5.")

main()