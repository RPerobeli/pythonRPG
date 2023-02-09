import pygame
import sys
import Interface.Utils as ut
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
        self.Alpha = 0
        self.Scene = 1
        self.Filename = "Caravan"
        self.MaxStoryIndex = 1
        
    #endfunc

    def ScenesManager(self):
        if (self.Scene == 1):
            actorPos = self.PlaceActors()
            self.LoadImages(actorPos)
            print(self.StoryIndex)
            print(self.StoryListId)
            print(self.StoryTextList)
            pygame.quit()
            self.LoadTextWithList(self.StoryTextList[self.StoryListId])
        else:
            print("erro ao entrar nas Cenas -> inn.ScenesManager()")
        #endif
    #endfunc

    def SelectNextStory(self):
        return (self.Personagem, 'Florianopolis')
    #endfunc
    
    def VerifyEvent(self):
        print('verificou possiveis eventos')
        
        
    #endif

    def Update(self):
        #Cena tapa na cachorra
        pygame.display.set_caption("Caravana")
        if(self.Scene == 1):
            self.StoryTextList = lib.SearchText(self.Filename,self.StoryIndex)
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
        return self.Personagem,'caravan'
    #endFunction

#endclass
