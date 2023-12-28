import pygame
import sys
#import Interface.Utils as ut
import Utils.JsonLoader as jsonL
import Interface.BattleWindow as bw
import Interface.GameOverWindow as gow
import Interacoes as lib
import Interface.States.GameState as GameState
from Utils.ConstText import StatesText as txt

class Recursos(GameState.GameState):
    def __init__(self, screen, dialogBox, personagem, monstros, npcs = None, armas= None):
        super().__init__(screen)
        self.ImagePath =  jsonL.GetImagePath()
        self.BackgroundImage = pygame.image.load(f'{self.ImagePath}/Background/guild.jpg').convert_alpha()
        self.DialogBox = dialogBox
        self.Personagem = personagem
        self.Monstros = monstros
        self.Actors = [None]*3
        self.Actors[0] = personagem
        self.Npcs = npcs
        self.Alpha = 255
        self.Scene = 1
        self.Filename = txt.Recursos
        self.MaxStoryIndex = 1
        self.Count = 0
        self.Armas = armas
        
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
        return (self.Personagem, txt.Curitiba, True)
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
            self.Actors[1] = lib.GetNpc(self.Npcs,"Taverneira")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif

        if(self.StoryTextList[self.StoryListId]['txt'] == "BattleEstatua\n"):
            self.Sound.StopMusic()
            battleWindow = bw.BattleWindow(self.Screen,self.DialogBox, self.Personagem,lib.GetMonstro(self.Monstros,"Cavaleiro Estatua"), "Forest")
            self.Personagem = battleWindow.Battle()
            self.Sound.PlayMusic(txt.Recursos)
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "BattleLobo\n"):
            self.Sound.StopMusic()
            battleWindow = bw.BattleWindow(self.Screen,self.DialogBox, self.Personagem,lib.GetMonstro(self.Monstros,"Lobo"), "Cave")
            self.Personagem = battleWindow.Battle()
            self.Sound.PlayMusic(txt.Recursos)
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "BattleTreant\n"):
            self.Sound.StopMusic()
            battleWindow = bw.BattleWindow(self.Screen,self.DialogBox, self.Personagem,lib.GetMonstro(self.Monstros,"Treant"), "Forest")
            self.Personagem = battleWindow.Battle()
            self.Sound.PlayMusic(txt.Recursos)
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
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirFloresta\n"):
            self.Sound.StopMusic()
            self.Sound.PlayMusic(txt.Recursos)
            self.BackgroundImage = pygame.image.load(f'{self.ImagePath}/Background/Forest.jpg').convert_alpha()
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirCaverna\n"):
            self.BackgroundImage = pygame.image.load(f'{self.ImagePath}/Background/Cave.jpg').convert_alpha()
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "Lose10HP\n"):
            self.Personagem.HP = self.Personagem.HP - 10
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "Ladrao\n"):
            self.Sound.PlaySFX("ladrao")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        
    #endif

#endclass
