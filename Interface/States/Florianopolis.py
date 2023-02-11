import pygame
import sys
import Interface.Utils as ut
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
        self.Actors = []
        self.Actors.append(personagem)
        self.Npcs = npcs
        self.Alpha = 255
        self.Scene = 1
        self.Filename = "SoltosEmFloripa"
        self.MaxStoryIndex = 5
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
        return (self.Personagem, 'Teofilotoni', True)
    #endfunc
    
    def VerifyEvent(self):
        print('verificou possiveis eventos')
        if(self.StoryTextList[self.StoryListId]['txt'] == "RemoverAtor1\n"):
            self.Actors.pop(1)
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirMagoAnciao\n"):
            self.Actors.append(lib.GetNpc(self.Npcs,"Mago Anciao"))
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirDryad\n"):
            self.Actors.append(lib.GetNpc(self.Npcs,"Dryad"))
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirGuardaMagico\n"):
            self.Actors.append(lib.GetMonstro(self.Monstros,"Guarda Magico"))
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirWillhelm\n"):
            self.Actors.append(lib.GetMonstro(self.Monstros,"Willhelm"))
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirDemonioInferior\n"):
            self.Actors.append(lib.GetMonstro(self.Monstros,"Demonio Inferior"))
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "GameOverEvent\n"):
            self.GameOver = gow.GameOverWindow(self.Screen)
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
            battleWindow = bw.BattleWindow(self.Screen,self.DialogBox, self.Personagem,lib.GetMonstro(self.Monstros,"Guarda Magico de Elite"), "CouncilRoom")
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
    #endif

    def Update(self):
        pygame.display.set_caption("Florianopolis")
        if(self.Count == 0):
            self.StoryTextList = lib.SearchText(self.Filename,self.StoryIndex)
            self.Count+=1
        #endif
        self.ScenesManager()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #endif
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_KP_ENTER):
                if(self.StoryListId == len(self.StoryTextList)-1):
                    if(self.isQuestion):
                        print("Ta com pressa irmao? para de pular os dialogos.")
                    else:
                        self.isQuestion = True
                        self.StoryIndex += 1 
                        if(self.StoryIndex == self.MaxStoryIndex):
                            return self.SelectNextStory()
                        #endif
                        self.StoryTextList = lib.SearchText(self.Filename,self.StoryIndex)
                        self.StoryListId = 0 
                        self.VerifyEvent()
                else:
                    self.StoryListId += 1
                    self.VerifyEvent()
                #endif
            #endif
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_1):
                self.SearchAnswerByUserInput(1)
                self.VerifyEvent()
            #endif
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_2):
                self.SearchAnswerByUserInput(2)
                self.VerifyEvent()
            #endif
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_3):
                self.SearchAnswerByUserInput(3)
                self.VerifyEvent()
            #endif
        #endfor
        pygame.display.update()
        return self.Personagem,'Florianopolis',False
    #endFunction

#endclass