from Classes_desafios.classe12 import *
from rich import print

print("RPG GUANABARA")
p1 = Guerreiro("ORC",450)
p2 = Mago("Rimuru",500)

print(f"{p1.nome} atacando {p2.nome}")
p1.atacar(p2,250)

print(f"{p2.nome} atacando {p1.nome}")
p2.atacar(p1,250)
print("VIDA DOS PERSONAGEM:")
print(f"{p1.nome} vida : {p1.vida}")
print(f"{p2.nome} vida : {p2.vida}")

print("CURAR VIDA")

print(f"{p1.nome} curando vida")
p1.curar()
print(f"{p2.nome} curando vida")
p2.curar()