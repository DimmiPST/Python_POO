from Classes_desafios.classe10 import *
from rich import print

modo = int(input("Qual a modo do frete? 1-uma consulta 2-consulta multipla "))
if modo == 1:
        while True:
            print("CALCULADOR FRETE 3000")
            distancia = int(input("DIGITE A DISTANCIA EM KM "))
            veiculo = int(input("""Escolha um veiculo 1-Moto 2-Caminhao 3-Drone
        OBS:CAMINHAO MIN 50KM
        DRONE MAX 10 KM\nDIGITE:"""))

            if veiculo == 1:
                transport = Moto(distancia)
                break
            elif veiculo == 2:
                transport = Caminhao(distancia)
                break
            elif veiculo == 3:
                transport = Drone(distancia)
                break
            else:
                print("[red] OPÇAO INVALIDA [/]")
        print(f"O frete  na distancia de {distancia} usando {type(transport).__name__} fica : {transport.calc_frete()}")
if modo == 2:
    distancia = int(input("DIGITE A DISTANCIA EM KM "))
    moto = Moto(distancia)
    caminhao = Caminhao(distancia)
    drone = Drone(distancia)
    viagem = [moto,caminhao,drone]
    for veiculo in viagem:
        try:
            print(f"DISTANCIA: {distancia} VEICULO:{type(veiculo).__name__} FRETE: {veiculo.calc_frete():.2f} KM")
        except Erro as E:
            print(f"DISTANCIA: {distancia} VEICULO:{type(veiculo).__name__} FRETE: {E} ")
