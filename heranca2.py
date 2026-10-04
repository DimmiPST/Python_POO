from rich import print

class Server:
    def __init__(self,correct_user : str,correct_pin : str ,try_failed : int =0,blocked : bool =False ):
        self.correct_user = correct_user
        self.correct_pin = correct_pin
        self.try_failed = try_failed
        self.blocked = blocked
    def authenticate(self,password):
        if self.blocked:
            print("[red] AUTHENTICATE RECUSED TRY EXCEEDED")
            return False
        else:
            if password != self.correct_pin:
                self.try_failed += 1
                tentativas = 15 - self.try_failed
                print(f"[red] incorrect password remain {tentativas} try")
                if self.try_failed >= 15:
                    self.blocked = True
                return False
            else:
                print(f"[green] password: {password} correct")
                self.try_failed = 0
                return True

class Ataque:
    @staticmethod
    def login(server : Server,list_pin1 : list[str]):
        for senha in list_pin1:
            if server.blocked:
                print(f"[red] BLOCKED")
                break
            print(f"Trying {senha}")
            resultado = server.authenticate(senha)
            if resultado:
                print("[bold green]Success! Stopping brute force.[/bold green]")
                break



#COMEÇANDO O CODIGO

serv = Server("Dimmipst","JOAO127657")
ataque = Ataque()
list_pin = [
    "123456",
    "password",
    "123456789",
    "qwerty",
    "admin123",
    "111111",
    "iloveyou",
    "JOAO127657",
    "sunshine",
    "12345678",
    "monkey",
    "welcome",
    "dragon",
    "p@ssword",
    "masterkey"
]
ataque.login(serv,list_pin)