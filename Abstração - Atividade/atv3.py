class ContaBancaria:
    def __init__(self, titular, saldo, numero, ):
        self.titular = titular
        self.saldo = saldo
        self.numero = numero
    def depositar(self, deposito):
        self.saldo += deposito

    def sacar(self, saque):
        if saque <= self.saldo:
            self.saldo -= saque

    def exibir_saldo(self):
        print(f"Saldo atual da conta de {self.titular}: R${self.saldo}")

conta1 = ContaBancaria("Julia", 1000, "12345")
a = int(input('Digite o valor que vc deseja sacar:'))
conta1.sacar(a)
conta1.exibir_saldo()

b = int(input('Digite o valor que vc deseja depositar:'))
conta1.depositar(b)
conta1.exibir_saldo()
