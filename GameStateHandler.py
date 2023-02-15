import pygame
from Interface.States import Inn
from Interface.States import Caravan
from Interface.States import Florianopolis
from Interface.States import ViagemTeofilotoni
from Interface.States import Teofilotoni
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
        if(self.State == "Teofilotoni"):
            self.Teofilotoni()
        #endif
    #endfunc

    #endfunc
    def IntroTitle(self):
        print("intro_title")
        self.Title.RedrawWindow()
        self.Hero = self.Title.Update()
        if(self.Hero!=None):
            # self.inn = Inn.Inn(self.Screen,self.DialogBox,self.Hero,self.Monstros, self.Npcs)
            # self.State = "inn"
            self.teofilotoni = Teofilotoni.Teofilotoni(self.Screen,self.DialogBox,self.Hero,self.Monstros,self.Npcs,self.Armas)
            self.State = "Teofilotoni"
    #endfunc
    def Inn(self):
        print("inn")
        self.inn.RedrawWindow()
        self.Hero,state, continueStory = self.inn.Update()
        self.State = state
        if(continueStory):
            if(self.Hero.classe.lower() == "mago"):
                self.caravan = Caravan.Caravan(self.Screen,self.DialogBox,self.Hero,self.Monstros,self.Npcs)
            elif(self.Hero.classe.lower() == "guerreiro"):
                self.caminhoTeofilo = ViagemTeofilotoni.ViagemTeofilotoni(self.Screen,self.DialogBox,self.Hero,self.Monstros,self.Npcs)
            elif(self.Hero.classe.lower() == "arqueiro"):
                self.caravan = Caravan.Caravan(self.Screen,self.DialogBox,self.Hero,self.Monstros,self.Npcs)
            #endif
        #endif
    #endfunc

    def Caravan(self):
        print('caravana')
        self.Hero,state, continueStory = self.caravan.Update()
        self.State = state
        if(continueStory):
            self.floripa = Florianopolis.Florianopolis(self.Screen,self.DialogBox,self.Hero,self.Monstros,self.Npcs,self.Armas)
        #endif
    #endfunc

    def ViagemTeofilotoni(self):
        print('caminhoTeofilo')
        self.Hero,state, continueStory = self.caminhoTeofilo.Update()
        self.State = state
        if(continueStory):
            self.teofilotoni = Teofilotoni.Teofilotoni(self.Screen,self.DialogBox,self.Hero,self.Monstros,self.Npcs,self.Armas)
        #endif
    #endfunc

    def Florianopolis(self):
        print('Florianopolis')
        self.Hero,state, continueStory = self.floripa.Update()
        self.State = state
        if(continueStory):
            print("partiu krambeck ou coliseu")
        #endif
    #endfunc

    def Teofilotoni(self):
        print('Teofilotoni')
        self.Hero,state, continueStory = self.teofilotoni.Update()
        self.State = state
        if(continueStory):
            print("partiu coliseu ou acre")
        #endif
    #endfunc
#endclass