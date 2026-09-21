from rich import print
from rich.panel import Panel
class Produto:
    def __init__(self,nome,preco):
        self.nome = nome
        self.preco = preco
    def etiqueta(self):
        conteudo = f"{self.nome.center(30, ' ')}"
        conteudo += f" R${self.preco}"
        etiqueta = Panel(conteudo,width=34)
        print(etiqueta)

produto1 = Produto(nome="MOUSE GAMER",preco=500)
produto2 = Produto(nome="TECLADO GAMER",preco=500)
produto1.etiqueta()
produto2.etiqueta()