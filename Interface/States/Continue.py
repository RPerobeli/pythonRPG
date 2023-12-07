import pygame
import sys
import random as rnd
import Interface.InterfaceUtils as ut
import Utils.JsonLoader as jsonL
import Interface.BattleWindow as bw
import Interacoes as lib
import Interface.States.GameState as GameState

class Continue(GameState.GameState):
    def __init__(self, screen):
        super().__init__(screen)
        self.ImagePath =  jsonL.GetImagePath()
        self.BackgroundImage = pygame.image.load(f'{self.ImagePath}/Background/ToBeContinued.png').convert_alpha()
        self.Alpha = 0
        self.Scene = 1
        self.Filename = "Continue"
        self.MaxStoryIndex = 3
        
    #endfunc
    


    def Update(self, namestate):
        #Cena tapa na cachorra
        ut.InsertBackground(self.BackgroundImage, self.Screen)
        self.Sound.PlayMusic("continue")
        pygame.display.set_caption("Continua")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #endif
            if (event.type == pygame.KEYDOWN and (event.key == pygame.K_KP_ENTER or event.key == pygame.K_SPACE)):
                pygame.quit()
                sys.exit()
            #endif
        #endfor
        pygame.display.update()
        return 'ToBeContinued'
    #endFunction

#endclass
