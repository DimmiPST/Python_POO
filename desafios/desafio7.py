from rich import print,inspect
from classe_escola import *


fessor = Professor("Mestrado","Graduado","OCACIR ASSIR MACHADO",45)
aluno = Aluno("INFORMATICA","HAMILTON","GABRIEL",15)
aluno.aniver()
aluno.matricula()
fessor.aniver()
fessor.aula()
inspect(fessor)
inspect(aluno,methods=True)

