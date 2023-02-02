#encoding: utf-8
import pygame
from Interface import Inn
from Interface import DialogBox
import pygame
import sys
from Domain import Heroi as heroi
import Interacoes as lib
import HistoriasPyGame as hpg


pygame.init()

screen_width = 800
screen_height = 550
screen= pygame.display.set_mode((screen_width,screen_height))
dialogBox = DialogBox.DialogBox(screen)


###############INTRODUCAO ###############################################################################
classesDisponiveis = ("Guerreiro", "Arqueiro", "Mago")
print("Bem vindo ao D&D da Deepweb, aqui você vai encontrar diversas aventuras(nem todas vão ser divertidas).")
nome = input("Digite o nome do seu personagem: ")
print("Perfeito, "+nome+", agora escolha a classe com a qual voce vai se ferrar!")
print("As classes disponíveis são: " + str(classesDisponiveis) + ".")
classe = input("E então, qual será a sua?")
while(lib.ConfereClasses(classesDisponiveis, classe) == False):
    classe = input("Classe invalida, digite novamente:")

print("Beleza, então você se chama "+nome + " e é um "+classe+".")
Heroi = heroi.Heroi(nome, classe)
Heroi.arma.danoBase = 3
print("status de "+str(Heroi.name)+": " + str(Heroi.skills))

resp = input("Deseja iniciar sua jornada? (s/n)")
if(resp == "n"):
    sys.exit()
###############INICIO DA HISTORIA###############################################################################
lib.LimpaConsole()
# começa a contar a historia
hpg.HistoriaIntro(screen,dialogBox,Heroi)

pygame.quit()