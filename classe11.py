from abc import ABC,abstractmethod
from rich import print

class Funcionario(ABC):
    salmin = 1612
    inss = 0.075
    def __init__(self,nome,salario_bruto):
        self.nome = nome
        self.salario_bruto = salario_bruto
        self.salario = 0

    @abstractmethod
    def calc_sal(self):
        pass

    def analisar(self):
            salario_equivalente = self.salario / Funcionario.salmin
            print(f"O salario liquido de {self.nome} liquido é {self.salario:.2f} e equivale a {salario_equivalente:.2f} salarios minimos")

class Horista(Funcionario):
    def __init__(self,nome,valorhoras,horastrabalhada):
        salario_bruto = valorhoras*horastrabalhada
        super().__init__(nome,salario_bruto)


    def calc_sal(self):
        self.salario = self.salario_bruto - self.salario_bruto * Funcionario.inss

class Mensal(Funcionario):
    pass

    def calc_sal(self):
        self.salario = self.salario_bruto - self.salario_bruto * Funcionario.inss
