import pygame
import Utils.JsonLoader as jsonL
def InsertBackground(background, screen):
    background = pygame.transform.scale(background, (screen.get_width(), screen.get_height()))
    screen.blit(background, (0,0))
#endFunction

def InsertImage(img, width, height, x,y, screen):
    img = pygame.transform.scale(img, (width, height))
    screen.blit(img, (x,y))
#endFunction

def InsertText(text, text_color, x, y, screen):
    fontName = jsonL.GetFont()
    textSize = jsonL.GetTextSize()
    font = pygame.font.SysFont(fontName, textSize)
    img = font.render(text, True, text_color)
    screen.blit(img, (x, y))
#endfunction
