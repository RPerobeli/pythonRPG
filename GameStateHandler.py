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
        self.Title = t.Title(self.Screen)
        self.DialogBox = DialogBox.DialogBox(self.Screen)
        self.Hero = None
        self.Monstros = lib.CriaMonstros()
        self.Armas = lib.CriaArmas()
        
    #endfunc

    def ManageState(self):
        if(self.State == "intro_title"):
            self.IntroTitle()
        if(self.State == "inn"):
            self.Inn()
        if(self.State == "caminhoTeofilo"):
            self.ViagemTeofilotoni()
        if(self.State == "caravana"):
            self.Caravana()
        #endif
    #endfunc

    #endfunc
    def IntroTitle(self):
        print("intro_title")
        self.Title.RedrawWindow()
        self.Hero = self.Title.Update()
        if(self.Hero!=None):
            self.inn = Inn.Inn(self.Screen,self.DialogBox,self.Hero,self.Monstros)
            self.State = "inn"
    #endfunc
    def Inn(self):
        print("inn")
        self.inn.RedrawWindow()
        self.Hero,state = self.inn.Update()
        if(state != None):
            self.State = state
        #endif
    #endfunc

    def Caravana(self):
        print('caravana')
    #endfunc
    def ViagemTeofilotoni(self):
        print('caminhoTeofilo')
    #endfunc
#endclass