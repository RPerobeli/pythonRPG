import pygame
#import Interface.Utils as ut
import Utils.JsonLoader as jsonL
import Interface.States.GameState as GameState
import Interacoes as lib
class BattleWindowMonsterTurn(GameState.GameState):
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
        self.SpellsList = jsonL.GetSpells(self.Personagem.classe)
    #endfunc


    def ScenesManager(self):
        if (self.Scene == 1):
            actorPos = self.PlaceActors()
            self.LoadImages(actorPos)
            self.LoadMonsterTurnOptions()
        elif(self.Scene == 2):
            actorPos = self.PlaceActors()
            self.LoadImages(actorPos)
            self.LoadTextWithList(self.BattleText)
        else:
            print("erro ao entrar nas Cenas -> inn.ScenesManager()")
        #endif
    #endfunc

    def LoadMonsterTurnOptions(self):
        self.OptionsDict = jsonL.GetOptions()
        self.CharHealthDict = {"txt": f"{self.Personagem.name}.HP: {self.Personagem.HP}/{self.Personagem.HPmax}\n{self.Personagem.name}.MP: {self.Personagem.MP}/{self.Personagem.MPmax}\n{self.Personagem.name}.SP: {self.Personagem.SP}/{self.Personagem.SPmax}\n"}
        self.MonsterHealthDict = {"txt": f"{self.Monster.name}.HP:  {self.Monster.HP}/{self.Monster.HPmax}\n{self.Monster.name}.MP:  {self.Monster.MP}/{self.Monster.MPmax}\n"}
        self.LoadTextWithList(self.MonsterHealthDict,self.OptionsDict["Options"]["PositionHealthBarsMonster"]["x"],self.OptionsDict["Options"]["PositionHealthBarsMonster"]["y"])
        self.LoadTextWithList(self.CharHealthDict)
        self.LoadTextWithList({"txt":"Vez do monstro atacar, segura na mão de Eru e vai!\n"}, self.OptionsDict["Options"]["PositionStatus1"]["x"],self.OptionsDict["Options"]["PositionStatus1"]["y"])
    #endfunc


    def PrintDmg(self, dano, personagem):
        if(personagem.acoes.isCrit):
            self.BattleText = {"txt": f"ACERTO CRÍTICO!!!\n{personagem.name} causou {dano} de dano!\n"}
        else:
            self.BattleText = {"txt": f"{personagem.name} causou {dano} de dano!\n"}
        #endif
    #endfunc
    
    def MonsterTurn(self):
        pygame.display.set_caption("Turno do Monstro")
        inBattle = True
        while inBattle:
            print("monster turn")
            self.ScenesManager()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                     pygame.quit()
                #endif
                if (event.type == pygame.KEYDOWN and (event.key == pygame.K_KP_ENTER or event.key == pygame.K_SPACE)):
                    if(self.Scene == 2):
                        self.Scene = 1
                        return
                    #endIf
                    atkType = self.Monster.acoes.TipoAtk(self.Monster)
                    if(atkType == 4):
                        self.Monster.acoes.Atk(self.Monster,atkType,self.Personagem)
                        self.BattleText = {"txt":"Regenerou vida e mana\n"}
                        self.Scene = 2
                    elif(atkType == 3):
                        spell = self.Monster.acoes.SelectMonsterSpell(self.Monster)
                        dano = self.Monster.acoes.Atk(self.Monster,atkType,self.Personagem,spell)
                        self.PrintDmg(dano, self.Monster)
                        self.Scene = 2
                    else:
                        dano = self.Monster.acoes.Atk(self.Monster,atkType,self.Personagem)
                        self.PrintDmg(dano, self.Monster)
                        self.Scene = 2
                    #endif
                #endif
            #endfor
            pygame.display.update()
        #endwhile
    #endFunction
#endclass