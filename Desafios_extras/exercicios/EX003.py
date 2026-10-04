from rich import print
from rich import inspect
class ContaBank:
    """Classe feita com poo pra sdimular uma conta bancaria"""
    def __init__(self,nome,id_conta,saldo):
        self.titular = nome
        self.id = id_conta
        self.saldo = saldo
        print(f"CONTA{self.id} CRIADA COM SUCESSO SALDO: {self.saldo}")
    def __str__(self):
        return f"A conta {self.titular} com ID: {self.id} e R${self.saldo:,.2f} de dinheiro e Pertence a classe: {self.__class__.__name__}"
    def depositar(self,valor):
        self.saldo += valor
        print(f"deposito de R${valor:,.2f} realizado com sucesso")
    def sacar(self,valor):
        if valor == 0:
            print("Nao é possivel sacar zero reais")
        elif valor > self.saldo:
            print(f"Voce nao pode realizar um saque Maior do que seu saldo, realize um saque até R${self.saldo:,.2f}")
        else:
            self.saldo -= valor
            print(f"Saque no valor de {valor} realizado com sucesso")

    def mostrar(self):
        print(f" seu saldo é de:{self.saldo}")

print("-"*50)
print("ROUND 6 BANK")
print("-"*50)
nomeconta = input("Digite O nome da conta: ")
idconta = int(input("Digite o ID da conta: "))
saldo_conta = float(input("Digite o saldo: "))
conta = ContaBank(nomeconta,idconta,saldo_conta)
deposito = int(input("Digite o deposito: "))
conta.depositar(deposito)
conta.mostrar()
saque = int(input("Digite o valor do saque: "))
conta.sacar(saque)
conta.mostrar()
inspect(conta)