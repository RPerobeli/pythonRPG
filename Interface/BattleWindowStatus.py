import pygame
#import Interface.Utils as ut
import Utils.JsonLoader as jsonL
import Interface.States.GameState as GameState
import Interacoes as lib
import random as rnd
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
            self.LoadTextWithList(self.BattleText)
        elif(self.Scene == 2):
            actorPos = self.PlaceActors()
            self.LoadImages(actorPos)
            self.LoadTextWithList(self.BattleText)
        else:
            print("erro ao entrar nas Cenas -> inn.ScenesManager()")
        #endif
    #endfunc

    def RemoveStatusInList(self, status :dict, listStatus :list):
        listaAux = list( filter(lambda x: x["TurnsToEnd"] > 0, listStatus) ) 
        return listaAux
    #endfunc

    def ApplyStatusEffects(self, personagem):
        self.BattleText = {"txt":""}
        personagem.canAct = True
        for status in personagem.Status :
                #Debuffs no inimigo
                if(status["Name"] == "Burning"):
                    if(status["TurnsToEnd"] > 0):
                        personagem.HP -= status["DamagePerTurn"]
                        status["TurnsToEnd"] -= 1
                        self.BattleText["txt"] += f"{personagem.name} sofreu {status['DamagePerTurn']} de dano devido às queimaduras.\n"
                    else:
                        personagem.Status = self.RemoveStatusInList(status, personagem.Status)
                        self.BattleText["txt"] += f"{personagem.name} não está mais queimando.\n"
                if(status["Name"] == "Paralyse"):
                    if(status["TurnsToEnd"] >= 0):
                        if(rnd.random() < status["Chance"]):
                            self.BattleText["txt"] += f"{personagem.name} está paralisado.\n"
                            status["TurnsToEnd"] -= 1
                            personagem.canAct = False
                        else:
                            self.BattleText["txt"] += f"{personagem.name} força para se mexer.\n"
                        #endif
                    else:
                        personagem.Status = self.RemoveStatusInList(status, personagem.Status)
                        self.BattleText["txt"] += f"{personagem.name} não está mais paralisado.\n"
                    #endif
                if(status["Name"] == "Sleep"):
                    if(status["TurnsToEnd"] > 0):
                        self.BattleText["txt"] += f"{personagem.name} está dormindo.\n"
                        status["TurnsToEnd"] -= 1
                        personagem.canAct = False
                    else:
                        personagem.Status = self.RemoveStatusInList(status, personagem.Status)
                        self.BattleText["txt"] += f"{personagem.name} acordou.\n"
                if(status["Name"] == "Stun"):
                    if(status["TurnsToEnd"] > 0):
                        self.BattleText["txt"] += f"{personagem.name} está atordoado.\n"
                        status["TurnsToEnd"] -= 1
                        personagem.canAct = False
                    else:
                        personagem.Status = self.RemoveStatusInList(status, personagem.Status)
                        self.BattleText["txt"] += f"{personagem.name} não está mais atordoado.\n"
                if(status["Name"] == "Poison"):
                    if(status["TurnsToEnd"] > 0):
                        personagem.HP -= {status['DamagePerTurn']}
                        status["TurnsToEnd"] -= 1
                        self.BattleText["txt"] += f"{personagem.name} sofreu {status['DamagePerTurn']} de dano devido ao veneno.\n"
                    else:
                        personagem.Status = self.RemoveStatusInList(status, personagem.Status)
                        self.BattleText["txt"] += f"{personagem.name} não está mais envenenado.\n"
                    #endif
                #Buffs no self.Personagem
                if(status["Name"] == "Enrage"):
                    if(status["TurnsToEnd"] > 0):
                        personagem.BuffDano = status["DamageBuff"]
                        status["TurnsToEnd"] -= 1
                        self.BattleText["txt"] += f"{self.Personagem.name} está enraivecido.\n"
                    else:
                        personagem.Status = self.RemoveStatusInList(status, personagem.Status)
                        personagem.BuffDano = 1
                        self.BattleText["txt"] += f"{self.Personagem.name} se acalmou.\n"
                    #endif
                if(status["Name"] == "Regeneration"):
                    if(status["TurnsToEnd"] > 0):
                        personagem.HP += status["HealPerTurn"]
                        status["TurnsToEnd"] -= 1
                        self.BattleText["txt"] += f"{self.Personagem.name} recuperou {status['HealPerTurn']} de vida.\n"
                    else:
                        personagem.Status = self.RemoveStatusInList(status, personagem.Status)
                        self.BattleText["txt"] += f"{self.Personagem.name} não está mais regenerando.\n"
                    #endif
                if(status["Name"] == "Berserk"):
                    if(status["TurnsToEnd"] > 0):
                        personagem.BuffDano = status["DamageBuff"]
                        status["TurnsToEnd"] -= 1
                        self.BattleText["txt"] += f"{self.Personagem.name} está enraivecido.\n"
                    else:
                        personagem.Status = self.RemoveStatusInList(status, personagem.Status)
                        personagem.BuffDano = 1
                        self.BattleText["txt"] += f"{self.Personagem.name} se acalmou.\n"
                    #endif
                if(status["Name"] == "Protection"):
                    if(status["TurnsToEnd"] > 0):
                        personagem.BuffBarreira = status["DamageBuff"]
                        status["TurnsToEnd"] -= 1
                        self.BattleText["txt"] += f"{self.Personagem.name} terá dano reduzido.\n"
                    else:
                        personagem.Status = self.RemoveStatusInList(status, personagem.Status)
                        personagem.BuffBarreira = 1
                        self.BattleText["txt"] += f"{self.Personagem.name} a proteção acabou.\n"
                    #endif
                #endif
            #endif
        #endif
    #endfunc

    def StatusApplied(self, character):
        pygame.display.set_caption("status")
        inBattle = True
        self.ApplyStatusEffects(character)
        while inBattle:
            self.ScenesManager()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                     pygame.quit()
                #endif
                if (event.type == pygame.KEYDOWN and (event.key == pygame.K_KP_ENTER or event.key == pygame.K_SPACE)):
                        return
                #endif
            #endfor
            pygame.display.update()
        #endwhile
    #endFunction
#endclass