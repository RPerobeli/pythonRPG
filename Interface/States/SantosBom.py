import pygame
import sys
#import Interface.Utils as ut
import Utils.JsonLoader as jsonL
import Interface.BattleWindow as bw
import Interface.GameOverWindow as gow
import Interacoes as lib
import Interface.States.GameState as GameState

class SantosBom(GameState.GameState):
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
        self.Filename = "SantosBom"
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
        return (self.Personagem, "RetornoAdLArqueiro", True)
    #endfunc
    
    def VerifyEvent(self):
        print('verificou possiveis eventos')
        
        #endif

        #region NPCs
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirRoger\n"):
            self.Actors[1] = lib.GetNpc(self.Npcs,"GolDRoger")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirFendric\n"):
            self.Actors[1] = lib.GetNpc(self.Npcs,"Fendric")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirTaverneiroSantos\n"):
            self.Actors[1] = lib.GetNpc(self.Npcs,"Taverneiro 2")
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
        if(self.StoryTextList[self.StoryListId]['txt'] == "BatalhaPirataBebado\n"):
            self.Sound.StopMusic()
            battleWindow = bw.BattleWindow(self.Screen,self.DialogBox, self.Personagem,lib.GetMonstro(self.Monstros,"Pirata Bebado"), "Santos")
            self.Personagem = battleWindow.Battle()
            self.Sound.PlayMusic("Santos")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "BatalhaTripulante1\n"):
            self.Sound.StopMusic()
            battleWindow = bw.BattleWindow(self.Screen,self.DialogBox, self.Personagem,lib.GetMonstro(self.Monstros,"Tripulante 1"), "PirateWarehouseNotInFire")
            self.Personagem = battleWindow.Battle()
            self.Sound.PlayMusic("Santos")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "BatalhaTripulante2\n"):
            self.Sound.StopMusic()
            battleWindow = bw.BattleWindow(self.Screen,self.DialogBox, self.Personagem,lib.GetMonstro(self.Monstros,"Tripulante 2"), "PirateWarehouseNotInFire")
            self.Personagem = battleWindow.Battle()
            self.Sound.PlayMusic("Santos")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "BatalhaTripulante3\n"):
            self.Sound.StopMusic()
            battleWindow = bw.BattleWindow(self.Screen,self.DialogBox, self.Personagem,lib.GetMonstro(self.Monstros,"Tripulante 3"), "PirateWarehouseNotInFire")
            self.Personagem = battleWindow.Battle()
            self.Sound.PlayMusic("Santos")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "BatalhaTripulante1Fire\n"):
            self.Sound.StopMusic()
            battleWindow = bw.BattleWindow(self.Screen,self.DialogBox, self.Personagem,lib.GetMonstro(self.Monstros,"Tripulante 1"), "PirateWarehouse")
            self.Personagem = battleWindow.Battle()
            self.Sound.PlayMusic("Santos")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "BatalhaTripulante2Fire\n"):
            self.Sound.StopMusic()
            battleWindow = bw.BattleWindow(self.Screen,self.DialogBox, self.Personagem,lib.GetMonstro(self.Monstros,"Tripulante 2"), "PirateWarehouse")
            self.Personagem = battleWindow.Battle()
            self.Sound.PlayMusic("Santos")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "BatalhaTripulante3Fire\n"):
            self.Sound.StopMusic()
            battleWindow = bw.BattleWindow(self.Screen,self.DialogBox, self.Personagem,lib.GetMonstro(self.Monstros,"Tripulante 3"), "PirateWarehouse")
            self.Personagem = battleWindow.Battle()
            self.Sound.PlayMusic("Santos")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "BatalhaImediatoBarbaNegra\n"):
            self.Sound.StopMusic()
            battleWindow = bw.BattleWindow(self.Screen,self.DialogBox, self.Personagem,lib.GetMonstro(self.Monstros,"Comandante"), "ShipDeck")
            self.Personagem = battleWindow.Battle()
            self.Sound.PlayMusic("Santos")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "BatalhaBecca\n"):
            self.Sound.StopMusic()
            battleWindow = bw.BattleWindow(self.Screen,self.DialogBox, self.Personagem,lib.GetMonstro(self.Monstros,"Becca"), "PirateWarehouseNotInFire")
            self.Personagem = battleWindow.Battle()
            self.Sound.PlayMusic("Santos")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        #endregion

        #region Monsters
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirBecca\n"):
            self.Actors[1] = lib.GetMonstro(self.Monstros,"Becca")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirPirataBebado\n"):
            self.Actors[1] = lib.GetMonstro(self.Monstros,"Pirata Bebado")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirBarbaNegra\n"):
            self.Actors[1] = lib.GetMonstro(self.Monstros,"Barba Negra")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif            
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirImediatoBarbaNegra\n"):
            self.Actors[1] = lib.GetMonstro(self.Monstros,"Comandante")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif            
        #endregion      

        #region Backgrounds
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirBackgroundCovilPirata\n"):
            self.BackgroundImage = pygame.image.load(f'{self.ImagePath}/Background/CovilPirata.jpg').convert_alpha()
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirBackgroundTavernaSantos\n"):
            self.BackgroundImage = pygame.image.load(f'{self.ImagePath}/Background/PirateTavern.jpg').convert_alpha()
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirBackgroundSantos\n"):
            self.BackgroundImage = pygame.image.load(f'{self.ImagePath}/Background/Santos.jpg').convert_alpha()
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirBackgroundWarehouse\n"):
            self.BackgroundImage = pygame.image.load(f'{self.ImagePath}/Background/PirateWarehouseNotInFire.jpg').convert_alpha()
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirBackgroundWarehouseFire\n"):
            self.BackgroundImage = pygame.image.load(f'{self.ImagePath}/Background/PirateWarehouse.jpg').convert_alpha()
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirBackgroundHarbor\n"):
            self.BackgroundImage = pygame.image.load(f'{self.ImagePath}/Background/PirateHarbor.jpg').convert_alpha()
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirBackgroundShip\n"):
            self.BackgroundImage = pygame.image.load(f'{self.ImagePath}/Background/ShipDeck.jpg').convert_alpha()
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        #endregion

        #region Weapons and status
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirMosquete\n"):
            self.Personagem.arma = lib.GetArma(self.Armas,"arma4Arqueiro")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "RecuperarHP\n"):
            self.Personagem.HP = self.Personagem.HPmax
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
