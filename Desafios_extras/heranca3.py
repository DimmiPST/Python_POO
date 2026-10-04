from rich import print

class Aviso:
    def __init__(self,nivel,msg):
        self.nivel = nivel
        self.msg = msg
        ##CRIA UM AVISO DA ANOMALIA
class Central:
    ##REGISTRA ESSA ANOMALIA NA CENTRAL
    def __init__(self):
        self.historico : list[Aviso] = []
        ##ADICIONANDO UM HISTORICO DE ANOMALIAS DE FORA

    def receber(self,alerta : Aviso): ##ADCIONANDO UMA ANOMALIA NO HISTORICO POR DENTRO
        self.historico.append(alerta)
        if alerta.nivel == "CRÍTICO": ##SE O ALERTA FOR CRITICO AVISA
            print("[red] NIVEL CRITICO DETECTADO ")
        else:
            print("[blue] TUDO NORMAL")

class Sensor: ##SENSOR CRIADO A PARTIR DA CENTRAL
    def __init__(self,nome_sensor,central: Central):
        self.nome_sensor = nome_sensor
        self.central = central

    def detectar(self,nivel_anomalia): ##FUNÇAO DETECTAR

        obtemp = Aviso(nivel_anomalia,f"Ameaça do tipo {nivel_anomalia} DETECTADA NO SISTEMA")
        self.central.receber(obtemp)


central_seguranca = Central()
sensor_porta_ssh = Sensor(nome_sensor="Sensor-SSH-DMZ", central=central_seguranca)

sensor_porta_ssh.detectar("MÉDIO")
sensor_porta_ssh.detectar("CRÍTICO")
