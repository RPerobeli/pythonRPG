import pygame
import Interface.Utils as ut
import Utils.JsonLoader as jsonL
import Interface.States.GameState as GameState
class BattleWindow(GameState.GameState):
    def __init__(self,screen, dialogBox,personagem, monstro, bgName):
        super().__init__(screen)
        imagePath =  jsonL.GetImagePath()
        self.DialogBox = dialogBox
        self.BackgroundImage = pygame.image.load(f'{imagePath}/Background/{bgName}.jpg').convert_alpha()
        self.Actors.append(personagem)
        self.Actors.append(monstro)
        self.Scene = 1
        self.Alpha = 255
        self.BattleText = {}
    #endfunc


    def ScenesManager(self):
        if (self.Scene == 1):
            actorPos = self.PlaceActors()
            self.LoadImages(actorPos)
            self.LoadTextWithList()
        else:
            print("erro ao entrar nas Cenas -> inn.ScenesManager()")
        #endif
    #endfunc


    def Battle(self):
        pygame.display.set_caption("Batalha")
        inBattle = True
        while inBattle:
            print("in battle")
            self.ScenesManager()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                #endif
            #endfor
            pygame.display.update()
        #endwhile
    #endFunction
#endclass