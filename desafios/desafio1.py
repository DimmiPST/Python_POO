from rich import print
from rich.panel import Panel
class Funcionario:
    nome_empresa ="Shizuku tec"
    def __init__(self,nome,setor,cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
    def apresentacao(self):
        return f"Meu nome é [blue]{self.nome} [/] trabalho de {self.cargo} no setor de {self.setor} na empresa {self.nome_empresa}"


painel_empresa = Panel(":money_bag:Cadastre suas informaçoes".center(50),title="Shizuku corp",width=50)
print(painel_empresa)
nome_funcionario = input("Qual seu nome?")
setor_funcionario = input("Qual seu setor?")
cargo_funcionario = input("Qual seu cargo?")
print("-"*50)
funcionario = Funcionario(nome_funcionario, setor_funcionario, cargo_funcionario)
print("-"*50)
print(funcionario.apresentacao())
