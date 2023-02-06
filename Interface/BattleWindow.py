import pygame
import Interface.InterfaceUtils as ut
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
        ut.InsertImage(self.Actors[0].Image.File, self.Actors[0].Image.Width, self.Actors[0].Image.Height, 0,100, self.Screen)
        ut.InsertImage(self.Actors[1].Image.File, self.Actors[1].Image.Width, self.Actors[1].Image.Height, 400,100, self.Screen)
        ut.InsertImage(self.DialogBox.image,self.DialogBox.Width,self.DialogBox.Height, self.DialogBox.x, self.DialogBox.y, self.Screen)
    #endfunc

    def Battle(self):
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

    def SetActors(self, actor1, actor2):
        self.Actors.append(actor1)
        actor2.Image.File = pygame.transform.flip(actor2.Image.File, True, False)
        self.Actors.append(actor2)
    #endfunc
#endclass