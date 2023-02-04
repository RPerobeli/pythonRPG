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
    #endfunc

    def RedrawWindow(self,alpha = 255):
        self.LoadImages(alpha)
    #endfunc

    def LoadImages(self, alpha = 255):
        print("não há imagens - método virtual")
    #endfunc

    def FadeOut(self):
        for alpha in range (255,-1,-5):
            self.RedrawWindow(alpha)
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

#endclass