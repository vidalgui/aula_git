class Conta:
    def __init__(self, saldo, titular):
        self.saldo = saldo
        self.titular = titular
    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de {valor} realizado. Seu saldo agora é de {self.saldo}")
    def sacar (self, valor):
        if self.saldo < valor:
            print("Não há saldo para realizar essa operação")
        else:
            self.saldo -= valor
            print(f"Saque de {valor} realizado. Seu saldo é de {self.saldo}")

a = Conta(20, "guiba")
a.depositar(10)
a.sacar(10)
a.depositar(100)