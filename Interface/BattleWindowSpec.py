import pygame
#import Interface.Utils as ut
import Utils.JsonLoader as jsonL
import Interface.States.GameState as GameState
import Interacoes as lib
class BattleWindowSpec(GameState.GameState):
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
    #endfunc


    def ScenesManager(self):
        if (self.Scene == 1):
            actorPos = self.PlaceActors()
            self.LoadImages(actorPos)
            self.LoadChooseSpecText()
        elif(self.Scene == 2):
            actorPos = self.PlaceActors()
            self.LoadImages(actorPos)
            self.LoadTextWithList(self.BattleText)
        else:
            print("erro ao entrar nas Cenas -> inn.ScenesManager()")
        #endif
    #endfunc

    def LoadChooseSpecText(self):
        self.OptionsDict = jsonL.GetOptions()
        self.LoadTextWithList({"txt": f"Escolha uma especialização para sua classe:\n"})
        self.LoadTextWithList({"txt":f"Escolha uma especialização para sua classe:\n"}, (self.OptionsDict["Options"]["PositionStatus1"]["x"]),self.OptionsDict["Options"]["PositionStatus1"]["y"])
        self.SpecOptionsList = jsonL.GetSpecializationOptions(self.Personagem.classe)
        self.LoadTextWithList({"txt": f"Especializações:\n1 - {self.SpecOptionsList[0]}\n2 - {self.SpecOptionsList[1]}\n3 - {self.SpecOptionsList[2]}\n"}, \
            self.OptionsDict["Options"]["PositionOptions"]["x"],self.OptionsDict["Options"]["PositionOptions"]["y"])
    #endfunc


    def PrintDmg(self, dano, personagem):
        if(personagem.acoes.isCrit):
            self.BattleText = {"txt": f"ACERTO CRÍTICO!!!\n{personagem.name} causou {dano} de dano!\n"}
        else:
            self.BattleText = {"txt": f"{personagem.name} causou {dano} de dano!\n"}
        #endif
    #endfunc
    

    def ChooseSpecialization(self, hero):
        self.Personagem = hero
        pygame.display.set_caption("Spec")
        inBattle = True
        while inBattle:
            print("Choosing Spec")
            self.ScenesManager()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                     pygame.quit()
                #endif
                if (event.type == pygame.KEYDOWN and (event.key == pygame.K_KP_ENTER or event.key == pygame.K_SPACE)):
                    self.Sound.PlaySFX("cursorError")
                #endif
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_1):
                    self.Personagem.Subclass = self.SpecOptionsList[0]
                    self.Personagem.UpdateHeroImage()
                    self.magias = jsonL.GetSpells(self.Personagem.Subclass.lower())
                    return self.Personagem
                #endif
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_2):
                    self.Personagem.Subclass = self.SpecOptionsList[1]
                    self.magias = jsonL.GetSpells(self.Personagem.Subclass.lower())
                    self.Personagem.UpdateHeroImage()
                    return self.Personagem
                #endif
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_3):
                    self.Personagem.Subclass = self.SpecOptionsList[2]
                    self.magias = jsonL.GetSpells(self.Personagem.Subclass.lower())
                    self.Personagem.UpdateHeroImage()
                    return self.Personagem
                #endif
            #endfor
            pygame.display.update()
        #endwhile
    #endFunction
#endclass