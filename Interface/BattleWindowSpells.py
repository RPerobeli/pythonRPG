import pygame
#import Interface.Utils as ut
import Utils.JsonLoader as jsonL
import Interface.States.GameState as GameState
import Interacoes as lib
class BattleWindowSpells(GameState.GameState):
    def __init__(self,screen, dialogBox,personagem, monster, bgName):
        super().__init__(screen)
        imagePath =  jsonL.GetImagePath()
        self.DialogBox = dialogBox
        self.BackgroundImage = pygame.image.load(f'{imagePath}/Background/{bgName}.jpg').convert_alpha()
        self.Actors[1] = personagem
        self.Personagem = personagem
        self.Monster = monster
        self.Actors[1] = monster
        self.Scene = 1
        self.Alpha = 255
        self.BattleText = {}
        if(self.Personagem.Subclass != None):
            self.SpellsList = jsonL.GetSpells(self.Personagem.Subclass)
        else:
            self.SpellsList = jsonL.GetSpells(self.Personagem.classe)
        #endif
    #endfunc


    def ScenesManager(self):
        if (self.Scene == 1):
            actorPos = self.PlaceActors()
            self.LoadImages(actorPos)
            self.LoadUsableSpells()
        else:
            print("erro ao entrar nas Cenas -> inn.ScenesManager()")
        #endif
    #endfunc

    def LoadUsableSpells(self):
        vspace  = jsonL.GetVerticalSpace()
        x,y = jsonL.GetSpeakerTextPosition()
        for spell in self.SpellsList:
            if spell["Lvl"] <= self.Personagem.lvl:
                self.LoadText(f"{spell['Key']}: {spell['Nome']} - {spell['Cost']}MP", x, y)
                y += vspace
            #endif
        #endfor
    #endfunc

    def GetSpellByUserInput(self,input):
        for spell in self.Personagem.magias :
            if spell["Key"] == input:
                return spell
            #endif
        #endfor
    #endfunc

    def SelectSpell(self):
        pygame.display.set_caption("Selecao de Magias")
        inBattle = True
        while inBattle:
            print("in spell selection")
            self.ScenesManager()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    inBattle = False
                #endif
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_1):
                    input = 1
                    return self.GetSpellByUserInput(input)
                #endif
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_2):
                    input = 2
                    return self.GetSpellByUserInput(input)
                #endif
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_3):
                    input = 3
                    return self.GetSpellByUserInput(input)
                #endif
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_4):
                    input = 4
                    return self.GetSpellByUserInput(input)
                #endif
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_5):
                    input = 5
                    return self.GetSpellByUserInput(input)
                #endif
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_6):
                    input = 6
                    return self.GetSpellByUserInput(input)
                #endif
            #endfor
            pygame.display.update()
        #endwhile
    #endFunction
#endclass