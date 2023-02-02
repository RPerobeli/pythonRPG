import pygame

def InsertBackground(background, screen):
    background = pygame.transform.scale(background, (screen.get_width(), screen.get_height()))
    screen.blit(background, (0,0))
#endFunction

def InsertImage(img, width, height, x,y, screen):
    img = pygame.transform.scale(img, (width, height))
    screen.blit(img, (x,y))
#endFunction
