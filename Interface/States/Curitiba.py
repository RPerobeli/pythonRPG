import pygame
import sys
#import Interface.Utils as ut
import Utils.JsonLoader as jsonL
from Utils.ConstText import StatesText as txt
import Interface.BattleWindow as bw
import Interface.GameOverWindow as gow
import Interacoes as lib
import Interface.States.GameState as GameState

class Curitiba(GameState.GameState):
    def __init__(self, screen, dialogBox, personagem, monstros, npcs = None, armas= None):
        super().__init__(screen)
        self.ImagePath =  jsonL.GetImagePath()
        self.BackgroundImage = pygame.image.load(f'{self.ImagePath}/Background/Curitiba.jpg').convert_alpha()
        self.DialogBox = dialogBox
        self.Personagem = personagem
        self.Monstros = monstros
        self.Actors = [None]*3
        self.Actors[0] = personagem
        self.Npcs = npcs
        self.Alpha = 255
        self.Scene = 1
        self.Filename = txt.Curitiba
        self.MaxStoryIndex = 4
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

        #region NPCs
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirLiriel\n"):
            self.Actors[1] = lib.GetNpc(self.Npcs,"Liriel")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirSoldadoElfo\n"):
            self.Actors[1] = lib.GetMonstro(self.Monstros,"Soldado Elfo 1")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirSoldadoElfo2\n"):
            self.Actors[1] = lib.GetMonstro(self.Monstros,"Soldado Elfo 2")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirElfoBandido\n"):
            self.Actors[1] = lib.GetMonstro(self.Monstros,"Elfo Bandido")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirMeretriz\n"):
            self.Actors[1] = lib.GetNpc(self.Npcs,"ElfWhore")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirElfoLarapio\n"):
            self.Actors[1] = lib.GetMonstro(self.Monstros,"Elfo Larapio")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        #endregion
        
        #region Sound
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirMusicaBordel\n"):
            self.Sound.StopMusic()
            self.Sound.PlayMusic("brothel")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        #endregion

        #region Battles
        if(self.StoryTextList[self.StoryListId]['txt'] == "BattleSoldadoElfo1\n"):
            self.Sound.StopMusic()
            battleWindow = bw.BattleWindow(self.Screen,self.DialogBox, self.Personagem,lib.GetMonstro(self.Monstros,"Soldado Elfo 1"), "Curitiba")
            self.Personagem = battleWindow.Battle()
            self.Sound.PlayMusic("Curitiba")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "BattleSoldadoElfo2\n"):
            self.Sound.StopMusic()
            battleWindow = bw.BattleWindow(self.Screen,self.DialogBox, self.Personagem,lib.GetMonstro(self.Monstros,"Soldado Elfo 2"), "Curitiba")
            self.Personagem = battleWindow.Battle()
            self.Sound.PlayMusic("Curitiba")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "BattleCriminosoAtirador\n"):
            self.Sound.StopMusic()
            battleWindow = bw.BattleWindow(self.Screen,self.DialogBox, self.Personagem,lib.GetMonstro(self.Monstros,"Criminoso Atirador"), "Brothel")
            self.Personagem = battleWindow.Battle()
            self.Sound.PlayMusic("brothel")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "BattleCriminoso\n"):
            self.Sound.StopMusic()
            battleWindow = bw.BattleWindow(self.Screen,self.DialogBox, self.Personagem,lib.GetMonstro(self.Monstros,"Criminoso Lanceiro"), "Brothel")
            self.Personagem = battleWindow.Battle()
            self.Sound.PlayMusic("brothel")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "BattleMystral\n"):
            self.Sound.StopMusic()
            battleWindow = bw.BattleWindow(self.Screen,self.DialogBox, self.Personagem,lib.GetMonstro(self.Monstros,"Mystral"), "Brothel")
            self.Personagem = battleWindow.Battle()
            self.Sound.PlayMusic("brothel")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "BattleSylathor\n"):
            self.Sound.StopMusic()
            battleWindow = bw.BattleWindow(self.Screen,self.DialogBox, self.Personagem,lib.GetMonstro(self.Monstros,"Sylathor"), "Brothel")
            self.Personagem = battleWindow.Battle()
            self.Sound.PlayMusic("brothel")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        #endregion

        #region Monsters
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirSylathor\n"):
            self.Actors[1] = lib.GetMonstro(self.Monstros,"Sylathor")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirCriminosoAtirador\n"):
            self.Actors[1] = lib.GetMonstro(self.Monstros,"Criminoso Atirador")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirMystral\n"):
            self.Actors[1] = lib.GetMonstro(self.Monstros,"Mystral")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif  
        #endregion      

        #region Backgrounds
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirKrambeck\n"):
            self.BackgroundImage = pygame.image.load(f'{self.ImagePath}/Background/Brothel.jpg').convert_alpha()
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirBackgroundBrothelRoom\n"):
            self.BackgroundImage = pygame.image.load(f'{self.ImagePath}/Background/BrothelRoom.jpg').convert_alpha()
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirBackgroundBordel\n"):
            self.BackgroundImage = pygame.image.load(f'{self.ImagePath}/Background/Brothel.jpg').convert_alpha()
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirCuritibaComMusica\n"):
            self.BackgroundImage = pygame.image.load(f'{self.ImagePath}/Background/Curitiba.jpg').convert_alpha()
            self.Sound.StopMusic()
            self.Sound.PlayMusic("Curitiba")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        #endregion

        #region Weapons and status
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirArcoLiriel\n"):
            self.Personagem.arma = lib.GetArma(self.Armas,"arma1Arqueiro")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "Perder10HP\n"):
            self.Personagem.HP = self.Personagem.HP/2
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "UmaMaquina\n"):
            self.Sound.PlaySFX("umaMaquina")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "goAcre\n"):
            self.NextStory = "AcreArqueiro"
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "goKrambeck\n"):
            self.NextStory = txt.KrambeckArqueiro
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "GameOverEvent\n"):
            self.GameOver = gow.GameOverWindow(self.Screen)
            self.Sound.StopMusic()
            self.GameOver.GameOver()
        #endif
        #endregion
    #endif

#endclass
