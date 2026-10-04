from rich import print
class Caneta:
    def __init__(self,cor="white"):
        self.cor = cor
        self.destampar = False
    def destampar(self):
        self.destampar = True
        print("CANETA DESTAMPADA")
    def escrever(self,frasec):
        if self.destampar:
            print(f"[{self.cor}] {frasec} [/]")
        else:
            print("[red] ABRA A CANETA")

print("-"*50)
print(" CANETA CIB")
while True:
    try:
        escolha_caneta = int(input("1-vermelho 2-azul 3-verde"))
        if escolha_caneta == 1:
            cor_caneta = "red"
            break
        elif escolha_caneta == 2:
            cor_caneta = "blue"
            break
        elif escolha_caneta == 3:
            cor_caneta = "green"
            break
        else:
            print("[red] DIGITE UMA OPÇAO VALIDA [/]")
    except ValueError:
        print("[red] DIGITE OPÇAO VALIDA [/]")
print("Criando caneta")
c1 = Caneta(cor_caneta)
while True:
    try:
        escolha_metodo = int(input("1- Deestampar 2-escrever 3-mudar cor 4-sair do programa"))
        if escolha_metodo == 1:
            print("DESTAMPANDO CANETA")
            c1.destampar = True
        elif escolha_metodo == 2:
            frase =input("Digite uma frase: ")
            c1.escrever(frase)
        elif escolha_metodo == 3:
            escolha_caneta = int(input("1-vermelho 2-azul 3-verde"))
            if escolha_caneta == 1:
                cor_caneta = "red"
                c1 = Caneta(cor_caneta)
            elif escolha_caneta == 2:
                cor_caneta = "blue"
                c1 = Caneta(cor_caneta)
            elif escolha_caneta == 3:
                cor_caneta = "green"
                c1 = Caneta(cor_caneta)
            else:
                print("[red] DIGITE UMA OPÇAO VALIDA [/]")
        elif escolha_metodo == 4:
                print("OBRIGADO POR USAR")
                break
        else:
            print("DIGITE UMA OPÇAO VALIDA ")
    except ValueError:
        print("[red] DIGITE CORRETAMENTE [/]")