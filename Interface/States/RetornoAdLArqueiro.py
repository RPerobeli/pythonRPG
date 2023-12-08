import pygame
import sys
#import Interface.Utils as ut
import Utils.JsonLoader as jsonL
import Interface.BattleWindow as bw
import Interface.GameOverWindow as gow
import Interacoes as lib
import Interface.States.GameState as GameState

class RetornoAdLArqueiro(GameState.GameState):
    def __init__(self, screen, dialogBox, personagem, monstros, npcs = None, armas= None):
        super().__init__(screen)
        self.ImagePath =  jsonL.GetImagePath()
        self.BackgroundImage = pygame.image.load(f'{self.ImagePath}/Background/Santos.jpg').convert_alpha()
        self.DialogBox = dialogBox
        self.Personagem = personagem
        self.Monstros = monstros
        self.Actors = [None]*3
        self.Actors[0] = personagem
        self.Npcs = npcs
        self.Alpha = 255
        self.Scene = 1
        self.Filename = "RetornoAdLArqueiro"
        self.MaxStoryIndex = 3
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
        return (self.Personagem, "Final", True)
    #endfunc
    
    def VerifyEvent(self):
        print('verificou possiveis eventos')
        
        if(self.StoryTextList[self.StoryListId]['txt'] == "RemoverAtor1\n"):
            self.Actors[1] = None
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif

        #region NPCs
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirPelegolas\n"):
            self.Actors[1] = lib.GetNpc(self.Npcs,"Pelegolas")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirEndilien\n"):
            self.Actors[1] = lib.GetNpc(self.Npcs,"Endilien")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirLiriel\n"):
            self.Actors[1] = lib.GetNpc(self.Npcs,"Liriel")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirMensageiro\n"):
            self.Actors[1] = lib.GetNpc(self.Npcs,"Mensageiro")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        
        #endregion
        
        #region Sound
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirSoundShot\n"):
            self.Sound.StopMusic()
            self.Sound.PlaySFX("Tiro")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirMusicaBordel\n"):
            self.Sound.StopMusic()
            self.Sound.PlayMusic("brothel")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirSoundBarragem\n"):
            self.Sound.PlaySFX("Barragem")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        #endregion

        #region Battles 
        if(self.StoryTextList[self.StoryListId]['txt'] == "BatalhaUndeadArcher\n"):
            self.Sound.StopMusic()
            battleWindow = bw.BattleWindow(self.Screen,self.DialogBox, self.Personagem,lib.GetMonstro(self.Monstros,"Arqueiro Morto"), "SnowyKrambeck")
            self.Personagem = battleWindow.Battle()
            self.Sound.PlayMusic("RetornoAdLArqueiro")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        
        #endregion

        #region Monsters
                   
        #endregion      

        #region Backgrounds
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirBackgroundSnowyKrambeck\n"):
            self.BackgroundImage = pygame.image.load(f'{self.ImagePath}/Background/SnowyKrambeck.jpg').convert_alpha()
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirBackgroundCuritibaNight\n"):
            self.BackgroundImage = pygame.image.load(f'{self.ImagePath}/Background/CuritibaNight.jpg').convert_alpha()
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        
        #endregion

        #region Weapons and status        
        if(self.StoryTextList[self.StoryListId]['txt'] == "GameOverEvent\n"):
            self.GameOver = gow.GameOverWindow(self.Screen)
            self.Sound.StopMusic()
            self.GameOver.GameOver()
        #endif
        #endregion
    #endif

#endclass
