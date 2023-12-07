import pygame
import sys
#import Interface.Utils as ut
import Utils.JsonLoader as jsonL
import Interface.BattleWindow as bw
import Interface.GameOverWindow as gow
import Interacoes as lib
import Interface.States.GameState as GameState

class Teofilotoni(GameState.GameState):
    def __init__(self, screen, dialogBox, personagem, monstros, npcs = None, armas= None):
        super().__init__(screen)
        self.ImagePath =  jsonL.GetImagePath()
        self.BackgroundImage = pygame.image.load(f'{self.ImagePath}/Background/TeofilotoniGates.jpg').convert_alpha()
        self.DialogBox = dialogBox
        self.Personagem = personagem
        self.Monstros = monstros
        self.Actors = [None]*3
        self.Actors[0] = personagem
        self.Npcs = npcs
        self.Alpha = 255
        self.Scene = 1
        self.Filename = "Teofilotoni"
        self.MaxStoryIndex = 4
        self.Count = 0
        self.Armas = armas
        
    #endfunc

    def SelectNextStory(self):
        self.Sound.StopMusic()
        return (self.Personagem, self.NextStory, True)
    #endfunc
    
    def VerifyEvent(self):
        print('verificou possiveis eventos')

        if(self.StoryTextList[self.StoryListId]['txt'] == "RemoverAtor1\n"):
            self.Actors[1] = None
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
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirTok\n"):
            self.Actors[1] = lib.GetNpc(self.Npcs,"Tok")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirTik\n"):
            self.Actors[1] = lib.GetNpc(self.Npcs,"Tik")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "BattleAnaoAtiradorInn\n"):
            self.Sound.StopMusic()
            battleWindow = bw.BattleWindow(self.Screen,self.DialogBox, self.Personagem,lib.GetMonstro(self.Monstros,"Anao Atirador"), "TeofilotoniInn")
            self.Personagem = battleWindow.Battle()
            self.Sound.PlayMusic("Teofilotoni")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "BattleAnaoAtiradorStreet\n"):
            self.Sound.StopMusic()
            battleWindow = bw.BattleWindow(self.Screen,self.DialogBox, self.Personagem,lib.GetMonstro(self.Monstros,"Anao Atirador"), "TeofilotoniStreets")
            self.Personagem = battleWindow.Battle()
            self.Sound.PlayMusic("Teofilotoni")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "BattleAnaoPolicialStreet\n"):
            self.Sound.StopMusic()
            battleWindow = bw.BattleWindow(self.Screen,self.DialogBox, self.Personagem,lib.GetMonstro(self.Monstros,"Anao Policial"), "TeofilotoniStreets")
            self.Personagem = battleWindow.Battle()
            self.Sound.PlayMusic("Teofilotoni")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "BattleAnaoPolicialInn\n"):
            self.Sound.StopMusic()
            battleWindow = bw.BattleWindow(self.Screen,self.DialogBox, self.Personagem,lib.GetMonstro(self.Monstros,"Anao Policial"), "TeofilotoniInn")
            self.Personagem = battleWindow.Battle()
            self.Sound.PlayMusic("Teofilotoni")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "BattleAnaoMagoStreet\n"):
            self.Sound.StopMusic()
            battleWindow = bw.BattleWindow(self.Screen,self.DialogBox, self.Personagem,lib.GetMonstro(self.Monstros,"Anao Mago"), "TeofilotoniStreets")
            self.Personagem = battleWindow.Battle()
            self.Sound.PlayMusic("Teofilotoni")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "battleAnaoNobre\n"):
            self.Sound.StopMusic()
            battleWindow = bw.BattleWindow(self.Screen,self.DialogBox, self.Personagem,lib.GetMonstro(self.Monstros,"Anao Nobre"), "TeofilotoniStreets")
            self.Personagem = battleWindow.Battle()
            self.Sound.PlayMusic("Teofilotoni")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "battleAssassino\n"):
            self.Sound.StopMusic()
            battleWindow = bw.BattleWindow(self.Screen,self.DialogBox, self.Personagem,lib.GetMonstro(self.Monstros,"Anao Assassino"), "TikTokHouse")
            self.Personagem = battleWindow.Battle()
            self.Sound.PlayMusic("Teofilotoni")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "battleCampeao\n"):
            self.Sound.StopMusic()
            battleWindow = bw.BattleWindow(self.Screen,self.DialogBox, self.Personagem,lib.GetMonstro(self.Monstros,"Gel'ssu"), "DwarvenPalace")
            self.Personagem = battleWindow.Battle()
            self.Sound.PlayMusic("Teofilotoni")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirTaverneiro\n"):
            self.Actors[1] = lib.GetNpc(self.Npcs,"Taverneiro")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirGuardaExterno\n"):
            self.Actors[1] = lib.GetNpc(self.Npcs,"Guarda Anao")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirNobreAnao\n"):
            self.Actors[1] = lib.GetMonstro(self.Monstros,"Anao Nobre")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirGuarda\n"):
            self.Actors[1] = lib.GetMonstro(self.Monstros,"Anao Policial")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirCampeao\n"):
            self.Actors[1] = lib.GetMonstro(self.Monstros,"Gel'ssu")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirReiAnao\n"):
            self.Actors[1] = lib.GetNpc(self.Npcs,"Rei dos Anoes")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        
        if(self.StoryTextList[self.StoryListId]['txt'] == "GameOverEvent\n"):
            self.GameOver = gow.GameOverWindow(self.Screen)
            self.Sound.StopMusic()
            self.GameOver.GameOver()
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirBackgroundTeofilotoniInn\n"):
            self.BackgroundImage = pygame.image.load(f'{self.ImagePath}/Background/TeofilotoniInn.jpg').convert_alpha()
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirBackgroundTeofilotoniStreets\n"):
            self.BackgroundImage = pygame.image.load(f'{self.ImagePath}/Background/TeofilotoniStreets.jpg').convert_alpha()
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirBattlegroundTikTokHouse\n"):
            self.BackgroundImage = pygame.image.load(f'{self.ImagePath}/Background/TikTokHouse.jpg').convert_alpha()
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirBackgroundDwarvenPalace\n"):
            self.BackgroundImage = pygame.image.load(f'{self.ImagePath}/Background/DwarvenPalace.jpg').convert_alpha()
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "LoseMPTotal\n"):
            self.Personagem.MP = 0
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "LoseMPMetade\n"):
            self.Personagem.MP = self.Personagem.MP/2
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "LoseMPMetade\n"):
            self.Personagem.MP = self.Personagem.MP/2
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirMartelodoNobre\n"):
            self.Personagem.arma = lib.GetArma(self.Armas,"arma1Guerreiro")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "goAcre\n"):
            self.NextStory = "Acre"
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "goFelastus\n"):
            self.NextStory = "Felastus"
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
    #endif

#endclass
