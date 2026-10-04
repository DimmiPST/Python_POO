#class
class Poo:
    def __init__(self):
        #atributo cliaçao
        self.nome = ""
        self.idade = 0

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

obj = Poo()
obj.idade = 16
obj.nome = "Jorge 100grau"
for i in range(10):
    obj.ani()
for i in range(5):
    obj.animenos()
obj2=Poo()
obj2.idade = 109
obj2.nome = "nikky idiota"
print(f"{obj.men()} \n{obj2.men()}")
obj2.trocar()
print(obj2.men())
obj.idnova()
print(obj.men())
obj.anonas()