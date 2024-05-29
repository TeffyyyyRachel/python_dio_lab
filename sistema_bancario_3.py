class Conta():
    def __init__(self, saldo, numero, agencia, cliente, historico):
        self.saldo = saldo
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = historico
    
    def mostrar_saldo(self):
        return
    
    def nova_conta(self, cliente, numero):
        return
    
    def sacar(self, valor):
        return
    
    def depositar(self, valor):
        return

class ContaCorrente(Conta):
    def __init__(self, saldo, numero, agencia, cliente, historico, limite, limite_saques):
        super().__init__(saldo, numero, agencia, cliente, historico)
        self.limite = limite
        self.limite_saques = limite_saques

class Cliente():
    def __init__(self, endereco, contas):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
    
    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, endereco, contas, cpf, nome, data_nascimento):
        super().__init__(endereco, contas)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

