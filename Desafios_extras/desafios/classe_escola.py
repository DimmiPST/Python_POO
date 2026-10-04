from abc import ABC,abstractmethod

class Pessoa(ABC):

    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def aniver(self):
        self.idade += 1
        print(f"{self.nome} sua idade agora é {self.idade}")
    @abstractmethod
    def correr(self):
        pass

class Aluno(Pessoa):
    def __init__(self,curso,turma,nome,idade):
        super().__init__(nome = nome,idade = idade)
        self.curso = curso
        self.turma = turma
    def matricula(self):
        print(f"{self.nome} do {self.curso} com turma: {self.turma} fez matricula")

    def correr(self):
        print("aluno corre")

class Professor(Pessoa):
    def __init__(self,especialidade,nivel,nome,idade):
        super().__init__(nome,idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def aula(self):
        print(f"{self.nome} do {self.nivel} com especializaçao: {self.especialidade} está dando aula")

    def correr(self):
        print("fessor corre")

class Funcionario(Pessoa):
    def __init__(self,cargo,setor,nome,idade):
        super().__init__(nome,idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        print(f"{self.nome} do {self.setor} com cargo: {self.cargo} bateu o ponto")

    def correr(self):
        print("funcionario corre")
