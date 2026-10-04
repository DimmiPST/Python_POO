from rich import print

class Churras:
    def __init__(self,nomechurrasco,pessoas):
        self.nomechurrasco = nomechurrasco
        self.pessoas = pessoas
    def analisar(self):
        print(f"[blue]{self.nomechurrasco}[/] quantidade pessoas: [blue]{self.pessoas}[/]")
        kgcarne= 0.400 * self.pessoas
        print(f"compre: {kgcarne:.2f} KG DE CARNE ")
        custototal = kgcarne *82.40
        print(f"Custo total: [blue]{custototal:.2f}[/]")
        precopessoa = custototal / self.pessoas
        print(f"custo pessoa: [blue]{precopessoa}[/]")

churra1 = Churras("CHURRAS RENGOKU",15)
churra1.analisar()