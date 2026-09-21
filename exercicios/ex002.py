
class Poo:
    """Classe pra testar a programaçao orientada a objetos
        atributos: Nome idade
        metodos: Ani(soma +ano)
        animenos(reduz um ano)
        trocar(insere um novo nome pro atributo nome d o objeto)
        idnova(atualiza os anos)
        anonas(calcula o ano de nascimento)"""
    def __init__(self,nomext ="Nao informado",idadext= 0):
        #atributo cliaçao
        self.nome = nomext
        self.idade = idadext

    def ani(self):
        self.idade += 1

    def animenos(self):
        self.idade -= 1
    def trocar(self):
        self.nome = input("Digite o novo nome: ")

    def idnova(self):
        at = int(input("quer atualizar quantos anos?"))
        for cont in range(at):
            self.idade += 1
    def anonas(self):
        anonas = 2026 - self.idade
        print(f"ano de nascimento:{anonas}")
    def men(self):
        return f"feliz aniversario {self.nome} sua idade agora é {self.idade}"
    def __str__(self):
        return f"O OBJETO PERTENCE A CLASS {self.__class__.__name__} COM ATRIBUTOS: nome: {self.nome} idade: {self.idade}"
    def __getstate__(self):
        return f"{self.nome} idade: {self.idade}"
obj = Poo("Joao",18)
obj2=Poo("Rodofl",98)
obj3 =Poo()
print(f"Antes de atualizar:{obj2.men()}")
obj2.idnova()
print(f"Depois de atualizar:{obj2.men()}")
print(Poo.__doc__)
print(obj2)
print(obj2.__getstate__())
print(obj.__class__.__name__)