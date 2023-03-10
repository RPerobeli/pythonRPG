import pygame
import sys
#import Interface.Utils as ut
import Utils.JsonLoader as jsonL
import Interface.BattleWindow as bw
import Interacoes as lib
import Interface.States.GameState as GameState

class Caravan(GameState.GameState):
    def __init__(self, screen, dialogBox, personagem, monstros, npcs = None):
        super().__init__(screen)
        self.ImagePath =  jsonL.GetImagePath()
        self.BackgroundImage = pygame.image.load(f'{self.ImagePath}/Background/SnowyCity.png').convert_alpha()
        self.DialogBox = dialogBox
        self.Personagem = personagem
        self.Monstros = monstros
        self.Actors = []
        self.Actors.append(personagem)
        self.Npcs = npcs
        self.Alpha = 255
        self.Scene = 1
        self.Filename = "Caravana"
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
        return (self.Personagem, 'Florianopolis', True)
    #endfunc
    
    def VerifyEvent(self):
        print('verificou possiveis eventos')
        if(self.StoryTextList[self.StoryListId]['txt'] == "RemoverTaverneira\n"):
            self.Actors.pop(1)
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirTaverneira\n"):
            self.Actors.append(lib.GetNpc(self.Npcs,"Jessie"))
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirFloresta\n"):
            self.BackgroundImage = pygame.image.load(f'{self.ImagePath}/Background/NightForest.jpg').convert_alpha()
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "battleBandido1\n"):
            battleWindow = bw.BattleWindow(self.Screen,self.DialogBox, self.Personagem,lib.GetMonstro(self.Monstros,"Bandido"), "NightForest")
            self.Personagem = battleWindow.Battle()
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "BattleJavali\n"):
            battleWindow = bw.BattleWindow(self.Screen,self.DialogBox, self.Personagem,lib.GetMonstro(self.Monstros,"Javali"), "NightForest")
            self.Personagem = battleWindow.Battle()
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "battleBandido2\n"):
            battleWindow = bw.BattleWindow(self.Screen,self.DialogBox, self.Personagem,lib.GetMonstro(self.Monstros,"Bandido Atirador"), "NightForest")
            self.Personagem = battleWindow.Battle()
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "BattleOrcBesteiro\n"):
            battleWindow = bw.BattleWindow(self.Screen,self.DialogBox, self.Personagem,lib.GetMonstro(self.Monstros,"Orc Besteiro"), "NightForest")
            self.Personagem = battleWindow.Battle()
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "RestoreMP\n"):
            self.Personagem.MP = self.Personagem.MPmax
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        
    #endif

    def Update(self):
        #Cena tapa na cachorra
        pygame.display.set_caption("Caravana")
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
            if (event.type == pygame.KEYDOWN and (event.key == pygame.K_KP_ENTER or event.key == pygame.K_SPACE)):
                if(self.StoryListId == len(self.StoryTextList)-1):
                    if(self.isQuestion):
                        self.Sound.PlaySFX("cursorError")
                        print("Ta com pressa irmao? para de pular os dialogos.")
                    else:
                        self.Sound.PlaySFX("cursorForward")
                        self.isQuestion = True
                        self.StoryIndex += 1 
                        if(self.StoryIndex == self.MaxStoryIndex):
                            return self.SelectNextStory()
                        #endif
                        self.StoryTextList = lib.SearchText(self.Filename,self.StoryIndex)
                        self.StoryListId = 0 
                        self.VerifyEvent()
                else:
                    self.Sound.PlaySFX("cursorForward")
                    self.StoryListId += 1
                    self.Done = False
                    self.VerifyEvent()
                #endif
            #endif
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_1):
                self.Sound.PlaySFX("cursorForward")
                self.Personagem.Good += 1
                self.SearchAnswerByUserInput(1)
                self.VerifyEvent()
            #endif
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_2):
                self.Sound.PlaySFX("cursorForward")
                self.Personagem.Neutral += 1
                self.SearchAnswerByUserInput(2)
                self.VerifyEvent()
            #endif
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_3):
                self.Sound.PlaySFX("cursorForward")
                self.Personagem.Evil += 1
                self.SearchAnswerByUserInput(3)
                self.VerifyEvent()
            #endif
        #endfor
        pygame.display.update()
        return self.Personagem,'caravana',False
    #endFunction

#endclass
