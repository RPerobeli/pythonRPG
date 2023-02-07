import pygame
import sys
import Interface.Utils as ut
import Utils.JsonLoader as jsonL
import Interface.BattleWindow as bw
import Interacoes as lib
import Interface.Button as btn

class GameState():
    def __init__(self, screen):
        self.imagePath =  jsonL.GetImagePath()
        self.Screen = screen
        self.NumberOfBtn = 0
        self.Actors = []
        self.Filename = ""
        self.StoryIndex = 1
        self.StoryListId = 0
        self.StoryTextList =[]
        self.DialogBox = None
        self.isQuestion = True
    #endfunc

    def RedrawWindow(self):
        self.ScenesManager()
    #endfunc

    def ScenesManager(self):
        print("não há imagens - método virtual")
    #endfunc

    def LoadImages(self, actorPos):
        ut.InsertBackground(self.BackgroundImage, self.Screen)
        ut.InsertImage(self.Actors[0].Image.File, self.Actors[0].Image.Width, self.Actors[0].Image.Height, actorPos['x0'],actorPos['y0'], self.Screen)
        if(len(self.Actors) > 1):
            ut.InsertImage(self.Actors[1].Image.File, self.Actors[1].Image.Width, self.Actors[1].Image.Height, actorPos['x1'],actorPos['y1'], self.Screen,self.Alpha)
        #endif
        ut.InsertImage(self.DialogBox.image,self.DialogBox.Width,self.DialogBox.Height, self.DialogBox.x, self.DialogBox.y, self.Screen)
        #endif
    #endfunc


    def FadeOut(self, actorPos):
        ut.InsertBackground(self.BackgroundImage, self.Screen,255)
        ut.InsertImage(self.Actors[0].Image.File, self.Actors[0].Image.Width, self.Actors[0].Image.Height, actorPos['x0'],actorPos['y0'], self.Screen,self.Alpha)
        if(self.Actors[1] != None):
            ut.InsertImage(self.Actors[1].Image.File, self.Actors[1].Image.Width, self.Actors[1].Image.Height, actorPos['x1'],actorPos['y1'], self.Screen,self.Alpha)
        #endif
        ut.InsertImage(self.DialogBox.image,self.DialogBox.Width,self.DialogBox.Height, self.DialogBox.x, self.DialogBox.y, self.Screen, self.Alpha)
        self.Alpha-=1
        #endif
    #endfunc

    def FadeIn(self, actorPos):
        ut.InsertBackground(self.BackgroundImage, self.Screen,255)
        ut.InsertImage(self.Actors[0].Image.File, self.Actors[0].Image.Width, self.Actors[0].Image.Height, actorPos['x0'],actorPos['y0'], self.Screen,self.Alpha)
        if(len(self.Actors) > 1):
            ut.InsertImage(self.Actors[1].Image.File, self.Actors[1].Image.Width, self.Actors[1].Image.Height, actorPos['x1'],actorPos['y1'], self.Screen,self.Alpha)
        #endif
        ut.InsertImage(self.DialogBox.image,self.DialogBox.Width,self.DialogBox.Height, self.DialogBox.x, self.DialogBox.y, self.Screen, self.Alpha)
        self.Alpha+=1
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
            actorPos = jsonL.GetActorPosition(i+1)
            returningActPos[f'x{i}'],returningActPos[f'y{i}'] = ut.TransformCenterCoordIntoBorder(self.Actors[i].Image, actorPos['x'],actorPos['y'])
        #endfor
        return returningActPos
    #endfunc

    def LoadText(self, text):
        text_color = jsonL.GetSpeakerTextColor()
        (x,y) = jsonL.GetSpeakerTextPosition()
        ut.InsertText(text,text_color, x, y, self.Screen)
    #endfunc

    def LoadTextWithList(self, textDict, x = None, y = None):
        textList = []
        textList = ut.WrapText(textDict['txt'], textList)
        text_color = jsonL.GetSpeakerTextColor()
        if(x == None or y == None):
            (x,y) = jsonL.GetSpeakerTextPosition()
        #endif
        vspace = jsonL.GetVerticalSpace()
        for text in textList:
            ut.InsertText(text,text_color, x, y, self.Screen)
            y += vspace
        #endfor
    #endfunc


    def SearchAnswerByUserInput(self, userInput):
        if(self.StoryListId == len(self.StoryTextList)-1 and self.isQuestion):
            self.isQuestion = False
            self.StoryTextList = lib.SearchText(self.Filename,self.StoryIndex,userInput)
            self.StoryListId = 0
        else:
            print("vc tem demencia?")
        #endif
    #endfunc

#endclass