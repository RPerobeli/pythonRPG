import Utils.JsonLoader as jsonL
import Interacoes as lib
import Interface.Utils as ut
import pygame

pygame.init()
screen_width = 1080
screen_height = 650
screen= pygame.display.set_mode((screen_width,screen_height))
Monstros = lib.CriaMonstros()
print(Monstros[1])

pygame.quit()