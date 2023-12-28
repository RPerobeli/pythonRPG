import sys
import pygame
import Interface.InterfaceUtils as ut
import Utils.JsonLoader as jsonL
import Interface.States.GameState as GameState
import Interacoes as lib
class TheEndWindow(GameState.GameState):
    def __init__(self,screen):
        super().__init__(screen)
        self.Scene = 1
        self.Alpha = 255
        self.BattleText = {"txt": "FIM!"}
        self.BackgroundImage = pygame.Surface((self.Screen.get_width(), self.Screen.get_height()))
        self.BackgroundImage.fill((45,45,45))
        self.BackgroundImage.set_alpha(255)
    #endfunc


    def ScenesManager(self):
        if (self.Scene == 1):
            self.LoadEnd()
            self.Sound.PlayMusic("TheEnd")
        else:
            print("erro ao entrar nas Cenas")
        #endif
    #endfunc

    def LoadEnd(self):
        ut.InsertBackground(self.BackgroundImage, self.Screen)
        x = 400
        y = 250
        font = jsonL.GetTitleFont()
        textSize = 200
        textColor = (240,240,240)
        ut.InsertText("Fim!",textColor,x,y,self.Screen,font,textSize)
    #endfunc

    def End(self):
        pygame.display.set_caption("Fim")
        running = True
        while running:
            print("The End")
            self.ScenesManager()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                #endif
                # if (event.type == pygame.KEYDOWN and event.key == pygame.K_KP_ENTER or event.key == pygame.K_SPACE):
                #     pygame.quit()
                #     sys.exit()
                # #endif
            #endfor
            pygame.display.update()
        #endwhile
    #endFunction
#endclass