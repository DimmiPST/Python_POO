from Classes_desafios.classe11 import *
from rich import print
from rich.console import Console
l= Console()


Funcionario = []
while True:
    input("Press enter")
    l.clear()
    print("[bold cyan]=== BEM-VINDO À EMPRESA JUPTER ===[/bold cyan]\n")
    escolher = int(input("1-Cadastar 2 - Visualizar 3-sair"))
    if escolher == 1:
        print("Selecione o tipo de funcionário:")
        print("1 - Horista")
        print("2 - Mensalista")
        opcao = int(input("Digite: "))
        func = int(input("Quantos funcionarios quer cadastrar?"))
        if opcao == 1:
            for funcionario in range(func):
                nome = input(f"Digite o nome do {funcionario+1}funcionário: ")
                valorhoras = float(input(f"Digite o valor da {funcionario+1} hora (R$): "))
                horastrabalhada = float(input(f"Digite as horas trabalhadas: "))
                Funcionario.append(Horista(nome,valorhoras,horastrabalhada))
        elif opcao == 2:
            for funcionario in range(func):
                nome = input(f"Digite o nome do {funcionario+1}funcionário: ")
                salario_bruto = float(input("Digite o salário bruto (R$): "))
                Funcionario.append(Mensal(nome,salario_bruto))
    elif escolher == 2:
        hor_men = int(input("Visualizar 1-horistas 2-mensalista 3-todos"))
        if hor_men == 1:
            print("HORISTAS:")
            for horas in Funcionario:
                if isinstance(horas,Horista):
                    horas.calc_sal()
                    horas.analisar()
        elif hor_men == 2:
            print("MENSALISTAS:")
            for mensal in Funcionario:
                if isinstance(mensal,Mensal):
                    mensal.calc_sal()
                    mensal.analisar()
        elif hor_men == 3:
            print("HORISTAS:")
            for horas in Funcionario:
                if isinstance(horas,Horista):
                    horas.calc_sal()
                    horas.analisar()
            print("MENSALISTAS:")
            for mensal in Funcionario:
                if isinstance(mensal,Mensal):
                    mensal.calc_sal()
                    mensal.analisar()
            total_horistas = len([f for f in Funcionario if isinstance(f,Horista)])
            total_mensalistas = len([f for f in Funcionario if isinstance(f,Mensal)])
            print(f"TOTAL MENSALISTA:{total_mensalistas} TOTAL HORISTAS:{total_horistas}")
        else:
            print("[red] ERRO [/]")
    elif escolher == 3:
        print("[red] SAINDO  [/]")
        break
    else:
        print("[red] ERRO [/]")