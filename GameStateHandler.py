import pygame
from Interface.States import Inn
from Interface.States import Title as t
from Interface import DialogBox
from Interface import BattleWindow as bw
import copy as cp
import Interacoes as lib

class GameStateHandler:
    def __init__(self, screen):
        self.State = 'intro_title'
        self.Screen = screen
        self.title = t.Title(self.Screen)
    #endfunc

    def ManageState(self):
        if(self.State == "intro_title"):
            self.IntroTitle()
        if(self.State == "title"):
            self.Title()
        #endif
    #endfunc

    def Title(self):
        print("title")
    #endfunc
    def IntroTitle(self):
        print("intro_title")
        self.title.RedrawWindow()
        self.title.Update()
        return 
    #endfunc
    def Inn(self):
        print("inn")
    #endfunc
#endclass