import pygame
import sys

#import Interface.Utils as ut
from Utils.ConstText import StatesText as txt
import Utils.JsonLoader as jsonL
import Interface.BattleWindow as bw
import Interacoes as lib
import Interface.States.GameState as GameState

class ViagemTeofilotoni(GameState.GameState):
    def __init__(self, screen, dialogBox, personagem, monstros, npcs = None):
        super().__init__(screen)
        self.ImagePath =  jsonL.GetImagePath()
        self.BackgroundImage = pygame.image.load(f'{self.ImagePath}/Background/SnowyCity.jpg').convert_alpha()
        self.DialogBox = dialogBox
        self.Personagem = personagem
        self.Monstros = monstros
        self.Actors = [None]*3
        self.Actors[0] = personagem
        self.Npcs = npcs
        self.Alpha = 255
        self.Scene = 1
        self.Filename = "ViagemTeofilotoni"
        self.MaxStoryIndex = 2
        self.Count = 0
        
    #endfunc

    def ScenesManager(self):
        if (self.Scene == 1):
            actorPos = self.PlaceActors()
            self.LoadImages(actorPos)
            self.LoadTextWithList(self.StoryTextList[self.StoryListId], heroName=self.Personagem.name)
        else:
            print("erro ao entrar nas Cenas -> inn.ScenesManager()")
        #endif
    #endfunc

    def SelectNextStory(self):
        self.Sound.StopMusic()
        return (self.Personagem, txt.Teofilotoni, True)
    #endfunc
    
    def VerifyEvent(self):
        print('verificou possiveis eventos')
        
        if(self.StoryTextList[self.StoryListId]['txt'] == "RemoverAtor1\n"):
            self.Actors[1] = None
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirTaverneira\n"):
            self.Actors[1] = lib.GetNpc(self.Npcs,"Jessie")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirAnaoFalastrao\n"):
            self.Actors[1] = lib.GetMonstro(self.Monstros,"Anao Falastrao")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirAnaoFerido\n"):
            self.Actors[1] = lib.GetMonstro(self.Monstros,"Anao Bandido")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirThete\n"):
            self.Actors[1] = lib.GetNpc(self.Npcs,"Thete")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirAnaBandida\n"):
            self.Actors[1] = lib.GetMonstro(self.Monstros,"Ana Bandida")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirLandscape\n"):
            self.Sound.StopMusic()
            self.Sound.PlayMusic("viagemTeofilo")
            self.BackgroundImage = pygame.image.load(f'{self.ImagePath}/Background/Landscape.jpg').convert_alpha()
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "battleAnaoFalastrao\n"):
            self.Sound.StopMusic()
            battleWindow = bw.BattleWindow(self.Screen,self.DialogBox, self.Personagem,lib.GetMonstro(self.Monstros,"Anao Falastrao"), "SnowyCity")
            self.Personagem = battleWindow.Battle()
            self.Sound.PlayMusic("inn")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "battleAnaoFerido\n"):
            self.Sound.StopMusic()
            battleWindow = bw.BattleWindow(self.Screen,self.DialogBox, self.Personagem,lib.GetMonstro(self.Monstros,"Anao Bandido"), "Landscape")
            self.Personagem = battleWindow.Battle()
            self.Sound.PlayMusic("viagemTeofilo")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "battleAnaBandida\n"):
            self.Sound.StopMusic()
            battleWindow = bw.BattleWindow(self.Screen,self.DialogBox, self.Personagem,lib.GetMonstro(self.Monstros,"Ana Bandida"), "Landscape")
            self.Personagem = battleWindow.Battle()
            self.Sound.PlayMusic("viagemTeofilo")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "Perder20deHP\n"):
            self.Personagem.HP -= 20
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
    #endif
#endclass
