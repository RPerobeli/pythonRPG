
import pygame
import Utils.JsonLoader as jsonL

class BagBox:
    def __init__(self, screen):
        self.Width = screen.get_width()
        self.Height = 300
        self.alpha = 255
        self.LoadImage()
        self.x= 0
        self.y = screen.get_height()-self.Height
    #endfunc

    def LoadImage(self):
        imagePath = jsonL.GetImagePath()
        self.image  = pygame.image.load(f'{imagePath}/Icones/BagBox.jpg').convert_alpha()
        self.image.set_alpha(self.alpha)
    #endfunc
#endclass