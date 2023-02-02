


import pygame
import Utils.JsonLoader as jsonL

class DialogBox:
    def __init__(self, screen):
        self.Width = screen.get_width()
        self.Height = 150
        self.alpha = 128
        self.image = None
        self.x= 0
        self.y = screen.get_height()-self.Height
    #endfunc

    def LoadImage(self):
        imagePath = jsonL.GetImagePath()
        self.image  = pygame.image.load(f'{imagePath}/Icones/DialogBox.png').convert_alpha()
        self.image.set_alpha(self.alpha)
    #endfunc
#endclass