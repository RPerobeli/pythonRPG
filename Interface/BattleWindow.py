import pygame
import Interface.Utils as ut
import Utils.JsonLoader as jsonL

class BattleWindow:
    def __init__(self, screen, dialogBox, actors, bgName):
        imagePath =  jsonL.GetImagePath()
        self.BackgroundImage = pygame.image.load(f'{imagePath}/Background/{bgName}.jpg').convert_alpha()
        self.DialogBox = dialogBox
        self.Screen = screen
        self.FrameRate = jsonL.GetFrameRate()
        self.Clock = pygame.time.Clock()
        self.Actors = actors
    #endfunc

    def LoadImages(self):
        ut.InsertBackground(self.BackgroundImage, self.Screen)
        ut.InsertImage(self.Actors.Image, self.Actors.Image.Width, self.Actors.Image.Height, 0,100, self.Screen)
        #ut.InsertImage(self.Actors.Image, 300, 450, 0,100, self.Screen)
        ut.InsertImage(self.DialogBox.image,self.DialogBox.Width,self.DialogBox.Height, self.DialogBox.x, self.DialogBox.y, self.Screen)
    #endfunc

    def InnDialog1(self):
        #Cena tapa na cachorra
        pygame.display.set_caption("Hospedagem")
        run = True
        while run:
            self.Clock.tick(self.FrameRate)
            self.LoadImages()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                #endif
            #endfor
            pygame.display.update()
        #endwhile
    #endFunction

#endclass