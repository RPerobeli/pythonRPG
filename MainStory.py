#encoding: utf-8
import sys
from Domain import Personagem as bnc
import Interacoes as lib
import Historias as h

###############INTRODUCAO ###############################################################################
classesDisponiveis = ("Guerreiro", "Arqueiro", "Mago")
print("Bem vindo ao D&D da Deepweb, aqui você vai encontrar diversas aventuras(nem todas vão ser divertidas).")
nome = input("Digite o nome do seu personagem: ")
print("Perfeito, "+nome+", agora escolha a classe com a qual voce vai se ferrar!")
print("As classes disponíveis são: "+ str(classesDisponiveis) + ".")
classe = input("E então, qual será a sua?")
while(lib.ConfereClasses(classesDisponiveis, classe)==False):
    classe = input("Classe invalida, digite novamente:")

print("Beleza, então você se chama "+nome+ " e é um "+classe+".")
Heroi = bnc.Personagem(nome, classe)
print("status de "+str(Heroi.name)+": "+ str(Heroi.skills))

resp = input("Deseja iniciar sua jornada? (s/n)")
if(resp == "n"):
    sys.exit()
###############INICIO DA HISTORIA###############################################################################
for i in range(0,20):
    print(".")

#começa a contar a historia
h.Intro(Heroi)