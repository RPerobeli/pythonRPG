import pygame
import Interface.InterfaceUtils as ut
import Utils.JsonLoader as jsonL
import Interface.States.GameState as GameState
import Interacoes as lib
import Interface.BattleWindowSpec as bwspec

import BagBox
class CaracterísticasWindow(GameState.GameState):
    def __init__(self,screen, dialogBox,personagem, monster, bgName):
        super().__init__(screen)
        imagePath =  jsonL.GetImagePath()
        self.DialogBox = dialogBox
        self.BackgroundImage = pygame.image.load(f'{imagePath}/Background/{bgName}.jpg').convert_alpha()
        self.BagBox = BagBox.BagBox(self.Screen)
        self.Actors[0] = personagem
        self.Personagem = personagem
        self.Monster = monster
        self.Actors[1] = monster
        self.Scene = 1
        self.Alpha = 255
        self.AlphaDisabled = 200
        self.BattleText = {}
        self.BGName = bgName
    #endfunc

    def ScenesManager(self):
        if (self.Scene == 1):
            actorPos = self.PlaceActors()
            self.LoadImagesWithAlpha(actorPos)
        elif(self.Scene == 2):
            actorPos = self.PlaceActors()
            self.LoadImages(actorPos)
            self.LoadTextWithList(self.BattleText)
        else:
            print("erro ao entrar nas Cenas -> inn.ScenesManager()")
        #endif
    #endfunc

    def LoadImagesWithAlpha(self, actorPos):
        ut.InsertBackground(self.BackgroundImage, self.Screen, alpha = self.AlphaDisabled)
        if(self.Actors[0] != None):
            ut.InsertImage(self.Actors[0].Image.File, self.Actors[0].Image.Width, self.Actors[0].Image.Height, actorPos['x0'],actorPos['y0'], self.Screen,alpha = self.AlphaDisabled)
        if(self.Actors[1] != None):
            ut.InsertImage(self.Actors[1].Image.File, self.Actors[1].Image.Width, self.Actors[1].Image.Height, actorPos['x1'],actorPos['y1'], self.Screen,alpha = self.AlphaDisabled)
        #endif
        ut.InsertImage(self.DialogBox.image,self.DialogBox.Width,self.DialogBox.Height, self.DialogBox.x, self.DialogBox.y, self.Screen, alpha = self.AlphaDisabled)
        ut.InsertImage(self.BagBox.image, self.DialogBox.Width,self.DialogBox.Height, self.DialogBox.x, self.DialogBox.y, self.Screen)
        #endif
    #endfunc

    def GetInfo(self, hero):
        self.Personagem = hero
        pygame.display.set_caption("Status")
        inBattle = True
        while inBattle:
            self.ScenesManager()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                     pygame.quit()
                #endif
                if (event.type == pygame.KEYDOWN and (event.key == pygame.K_KP_ENTER or event.key == pygame.K_SPACE)):
                    pass
            #endfor
            pygame.display.update()
        #endwhile
    #endFunction
#endClass