import pygame
import Interface.Utils as ut
import Utils.JsonLoader as jsonL
import Interface.States.GameState as GameState
from Interface import BattleWindowSpells as bws
from Interface import BattleWindowMonsterTurn as bwmt
from Interface import BattleWindowLvlUp as bwlvl
from Interface import GameOverWindow as gow
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
        self.isSelectingSpell = False
        self.SpellsList = jsonL.GetSpells(self.Personagem.classe)
        self.SpellsWindow = bws.BattleWindowSpells(self.Screen, self.DialogBox, self.Personagem, self.Monster, bgName)
        self.MonsterTurnWindow = bwmt.BattleWindowMonsterTurn(self.Screen, self.DialogBox, self.Personagem, self.Monster, bgName)
        self.LvlUpWindow = bwlvl.BattleWindowLvlUp(self.Screen, self.DialogBox, self.Personagem, self.Monster, bgName)
        self.GameOverWindow = gow.GameOverWindow(self.Screen)
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

    def PrintDmg(self, dano, personagem, isCrit = None):
        if(personagem.acoes.isCrit or isCrit == True):
            self.BattleText = {"txt": f"ACERTO CRÍTICO!!!\n{personagem.name} causou {dano} de dano!\n"}
        else:
            self.BattleText = {"txt": f"{personagem.name} causou {dano} de dano!\n"}
        #endif
    #endfunc

    def VerifyIfBattleIsFinished(self):
        if(self.Personagem.HP <= 0):
            self.GameOverWindow.GameOver()
        elif(self.Monster.HP <= 0):
            self.Personagem = self.LvlUpWindow.LvlUp(self.Personagem)
            return True
        #endif
    #endfunc

    def VerifyMana(self, spell):
        if(self.Personagem.MP < spell["Cost"]):
            return True
        else:
            return False
        #endif
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
                    #confere se a luta acabou
                    isFinished = self.VerifyIfBattleIsFinished()
                    if(isFinished):
                        return self.Personagem
                    #endif

                    if(turnCounter == 2):
                        self.MonsterTurnWindow.MonsterTurn()
                        turnCounter -= 1
                        self.isOptions = True
                        self.VerifyIfBattleIsFinished()
                    #endif

                #endif
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_1):
                    if(self.isOptions):
                        self.isOptions = False
                        atkType = 1
                        dano = self.Personagem.acoes.Atk(self.Personagem,atkType,self.Monster)
                        self.PrintDmg(dano, self.Personagem)
                        turnCounter += 1
                    #endif
                #endif
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_2):
                    if(self.isOptions):
                        self.isOptions = False
                        atkType = 2
                        self.BattleText = self.Personagem.arma.textoAtkEspecial
                        dano = self.Personagem.acoes.Atk(self.Personagem,atkType,self.Monster)
                        self.PrintDmg(dano,self.Personagem)
                        turnCounter += 1
                    #endif
                #endif
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_3):
                    if(self.isOptions):
                        self.isSelectingSpell = True
                        atkType = 3
                        spell = self.SpellsWindow.SelectSpell()
                        if(self.VerifyMana(spell)== True):
                            self.BattleText = {"txt": "TA SEM MANA, OTARIO!\n"}
                        else:
                            dano = self.Personagem.acoes.Atk(self.Personagem,atkType,self.Monster, spell)
                            self.PrintDmg(dano,self.Personagem)
                        #endif
                        self.isOptions = False
                        turnCounter += 1
                    #endif  
                #endif
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_4):
                    if(self.isOptions):
                        atkType = 4
                        self.Personagem.acoes.Atk(self.Personagem,atkType,self.Monster, spell)
                        self.isOptions = False
                        self.BattleText = {"txt": f"{self.Personagem.name} regenerou vida e mana.\n"}
                        turnCounter += 1
                    #endif  
                #endif
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_9):
                    if(self.isOptions):
                        atkType = 69
                        dano = self.Personagem.acoes.Atk(self.Personagem,atkType,self.Monster)
                        self.PrintDmg(dano,self.Personagem)
                        turnCounter += 1
                    #endif  
                #endif
            #endfor
            pygame.display.update()
        #endwhile
    #endFunction
#endclass