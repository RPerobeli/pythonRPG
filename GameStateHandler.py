import pygame
from Interface.States import Inn
from Interface.States import Caravan
from Interface.States import Title as t
from Interface import DialogBox
from Interface import BattleWindow as bw
from Utils import JsonLoader as jsonL
import copy as cp
import Interacoes as lib

class GameStateHandler:
    def __init__(self, screen):
        self.State = 'intro_title'
        self.Screen = screen
        self.Title = t.Title(self.Screen)
        self.DialogBox = DialogBox.DialogBox(self.Screen)
        self.Hero = None
        self.Monstros = lib.CreateMonsters()
        self.Armas = lib.CriaArmas()
        self.Npcs = lib.CreateNpcs()
        
    #endfunc

    def ManageState(self):
        if(self.State == "intro_title"):
            self.IntroTitle()
        if(self.State == "inn"):
            self.Inn()
        if(self.State == "caminhoTeofilo"):
            self.ViagemTeofilotoni()
        if(self.State == "caravana"):
            self.Caravan()
        if(self.State == "Florianopolis"):
            self.Florianopolis()
        #endif
    #endfunc

    #endfunc
    def IntroTitle(self):
        print("intro_title")
        self.Title.RedrawWindow()
        self.Hero = self.Title.Update()
        if(self.Hero!=None):
            self.inn = Inn.Inn(self.Screen,self.DialogBox,self.Hero,self.Monstros, self.Npcs)
            self.State = "inn"
    #endfunc
    def Inn(self):
        print("inn")
        self.inn.RedrawWindow()
        self.Hero,state, continueStory = self.inn.Update()
        self.State = state
        if(continueStory):
            self.caravan = Caravan.Caravan(self.Screen,self.DialogBox,self.Hero,self.Monstros,self.Npcs)
        #endif
    #endfunc

    def Caravan(self):
        print('caravana')
        self.Hero,state, continueStory = self.caravan.Update()
        self.State = state
        if(continueStory):
            print("partiu floripa")
        #endif
    #endfunc

    def ViagemTeofilotoni(self):
        print('caminhoTeofilo')
        self.Hero,state, continueStory = self.caravan.Update()
        self.State = state
        if(continueStory):
            print("partiu teofilotoni")
        #endif
    #endfunc

    def Florianopolis(self):
        print('florianopolis')
    #endfunc
#endclass