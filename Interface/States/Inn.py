import pygame
import sys
import random as rnd
import Interface.InterfaceUtils as ut
from Utils.ConstText import StatesText as txt
import Utils.JsonLoader as jsonL
import Interface.BattleWindow as bw
import Interacoes as lib
import Interface.States.GameState as GameState
#import Interface.Sound as Sound

class Inn(GameState.GameState):
    def __init__(self, screen, dialogBox, personagem, monstros, npcs = None):
        super().__init__(screen)
        self.ImagePath =  jsonL.GetImagePath()
        self.BackgroundImage = pygame.image.load(f'{self.ImagePath}/Background/quarto.jpg').convert_alpha()
        self.DialogBox = dialogBox
        self.Personagem = personagem
        self.Monstros = monstros
        self.Actors = [None]*3
        self.Actors[0] = personagem
        self.Npcs = npcs
        self.Alpha = 0
        self.Scene = 1
        self.Filename = "Introducao"
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
        if(self.Personagem.classe.lower() == 'guerreiro'):
            return (self.Personagem, txt.CaminhoTeofilo,True)
        elif(self.Personagem.classe.lower() == 'mago'):
            return (self.Personagem, txt.Caravana,True)
        elif(self.Personagem.classe.lower() == 'arqueiro'):
            return (self.Personagem, txt.Recursos,True)
        else:
            print('erro ao selecionar proxima historia')
        #endif
    #endfunc
    
    def VerifyEvent(self):
        print('verificou possiveis eventos')
        if(self.StoryTextList[self.StoryListId]['txt'] == "battleCachorra\n"):
            self.Sound.StopMusic()
            battleWindow = bw.BattleWindow(self.Screen,self.DialogBox, self.Personagem,lib.GetMonstro(self.Monstros,"Cao Infernal"), "quarto")
            self.Personagem = battleWindow.Battle()
            self.Sound.PlayMusic(txt.Inn)
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "perde 2 de hp\n"):
            self.Personagem.HP -= 2
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "Temer\n"):
            self.Sound.PlaySFX("temer")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "removerCachorra\n"):
            print("removeu a cachorra")
            self.Actors[1] = None
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "inserirCachorra\n"):
            print("inseriu a cachorra")
            self.Actors[1] = lib.GetMonstro(self.Monstros,"Cao Infernal")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirBackgroundCidade\n"):
            print('inseriu background')
            self.BackgroundImage = pygame.image.load(f'{self.ImagePath}/Background/SnowyCity.jpg').convert_alpha()
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirTaverneira\n"):
            self.BackgroundImage = pygame.image.load(f'{self.ImagePath}/Background/guild.jpg').convert_alpha()
            self.Actors[1] = lib.GetNpc(self.Npcs,"Jessie")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "perder10hp\n"):
            self.Personagem.HP -= 10
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif   
    #endif

#endclass
