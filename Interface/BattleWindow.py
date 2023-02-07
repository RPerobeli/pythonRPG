import pygame
import Interface.Utils as ut
import Utils.JsonLoader as jsonL
import Interface.States.GameState as GameState
import Interacoes as lib
class BattleWindow(GameState.GameState):
    def __init__(self,screen, dialogBox,personagem, monster, bgName):
        super().__init__(screen)
        imagePath =  jsonL.GetImagePath()
        self.DialogBox = dialogBox
        self.BackgroundImage = pygame.image.load(f'{imagePath}/Background/{bgName}.jpg').convert_alpha()
        self.Actors.append(personagem)
        self.Personagem = personagem
        self.Monster = monster
        self.Actors.append(monster)
        self.Scene = 1
        self.Alpha = 255
        self.BattleText = {}
        self.isOptions = True
    #endfunc


    def ScenesManager(self):
        if (self.Scene == 1):
            actorPos = self.PlaceActors()
            self.LoadImages(actorPos)
            if(self.isOptions):
                self.LoadBattleOptions()
            else:
                self.LoadTextWithList(self.BattleText)
            #endif
        elif(self.Scene == 2):
            print("Lanchado, se fodeu.")
            print("criar a tela de game over")
        else:
            print("erro ao entrar nas Cenas -> inn.ScenesManager()")
        #endif
    #endfunc

    def LoadBattleOptions(self):
        self.OptionsDict = jsonL.GetOptions()
        self.HealthDict = {"txt": f"{self.Personagem.name}.HP: {self.Personagem.HP}/{self.Personagem.HPmax}       {self.Monster.name}.HP:  {self.Monster.HP}/{self.Monster.HPmax}\n{self.Personagem.name}.MP: {self.Personagem.MP}/{self.Personagem.MPmax}       {self.Monster.name}.MP:  {self.Monster.MP}/{self.Monster.MPmax}\n"}
        self.StatusDict = {"txt": f"Força:        {self.Personagem.skills['str']}\nAgilidade:    {self.Personagem.skills['agi']}\nVitalidade:   {self.Personagem.skills['vit']}\nInteligência: {self.Personagem.skills['int']}\n"}
        self.LoadTextWithList(self.HealthDict)
        self.LoadTextWithList(self.StatusDict, self.OptionsDict["Options"]["PositionStatus"]["x"],self.OptionsDict["Options"]["PositionStatus"]["y"])
        self.LoadTextWithList(self.OptionsDict["Options"]["OptionsText"], self.OptionsDict["Options"]["PositionOptions"]["x"],self.OptionsDict["Options"]["PositionOptions"]["y"])
    #endfunc

    def Battle(self):
        self.Monster.AutoLvl(self.Personagem.lvl)
        self.Monster.AdequaHP()
        turnCounter = 1
        pygame.display.set_caption("Batalha")
        inBattle = True
        while inBattle:
            print("in battle")
            self.ScenesManager()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                #endif
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_KP_ENTER):
                    if(turnCounter == 1):
                        turnCounter += 1
                        self.isOptions = True
                    #endif
                #endif
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_1):
                    self.isOptions = False
                #endif
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_2):

                #endif
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_3):

                #endif
            #endfor
            if(self.Personagem.HP <= 0):
                self.Scene = 2
            elif(self.Monster.HP <= 0):
                print(f"O {self.Monster.name} foi capinado.")
                self.Personagem.XP += lib.XP(self.Monster.lvl)
                if(self.Personagem.XP >= 100):
                    self.Personagem.LvlUP()
                else:
                    print("XP: " + str(self.Personagem.XP)+'/' + str(100))
                #endif
            #endif
            pygame.display.update()
        #endwhile
    #endFunction
#endclass