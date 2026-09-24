from rich import print
from abc import ABC, abstractmethod

class Cafeteria(ABC):
    @staticmethod
    def ferver():
        print("fervendo Agua a 100º celsius")

    @abstractmethod


    def mistura(self):
        pass


    @abstractmethod
    def servir(self):
        pass


    def preparar(self):
        Cafeteria.ferver()
        self.mistura()
        self.servir()
        print("BEBIDA  PRAPARADA")

class Cafe(Cafeteria):
    def mistura(self):
        print("adicionando café")
    def servir(self):
        print("servindo cafe na xicara")

class Leite(Cafeteria):
    def mistura(self):
        print("adicionando leite")
    def servir(self):
        print("servindo leite na caneca")

class Cha(Cafeteria):
    def mistura(self):
        print("adicionando cha")
    def servir(self):
        print("servindo cha no chimarrao")