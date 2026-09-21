import json
from rich import print
class Livro:
    def __init__(self,nome,paginas):
        self.nome = nome
        self.pagina = paginas
        print(f"Voce acabou de abrir o livro {self.nome} e está na pagina [yellow] 1 [/]")

    def passar(self,avancar):
        fim = False
        try:
            with open("pag_atual.json","r",encoding="utf-8") as pag:
                livro = json.load(pag)
        except FileNotFoundError:
            livro = {"Pagina Atual":1}
        for i in range(avancar):
            if livro["Pagina Atual"]==self.pagina:
                print(f"[red] Você chegou ao fim do livro {self.nome}")
                fim = True
                livro["Pagina Atual"] = 1
                break
            else:
                livro["Pagina Atual"] += 1
                print(f"Pág{livro['Pagina Atual']} ▶",end=" ")
        if not fim:
            print(f"Você avançou {avancar} Paginas e ésta na pagina:[yellow] {livro['Pagina Atual']}")
        with open("pag_atual.json","w",encoding="utf-8") as pag:
            json.dump(livro,pag,indent=4,ensure_ascii=False)
    def voltar(self,voltar):
        try:
            with open("pag_atual.json","r",encoding="utf-8") as pag:
                livro = json.load(pag)
        except FileNotFoundError:
            livro = {"Pagina Atual":1}
        paginas_voltadas = 0
        for i in range(voltar):
            if livro["Pagina Atual"]<=1:
                print(f"Voce Já esta na Pagina [yellow] 1 [/] nao é possivel voltar mais paginas do livro {self.nome}")
                livro["Pagina Atual"] = 1
                break
            else:
                livro["Pagina Atual"] -= 1
                print(f"⇝ Pág{livro['Pagina Atual']} ", end=" ")
                paginas_voltadas +=1
        if paginas_voltadas>0:
            print(f"Você retornou {paginas_voltadas} Paginas e ésta na pagina:[yellow] {livro['Pagina Atual']}")
        with open("pag_atual.json","w",encoding="utf-8") as pag:
            json.dump(livro,pag,indent=4,ensure_ascii=False)
l1 = Livro("Shizuku",20)
l1.passar(5)
l1.passar(10)
l1.voltar(5)
l1.passar(5)