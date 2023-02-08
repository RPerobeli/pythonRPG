#encoding: utf-8
import pygame
from Interface.States import Inn
from Interface import DialogBox
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