import pygame
import sys
import Interface.InterfaceUtils as ut
import Utils.JsonLoader as jsonL
from Interface import BattleWindow as bw
import Interacoes as lib
import Interface.Button as btn
import Interface.Sound as Sound

class GameState():
    def __init__(self, screen):
        self.imagePath =  jsonL.GetImagePath()
        self.Screen = screen
        self.NumberOfBtn = 0
        self.Actors = [None] * 3
        self.Filename = ""
        self.StoryIndex = 1
        self.StoryListId = 0
        self.StoryTextList =[]
        self.MaxStoryIndex = 0
        self.DialogBox = None
        self.isQuestion = True
        self.Alpha = 255
        self.NextStory = "Title"
        self.Sound = Sound.Sound()
        self.Done = False
        self.Count = 0
    #endfunc

    def RedrawWindow(self):
        self.ScenesManager()
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

    def LoadImages(self, actorPos):
        ut.InsertBackground(self.BackgroundImage, self.Screen)
        if(self.Actors[0] != None):
            ut.InsertImage(self.Actors[0].Image.File, self.Actors[0].Image.Width, self.Actors[0].Image.Height, actorPos['x0'],actorPos['y0'], self.Screen)
        if(self.Actors[1] != None):
            ut.InsertImage(self.Actors[1].Image.File, self.Actors[1].Image.Width, self.Actors[1].Image.Height, actorPos['x1'],actorPos['y1'], self.Screen)
        #endif
        ut.InsertImage(self.DialogBox.image,self.DialogBox.Width,self.DialogBox.Height, self.DialogBox.x, self.DialogBox.y, self.Screen)
        #endif
    #endfunc

    def CreateButtons(self):
        self.ButtonList = []
        for i in range(1,self.NumberOfBtn + 1):
            self.ButtonList.append(btn.Button(i,i, self.Screen))
        #endfor
    #endfunc
    
    def LoadButtons(self):
        for button in self.ButtonList:
            button.Draw()
        #endfor
    #endfunc

    def PlaceActors(self):
        returningActPos = {}
        for i in range (0,len(self.Actors)):
            if(self.Actors[i] == None):
                continue
            #endif
            actorPos = jsonL.GetActorPosition(i+1)
            returningActPos[f'x{i}'],returningActPos[f'y{i}'] = ut.TransformCenterCoordIntoBorder(self.Actors[i].Image, actorPos['x'],actorPos['y'])
        #endfor
        return returningActPos
    #endfunc

    def LoadText(self, text, x = None, y = None):
        text_color = jsonL.GetSpeakerTextColor()
        if(x == None or y == None):
            (x,y) = jsonL.GetSpeakerTextPosition()
        #endif
        ut.InsertText(text,text_color, x, y, self.Screen)
    #endfunc

    def LoadTextWithList(self, textDict, x = None, y = None, heroName = "Heroi"):
        textList = []
        textDict["txt"] = textDict["txt"].replace("Heroi", heroName)
        textList = ut.WrapText(textDict['txt'], textList)
        text_color = jsonL.GetSpeakerTextColor()
        if(x == None or y == None):
            (x,y) = jsonL.GetSpeakerTextPosition()
        #endif
        vspace = jsonL.GetVerticalSpace()
        
        for text in textList:
            done = False
            if(not self.Done and not done):
                done = ut.InsertTextTypewrite(text,text_color, x, y, self.Screen)
            else:
                ut.InsertText(text,text_color, x, y, self.Screen)
            #endif
            y += vspace
        #endfor
        self.Done = True
    #endfunc


    def SearchAnswerByUserInput(self, userInput):
        self.Done = False
        if(self.StoryListId == len(self.StoryTextList)-1 and self.isQuestion):
            self.isQuestion = False
            self.StoryTextList = lib.SearchText(self.Filename,self.StoryIndex,userInput)
            self.StoryListId = 0
        else:
            print("vc tem demencia?")
        #endif
    #endfunc

    def VerifyFirstTimeInWindowToPlayMusic(self, music):
        if(music == 'Recuros' or music == 'caminhoTeofilo' or music == 'caravana'):
            music = 'inn'
        #endif
        if(self.Count == 0):
            self.Sound.PlayMusic(f"{music}")
        #endif
    #endfunction


    def SelectNextStory(self):
        self.Sound.StopMusic()
        return (self.Personagem, self.NextStory, True)
    #endfunc

    def Update(self, nomeState):
        #Cena tapa na cachorra
        pygame.display.set_caption(nomeState)
        self.VerifyFirstTimeInWindowToPlayMusic(nomeState)
        if(self.Count == 0):
            self.StoryTextList = lib.SearchText(self.Filename,self.StoryIndex)
            self.Count += 1
        #endif
        self.ScenesManager()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #endif
            if (event.type == pygame.KEYDOWN and (event.key == pygame.K_KP_ENTER or event.key == pygame.K_SPACE)):
                if(self.StoryListId == len(self.StoryTextList)-1):
                    if(self.isQuestion and self.StoryIndex < self.MaxStoryIndex):
                        self.Sound.PlaySFX("cursorError")
                        print(self.MaxStoryIndex)
                        print("Ta com pressa irmao? para de pular os dialogos.")
                    else:
                        self.Sound.PlaySFX("cursorForward")
                        self.isQuestion = True
                        self.StoryIndex += 1 
                        if(self.StoryIndex > self.MaxStoryIndex):
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
        return self.Personagem,nomeState, False
    #endFunction
#endclass