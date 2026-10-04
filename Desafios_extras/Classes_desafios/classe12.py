from rich import print
from abc import ABC,abstractmethod
import random
class Persona(ABC):
    def __init__(self,nome,vida):
        self.nome = nome
        self.vida = vida
        self.vidamax = vida
        self.golpes = []

    def atacar(self,alvo,dano):
        import random
        danorecalculado = random.randint(0,dano)
        print(f"{self.nome} atacou {alvo.nome} usando: {random.choice(self.golpes)} e causou [yellow]{danorecalculado}[/]")
        alvo.receber(danorecalculado)


    def receber(self,dano):
        self.vida -= dano
        print(f"{self.nome} recebeu [blue] {dano}[/]")

    @abstractmethod
    def curar(self):
        pass

class Guerreiro(Persona):
    def __init__(self,nome,vida):
        super().__init__(nome,vida)
        self.golpes = ["SOCO","SOCO MEGA FORTE","SOCO SUPER FORTE"]

    def curar(self):
        sorteio = random.randint(0,100)
        self.vida = min(self.vidamax, self.vida + sorteio)
        print(f"{self.nome} Recuperou {sorteio} usando habilidade berserker")

class Mago(Persona):
    def __init__(self,nome,vida):
        super().__init__(nome,vida)
        self.golpes = ["Bola fogo","BOLA AGUA","bola DE NEVE"]

    def curar(self):
        sorteio = random.randint(0, 100)
        self.vida = min(self.vidamax, self.vida + sorteio)
        print(f"{self.nome} Recuperou {sorteio}HP usando magia de cura")