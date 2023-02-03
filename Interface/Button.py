import pygame
import Utils.JsonLoader as jsonL


class Button:
    def __init__(self, id,filename, screen):
        self.Screen  = screen
        self.Boundary = jsonL.GetButton(id)
        imagePath = jsonL.GetImagePath()
        self.Button = pygame.Rect(self.Boundary['x'],self.Boundary['y'],self.Boundary['width'],self.Boundary['height'])
        self.Image = pygame.image.load(f'{imagePath}/Icones/{str(filename)}.png').convert_alpha()
        self.BoundaryColor = (20,20,20)
        self.BoundaryThickness = jsonL.GetBoundaryThickness()
    #endfunc

    def Draw(self):
        pygame.draw.rect(self.Screen,self.BoundaryColor, self.Button, self.BoundaryThickness)
        self.Image = pygame.transform.scale(self.Image, (self.Boundary['width']-10, self.Boundary['height']-10))
        self.Screen.blit(self.Image, (self.Boundary['x']+5,self.Boundary['y']+5))
    #endfunc
#endclass