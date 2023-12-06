import pygame
import sys
#import Interface.Utils as ut
import Utils.JsonLoader as jsonL
import Interface.BattleWindow as bw
import Interface.GameOverWindow as gow
import Interacoes as lib
import Interface.States.GameState as GameState

class Recursos(GameState.GameState):
    def __init__(self, screen, dialogBox, personagem, monstros, npcs = None, armas= None):
        super().__init__(screen)
        self.ImagePath =  jsonL.GetImagePath()
        self.BackgroundImage = pygame.image.load(f'{self.ImagePath}/Background/guild.jpg').convert_alpha()
        self.DialogBox = dialogBox
        self.Personagem = personagem
        self.Monstros = monstros
        self.Actors = []
        self.Actors.append(personagem)
        self.Npcs = npcs
        self.Alpha = 255
        self.Scene = 1
        self.Filename = "ColetaRecursos"
        self.MaxStoryIndex = 2
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
        return (self.Personagem, "Curitiba", True)
    #endfunc
    
    def VerifyEvent(self):
        print('verificou possiveis eventos')
        if(self.StoryTextList[self.StoryListId]['txt'] == "RemoverAtor1\n"):
            self.Actors.pop(1)
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirTaverneira\n"):
            self.Actors.append(lib.GetNpc(self.Npcs,"Taverneira"))
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif

        if(self.StoryTextList[self.StoryListId]['txt'] == "BattleEstatua\n"):
            self.Sound.StopMusic()
            battleWindow = bw.BattleWindow(self.Screen,self.DialogBox, self.Personagem,lib.GetMonstro(self.Monstros,"Cavaleiro Estatua"), "Forest")
            self.Personagem = battleWindow.Battle()
            self.Sound.PlayMusic("forest")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "BattleLobo\n"):
            self.Sound.StopMusic()
            battleWindow = bw.BattleWindow(self.Screen,self.DialogBox, self.Personagem,lib.GetMonstro(self.Monstros,"Lobo"), "Cave")
            self.Personagem = battleWindow.Battle()
            self.Sound.PlayMusic("forest")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "BattleTreant\n"):
            self.Sound.StopMusic()
            battleWindow = bw.BattleWindow(self.Screen,self.DialogBox, self.Personagem,lib.GetMonstro(self.Monstros,"Treant"), "Forest")
            self.Personagem = battleWindow.Battle()
            self.Sound.PlayMusic("forest")
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
            self.Sound.PlayMusic("forest")
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

    def Update(self):
        self.VerifyFirstTimeInWindowToPlayMusic("inn")
        pygame.display.set_caption("Recursos")
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
                            self.Sound.StopMusic()
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
        return self.Personagem,'Recursos',False
    #endFunction

#endclass
