from abc import ABC, abstractmethod
from rich import print
from math import pi
class Poligono(ABC):
    def __init__(self,qtd_lados=0):
        self.qtd_lados = qtd_lados

    @abstractmethod
    def perimetro(self):
        pass
    @abstractmethod
    def area(self):
        pass

class Quadrado(Poligono):
    def __init__(self,lado):
        super().__init__(qtd_lados=4)
        self.lado = lado

    def perimetro(self):
        perimetro = 4*self.lado
        return perimetro
    def area(self):
        area = self.lado*self.lado
        return area

class Circulo(Poligono):
    def __init__(self,raio):
        super().__init__(qtd_lados =0)
        self.raio = raio

    def perimetro(self):
        perimetro = 2*pi*self.raio
        return perimetro
    def area(self):
        area = pi*self.raio**2
        return area
