from rich import print

class Package:
    def __init__(self,ip_og : str,ip_dt :str,door : int, package : str):
        self.ip_og = ip_og
        self.ip_dt = ip_dt
        self.doors = door
        self.package = package

class Firewall:
    def __init__(self,d_lock : list):
        self.doors_lock = d_lock

    def analyze_package(self,data_package: Package):
        print(f"Firewall analyzing THE IP ORIGIN  {data_package.ip_og} intended THE DOOR : {data_package.doors}")
        if data_package.doors in self.doors_lock:
            print(f"[red][BLOCKED] THE DOOR {data_package.doors}  FIREWALL IS IN FIREWALL DOORS BLOCKED ")
            return False
        else:
            print(f"[green][OPEN] THE DOOR IS OPEN AND FIREWALL IS NOT BLOCKED ")
            return True
    def analyze_packages(self,list_package : list[Package]):
        print(f"RECEIVED {len(list_package)} PACKAGES ")
        for package in list_package:
            self.analyze_package(package)

#CRIANDO OBJETOS

p1 = Package("400.289.22","229.820.04",42,"sending cat pictures")
p2 = Package("94.131.228.157","142.86.137.176",67,"sending content malicious")

Fiw = Firewall([67,87,90,875,876,98])
Fiw.analyze_packages([p1,p2])
