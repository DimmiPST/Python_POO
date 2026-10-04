from abc import ABC, abstractmethod
from rich import print

class Erro(Exception):
    pass

class Transporte(ABC):
    def __init__(self,distancia):
        self.dista = distancia
        self.frete = 0

    @abstractmethod
    def calc_frete(self):
        pass


class Moto(Transporte):
    fator = 0.50
    def __init__(self,dist):
        super().__init__(dist)

    def calc_frete(self):

        self.frete = self.dista*Moto.fator
        return self.frete


class  Caminhao(Transporte):
    fator = 1.20
    def __init__(self,dist):
        super().__init__(dist)

    def calc_frete(self):

        if self.dista >=50:
            self.frete = self.dista*Caminhao.fator
            return self.frete

        else:
            raise Erro("[red] DISTANCIA MINIMA 50KM")


class Drone(Transporte):
    fator = 9.50
    def __init__(self,dist):
        super().__init__(dist)

    def calc_frete(self):

        if self.dista <=10:
            self.frete = self.dista*Drone.fator
            return self.frete

        else:
            raise Erro("[red] DISTANCIA MAXIMA  10KM")