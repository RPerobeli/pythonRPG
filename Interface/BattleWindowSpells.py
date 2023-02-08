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
        self.SpellsList = jsonL.GetSpells(self.Personagem.classe)
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


    def Battle(self):
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
                    return self.Personagem.magias['Key']
                #endif
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_2):
                    self.isOptions = False
                    atkType = 2
                    self.BattleText = self.Personagem.arma.textoAtkEspecial
                    dano = self.Personagem.acoes.Atk(self.Personagem,atkType,self.Monster,turnCounter)
                    self.PrintDmg(dano,self.Personagem)
                #endif
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_3):
                    if(self.isOptions):
                        self.isSelectingSpell = True
                        self.LoadUsableSpells() 
                #endif
            #endfor
            pygame.display.update()
        #endwhile
    #endFunction
#endclass