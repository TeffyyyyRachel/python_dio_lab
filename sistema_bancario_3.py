class Conta():
    def __init__(self, saldo, numero, agencia, cliente, historico):
        self._saldo = saldo
        self._numero = numero
        self._agencia = agencia
        self._cliente = cliente
        self._historico = Historico()
    
    def mostrar_saldo(self):
        return
    
    @classmethod
    def nova_conta(self, cliente, numero):
        return cls(cliente, numero)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo
        saldo_zerado = saldo <= 0
        saldo_suficiente = saldo > 0

        if excedeu_saldo:
            print("OPERAÇÃO FALHOU! Valor pedido ultrapassa o saldo atual.")
            return False
    
        elif saldo_zerado:
            print("OPERAÇÃO FALHOU! Conta atualmente zerada. Faça um depósito antes de sacar.")
            return False
        
        elif saldo_suficiente and not excedeu_saldo:
            print("OPERAÇÃO REALIZADA COM SUCESSO!")
            return True
        
        else:
            print("OPERAÇÃO FALHOU! Tente novamente se atentando às informações fornecidas.")
            return False
    
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
        self.cpf = cpf_
        self.nome = no_me
        self.data_nasc_imento = data_nascimento__

