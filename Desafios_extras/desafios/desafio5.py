from rich import print
class Gamer:
    def __init__(self,nome,nick):
        self.nome = nome
        self.nick = nick
        self.jogosfavoritos = []
        self.contagem = 0
    def adicionar_jogo(self,nomejogos):
        novojogo = str(nomejogos)
        self.contagem += 1
        self.jogosfavoritos.append(novojogo)
    def mostrar_player(self):
        print(f"Nome : {self.nome}")
        print(f"Nick : {self.nick}")
        print("Jogos  favoritos:")
        jogoordem = sorted(self.jogosfavoritos)
        for pos,jogo in enumerate(jogoordem):
            print(      f"JOGO{pos+1} : {jogo}")


print("--------------------------------")
print(" criando objeto")
g1 = Gamer("ROBERTO PEREIRA","DISCORD77")
while True:
    try:
        escolha = int(input("1- adicionar jogo 2-sair"))
        if escolha == 1:
            nomejogo = input("Nome do jogo:")
            g1.adicionar_jogo(nomejogo)
        elif  escolha == 2:
            break
        else:
            print("DIGITE UMA ESCOLHA VALIDA")
    except ValueError:
        print("DIGITE UMA ESCOLHA VALIDA")

g1.mostrar_player()
