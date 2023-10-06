#encoding: utf-8
import pygame
import Interface.States.Inn as Inn
import Interface.DialogBox as DialogBox
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
#endwhile
pygame.quit()