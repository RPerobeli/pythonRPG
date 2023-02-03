import pygame
import sys
import Interface.Utils as ut
import Utils.JsonLoader as jsonL
import Interface.BattleWindow as bw
import Interacoes as lib

class GameState():
    def __init__(self, screen):
        self.imagePath =  jsonL.GetImagePath()
        self.Screen = screen
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

#endclass