import pygame
import sys
#import Interface.Utils as ut
import Utils.JsonLoader as jsonL
import Interface.BattleWindow as bw
import Interface.GameOverWindow as gow
import Interacoes as lib
import Interface.States.GameState as GameState

class Florianopolis(GameState.GameState):
    def __init__(self, screen, dialogBox, personagem, monstros, npcs = None, armas= None):
        super().__init__(screen)
        self.ImagePath =  jsonL.GetImagePath()
        self.BackgroundImage = pygame.image.load(f'{self.ImagePath}/Background/Florianopolis.jpg').convert_alpha()
        self.DialogBox = dialogBox
        self.Personagem = personagem
        self.Monstros = monstros
        self.Actors = [None]*3
        self.Actors[0] = personagem
        self.Npcs = npcs
        self.Alpha = 255
        self.Scene = 1
        self.Filename = "SoltosEmFloripa"
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
    
    def VerifyEvent(self):
        print('verificou possiveis eventos')
        if(self.StoryTextList[self.StoryListId]['txt'] == "RemoverAtor1\n"):
            self.Actors[1] = None
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirMagoAnciao\n"):
            self.Actors[1] = lib.GetNpc(self.Npcs,"Mago Anciao")
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
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirGuardaMagico\n"):
            self.Actors[1] = lib.GetMonstro(self.Monstros,"Guarda Magico")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirWillhelm\n"):
            self.Actors[1] = lib.GetMonstro(self.Monstros,"Willhelm")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirDemonioInferior\n"):
            self.Actors[1] = lib.GetMonstro(self.Monstros,"Demonio Inferior")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "GameOverEvent\n"):
            self.Sound.StopMusic()
            self.GameOver = gow.GameOverWindow(self.Screen)
            self.GameOver.GameOver()
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirFlorianopolis\n"):
            self.BackgroundImage = pygame.image.load(f'{self.ImagePath}/Background/Florianopolis.jpg').convert_alpha()
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InsereCorredor\n"):
            self.BackgroundImage = pygame.image.load(f'{self.ImagePath}/Background/TowerCorridor.jpg').convert_alpha()
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirCouncilRoom\n"):
            self.BackgroundImage = pygame.image.load(f'{self.ImagePath}/Background/CouncilRoom.jpg').convert_alpha()
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirUniversidade\n"):
            self.BackgroundImage = pygame.image.load(f'{self.ImagePath}/Background/MagicUniversity.jpg').convert_alpha()
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "battleGuardaMagico\n"):
            battleWindow = bw.BattleWindow(self.Screen,self.DialogBox, self.Personagem,lib.GetMonstro(self.Monstros,"Guarda Magico"), "Florianopolis")
            self.Personagem = battleWindow.Battle()
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "battleGuardaMagicoElite\n"):
            battleWindow = bw.BattleWindow(self.Screen,self.DialogBox, self.Personagem,lib.GetMonstro(self.Monstros,"Guarda de Elite"), "CouncilRoom")
            self.Personagem = battleWindow.Battle()
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "battleWillhelm\n"):
            battleWindow = bw.BattleWindow(self.Screen,self.DialogBox, self.Personagem,lib.GetMonstro(self.Monstros,"Willhelm"), "MagicUniversity")
            self.Personagem = battleWindow.Battle()
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "battleDemonioInferior\n"):
            battleWindow = bw.BattleWindow(self.Screen,self.DialogBox, self.Personagem,lib.GetMonstro(self.Monstros,"Demonio Inferior"), "TowerCorridor")
            self.Personagem = battleWindow.Battle()
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "RestoreHP\n"):
            self.Personagem.HP = self.Personagem.HPmax
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "AdquirirCajadoDoBonde\n"):
            self.Personagem.arma = lib.GetArma(self.Armas,"arma1mago")
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
        if(self.StoryTextList[self.StoryListId]['txt'] == "goKrambeck\n"):
            self.NextStory = "KrambeckMago"
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
    #endif

#endclass
