#encoding: utf-8
import pygame
from Interface.States import Inn
from Interface import DialogBox
import pygame
import sys
from Domain import Heroi as heroi
import Interacoes as lib
import GameStateHandler as gsh
import Utils.JsonLoader as jsonL

pygame.init()

screen_width = 1080
screen_height = 650
screen= pygame.display.set_mode((screen_width,screen_height))
dialogBox = DialogBox.DialogBox(screen)
FrameRate = jsonL.GetFrameRate()
Clock = pygame.time.Clock()

# ###############INTRODUCAO ###############################################################################
# classesDisponiveis = ("Guerreiro", "Arqueiro", "Mago")
# print("Bem vindo ao D&D da Deepweb, aqui você vai encontrar diversas aventuras(nem todas vão ser divertidas).")
# nome = input("Digite o nome do seu personagem: ")
# print("Perfeito, "+nome+", agora escolha a classe com a qual voce vai se ferrar!")
# print("As classes disponíveis são: " + str(classesDisponiveis) + ".")
# classe = input("E então, qual será a sua?")
# while(lib.ConfereClasses(classesDisponiveis, classe) == False):
#     classe = input("Classe invalida, digite novamente:")

# print("Beleza, então você se chama "+nome + " e é um "+classe+".")
# Heroi = heroi.Heroi(nome, classe)
# Heroi.arma.danoBase = 3
# print("status de "+str(Heroi.name)+": " + str(Heroi.skills))

# resp = input("Deseja iniciar sua jornada? (s/n)")
# if(resp == "n"):
#     sys.exit()
# ###############INICIO DA HISTORIA###############################################################################
# lib.LimpaConsole()

run = True
gameStateHandler = gsh.GameStateHandler(screen)
while run:
    pos = jsonL.GetNameTextPosition()
    gameStateHandler.ManageState()
    Clock.tick(FrameRate)
    pygame.display.update()
#endwhile
#gsh.Title(screen)
# começa a contar a historia
#gsh.HistoriaIntro(screen,dialogBox,Heroi)
pygame.quit()