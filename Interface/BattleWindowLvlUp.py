import pygame
import Interface.Utils as ut
import Utils.JsonLoader as jsonL
import Interface.States.GameState as GameState
import Interacoes as lib
class BattleWindowLvlUp(GameState.GameState):
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
        self.LoadTextWithList({"txt":f"Você chegou ao NIVEL {self.Personagem.lvl}!\n"}, self.OptionsDict["Options"]["PositionStatus"]["x"],self.OptionsDict["Options"]["PositionStatus"]["y"])
        self.LoadTextWithList({"txt": "Consuma seu ponto de habilidade\n1 - Força\n2 - Agilidade\n3 - Inteligência\n4 - Vitalidade\n"}, \
            self.OptionsDict["Options"]["PositionOptions"]["x"],self.OptionsDict["Options"]["PositionOptions"]["y"])
    #endfunc


    def PrintDmg(self, dano, personagem):
        if(personagem.acoes.isCrit):
            self.BattleText = {"txt": f"ACERTO CRÍTICO!!!\n{personagem.name} causou {dano} de dano!\n"}
        else:
            self.BattleText = {"txt": f"{personagem.name} causou {dano} de dano!\n"}
        #endif
    #endfunc
    
    def LvlUpPersonagem(self):
        self.Personagem.XP += lib.XP(self.Monster.lvl)
        if(self.Personagem.XP >= 100):
            self.Personagem.lvl += 1
            self.Personagem.XP -= 100
            self.Scene = 1
            self.Upou = True
        else:
            self.BattleText = {"txt": f"O {self.Monster.name} foi capinado.\nXP: {round(self.Personagem.XP,2)}/100\n"}
            self.Upou = False
            self.Scene = 2
        #endif
    #endfunc
    def LvlUp(self, hero):
        self.Personagem = hero
        self.LvlUpPersonagem()
        pygame.display.set_caption("Xp")
        inBattle = True
        while inBattle:
            print("Lvl up")
            self.ScenesManager()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                     pygame.quit()
                #endif
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_KP_ENTER):
                    if(not self.Upou):
                        return self.Personagem
                    #endif
                #endif
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_1):
                    self.Personagem.skills["str"] += 1
                    self.Personagem.AtualizaStatus()
                    return self.Personagem
                #endif
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_2):
                    self.Personagem.skills["agi"] += 1
                    self.Personagem.AtualizaStatus()
                    return self.Personagem
                #endif
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_3):
                    self.Personagem.skills["int"] += 1
                    self.Personagem.AtualizaStatus()
                    return self.Personagem
                #endif
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_4):
                    self.Personagem.skills["vit"] += 1
                    self.Personagem.AtualizaStatus()
                    return self.Personagem
                #endif
            #endfor
            pygame.display.update()
        #endwhile
    #endFunction
#endclass