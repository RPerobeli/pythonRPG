import sys
import pygame
import Interface.InterfaceUtils as ut
import Utils.JsonLoader as jsonL
import Interface.States.GameState as GameState
import Interacoes as lib
class GameOverWindow(GameState.GameState):
    def __init__(self,screen):
        super().__init__(screen)
        self.Scene = 1
        self.Alpha = 255
        self.BattleText = {"txt": "LANCHADO!\nSE FODEU\n"}
        self.BackgroundImage = pygame.Surface((self.Screen.get_width(), self.Screen.get_height()))
        self.BackgroundImage.fill((45,45,45))
        self.BackgroundImage.set_alpha(255)
    #endfunc


    def ScenesManager(self):
        if (self.Scene == 1):
            self.LoadGameOver()
            self.Sound.PlayMusic("gameover")
        else:
            print("erro ao entrar nas Cenas")
        #endif
    #endfunc

    def LoadGameOver(self):
        ut.InsertBackground(self.BackgroundImage, self.Screen)
        x = 300
        y = 125
        font = jsonL.GetTitleFont()
        textSize = 100
        textColor = (255,0,0)
        ut.InsertText("LANCHADO!!",textColor,x,y,self.Screen,font,textSize)
        x = 400
        y = 300
        textSize = 70
        ut.InsertText("SE FODEU!!",textColor,x,y,self.Screen,font,textSize)
    #endfunc

    def GameOver(self):
        pygame.display.set_caption("Game Over")
        running = True
        while running:
            print("Game Over")
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