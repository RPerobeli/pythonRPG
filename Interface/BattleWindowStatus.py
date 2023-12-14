import pygame
#import Interface.Utils as ut
import Utils.JsonLoader as jsonL
import Interface.States.GameState as GameState
import Interacoes as lib
import Interface.BattleWindowSpec as bwspec
class BattleWindowStatus(GameState.GameState):
    def __init__(self,screen, dialogBox,personagem, monster, bgName):
        super().__init__(screen)
        imagePath =  jsonL.GetImagePath()
        self.DialogBox = dialogBox
        self.BackgroundImage = pygame.image.load(f'{imagePath}/Background/{bgName}.jpg').convert_alpha()
        self.Actors[0] = personagem
        self.Personagem = personagem
        self.Monster = monster
        self.Actors[1] = monster
        self.Scene = 1
        self.Alpha = 255
        self.BattleText = {}
        self.BGName = bgName
    #endfunc


    def ScenesManager(self):
        if (self.Scene == 1):
            actorPos = self.PlaceActors()
            self.LoadImages(actorPos)
            self.LoadLvlUpText()
        elif(self.Scene == 2):
            actorPos = self.PlaceActors()
            self.LoadImages(actorPos)
            self.LoadTextWithList(self.BattleText)
        else:
            print("erro ao entrar nas Cenas -> inn.ScenesManager()")
        #endif
    #endfunc

    def LoadLvlUpText(self):
        self.OptionsDict = jsonL.GetOptions()
        self.CapinadoDict = {"txt": f"O {self.Monster.name} foi capinado.\n"}
        self.LoadTextWithList(self.CapinadoDict)
        self.LoadTextWithList({"txt":f"Você chegou ao NIVEL {self.Personagem.lvl}!\n"}, (self.OptionsDict["Options"]["PositionStatus1"]["x"]),self.OptionsDict["Options"]["PositionStatus1"]["y"])
        self.LoadTextWithList({"txt": "Consuma seu ponto de habilidade\n1 - Força\n2 - Agilidade\n3 - Inteligência\n4 - Vitalidade\n5 - Sabedoria\n"}, \
            self.OptionsDict["Options"]["PositionOptions"]["x"],self.OptionsDict["Options"]["PositionOptions"]["y"])
    #endfunc



    def StatusApplied(self, hero):
        self.Personagem = hero
        pygame.display.set_caption("statuses")
        inBattle = True
        while inBattle:
            self.ScenesManager()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                     pygame.quit()
                #endif
                if (event.type == pygame.KEYDOWN and (event.key == pygame.K_KP_ENTER or event.key == pygame.K_SPACE)):
                    print("proximo status")
                #endif
            #endfor
            pygame.display.update()
        #endwhile
    #endFunction
#endclass