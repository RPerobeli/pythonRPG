
import pygame
import Interface.DialogBox as DialogBox
import GameStateHandler as gsh
import Utils.JsonLoader as jsonL

pygame.init()

SCREEN_WIDTH = 1080 
SCREEN_HEIGHT = 650
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
dialogBox = DialogBox.DialogBox(screen)
FrameRate = jsonL.GetFrameRate()
Clock = pygame.time.Clock()

run = True
gameStateHandler = gsh.GameStateHandler(screen)
while run:
    pos = jsonL.GetNameTextPosition()
    gameStateHandler.ManageState()
    Clock.tick(FrameRate)
pygame.quit()