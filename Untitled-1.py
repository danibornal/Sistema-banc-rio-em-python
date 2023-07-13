class Banco:
    def __init__(self):
        self.saldo = 0

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente!")

    def extrato(self):
        print(f"Saldo atual: {self.saldo}")


# Uso do código
banco = Banco()

banco.deposito(100)  # Depositar R$ 100
banco.extrato()  # Imprimir saldo atual

banco.saque(50)  # Sacar R$ 50
banco.extrato()  # Imprimir saldo atual

banco.saque(1000)  # Tentar sacar R$ 1000 (saldo insuficiente)
banco.extrato()  # Imprimir saldo atual
