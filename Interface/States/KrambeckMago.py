import pygame
import sys
#import Interface.Utils as ut
import Utils.JsonLoader as jsonL
from Utils.ConstText import StatesText as txt
import Interface.BattleWindow as bw
import Interface.GameOverWindow as gow
import Interacoes as lib
import Interface.States.GameState as GameState

class KrambeckMago(GameState.GameState):
    def __init__(self, screen, dialogBox, personagem, monstros, npcs = None, armas= None):
        super().__init__(screen)
        self.ImagePath =  jsonL.GetImagePath()
        self.BackgroundImage = pygame.image.load(f'{self.ImagePath}/Background/PirateTavern.jpg').convert_alpha()
        self.DialogBox = dialogBox
        self.Personagem = personagem
        self.Monstros = monstros
        self.Actors = [None]*3
        self.Actors[0] = personagem
        self.Npcs = npcs
        self.Alpha = 255
        self.Scene = 1
        self.Filename = txt.KrambeckMago
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
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirPelegolas\n"):
            self.Actors[1] = lib.GetNpc(self.Npcs,"Pelegolas")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirDonoEstalagem\n"):
            self.Actors[1] = lib.GetNpc(self.Npcs,"Taverneiro2")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirSenhora\n"):
            self.Actors[1] = lib.GetNpc(self.Npcs,"Aldea")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirAldeao1\n"):
            self.Actors[1] = lib.GetNpc(self.Npcs,"Villager1")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirAldeao2\n"):
            self.Actors[1] = lib.GetNpc(self.Npcs,"Villager2")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirArqueiro\n"):
            self.Actors[1] = lib.GetNpc(self.Npcs,"Arqueiro")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirDryad\n"):
            self.Actors[1] = lib.GetNpc(self.Npcs,"Dryad")
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
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirAguiaSound\n"):
            self.Sound.PlaySFX("Aguia")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirBlacksmithSound\n"):
            self.Sound.PlaySFX("Blacksmith")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        #endregion

        #region Battles 
        if(self.StoryTextList[self.StoryListId]['txt'] == "BatalhaGhoul\n"):
            self.Sound.StopMusic()
            battleWindow = bw.BattleWindow(self.Screen,self.DialogBox, self.Personagem,lib.GetMonstro(self.Monstros,"Ghoul"), "KrambeckNight")
            self.Personagem = battleWindow.Battle()
            self.Sound.PlayMusic(txt.KrambeckArqueiro)
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "BatalhaWraith\n"):
            self.Sound.StopMusic()
            battleWindow = bw.BattleWindow(self.Screen,self.DialogBox, self.Personagem,lib.GetMonstro(self.Monstros,"Wraith"), "KrambeckNight")
            self.Personagem = battleWindow.Battle()
            self.Sound.PlayMusic(txt.KrambeckArqueiro)
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "BatalhaZumbi\n"):
            self.Sound.StopMusic()
            battleWindow = bw.BattleWindow(self.Screen,self.DialogBox, self.Personagem,lib.GetMonstro(self.Monstros,"Zumbi"), "KrambeckNight")
            self.Personagem = battleWindow.Battle()
            self.Sound.PlayMusic(txt.KrambeckArqueiro)
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "BatalhaAcolito\n"):
            self.Sound.StopMusic()
            battleWindow = bw.BattleWindow(self.Screen,self.DialogBox, self.Personagem,lib.GetMonstro(self.Monstros,"Elfo Acolito"), "Krambeck2")
            self.Personagem = battleWindow.Battle()
            self.Sound.PlayMusic(txt.KrambeckArqueiro)
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "BatalhaImp\n"):
            self.Sound.StopMusic()
            battleWindow = bw.BattleWindow(self.Screen,self.DialogBox, self.Personagem,lib.GetMonstro(self.Monstros,"Imp"), "Krambeck2")
            self.Personagem = battleWindow.Battle()
            self.Sound.PlayMusic(txt.KrambeckArqueiro)
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "BatalhaImp\n"):
            self.Sound.StopMusic()
            battleWindow = bw.BattleWindow(self.Screen,self.DialogBox, self.Personagem,lib.GetMonstro(self.Monstros,"Imp"), "Krambeck2")
            self.Personagem = battleWindow.Battle()
            self.Sound.PlayMusic(txt.KrambeckArqueiro)
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "BatalhaHidra\n"):
            self.Sound.StopMusic()
            battleWindow = bw.BattleWindow(self.Screen,self.DialogBox, self.Personagem,lib.GetMonstro(self.Monstros,"Hydra do Leste"), "ObeliskKrambeck")
            self.Personagem = battleWindow.Battle()
            self.Sound.PlayMusic(txt.KrambeckArqueiro)
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "BatalhaRhonAldyn\n"):
            self.Sound.StopMusic()
            battleWindow = bw.BattleWindow(self.Screen,self.DialogBox, self.Personagem,lib.GetMonstro(self.Monstros,"Rhon'Aldyn"), "AltarKrambeck")
            self.Personagem = battleWindow.Battle()
            self.Sound.PlayMusic(txt.KrambeckArqueiro)
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        #endregion

        #region Monsters
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirAcolito\n"):
            self.Actors[1] = lib.GetMonstro(self.Monstros,"Elfo Acolito")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirRhonAldyn\n"):
            self.Actors[1] = lib.GetMonstro(self.Monstros,"Rhon'Aldyn")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif  
        #endregion      

        #region Backgrounds
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirBackgroundKrambeck\n"):
            self.BackgroundImage = pygame.image.load(f'{self.ImagePath}/Background/Krambeck.jpg').convert_alpha()
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirBackgroundStrategyRoom\n"):
            self.BackgroundImage = pygame.image.load(f'{self.ImagePath}/Background/ElvenCouncilRoomKrambeck.jpg').convert_alpha()
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirBackgroundKrambeckNight\n"):
            self.BackgroundImage = pygame.image.load(f'{self.ImagePath}/Background/KrambeckNight.jpg').convert_alpha()
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirBackgroundKrambeckObelisk\n"):
            self.BackgroundImage = pygame.image.load(f'{self.ImagePath}/Background/ObeliskKrambeck.jpg').convert_alpha()
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirBackgroundQuartoElfico\n"):
            self.BackgroundImage = pygame.image.load(f'{self.ImagePath}/Background/ElvenRoom.jpg').convert_alpha()
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirBackgroundKrambeck2\n"):
            self.BackgroundImage = pygame.image.load(f'{self.ImagePath}/Background/Krambeck2.jpg').convert_alpha()
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirBackgroundSantuario\n"):
            self.BackgroundImage = pygame.image.load(f'{self.ImagePath}/Background/AltarKrambeck.jpg').convert_alpha()
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        #endregion

        #region Weapons and status
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirArcoMelhoradoDosElfos\n"):
            self.Personagem.arma = lib.GetArma(self.Armas,"arma2Arqueiro")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirArcoAbençoadoDosElfos\n"):
            self.Personagem.arma = lib.GetArma(self.Armas,"arma3Arqueiro")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "goSantos\n"):
            self.NextStory = "SantosBom"
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
