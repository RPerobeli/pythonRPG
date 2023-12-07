import pygame
from Interface.States import Inn
from Interface.States import Caravan
from Interface.States import Florianopolis
from Interface.States import ViagemTeofilotoni
from Interface.States import Teofilotoni
from Interface.States import Recursos
from Interface.States import Curitiba
from Interface.States import Continue
from Interface.States import KrambeckArqueiro
from Interface.States import SantosBom
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
        if(self.State == "Recursos"):
            self.Recursos()
        if(self.State == "Florianopolis"):
            self.Florianopolis()
        #endif
        if(self.State == "Teofilotoni"):
            self.Teofilotoni()
        #endif
        if(self.State == "Curitiba"):
            self.Curitiba()
        #endif
        if(self.State == "KrambeckArqueiro"):
            self.KrambeckArqueiro()
        #endif
        if(self.State == "SantosBom"):
            self.SantosBom()
        #endif
        if(self.State == "Felastus"):
            self.Felastus()
        #endif
        if(self.State == "Acre"):
            self.Acre()
        #endif
        if(self.State == "ToBeContinued"):
            self.ToBeContinued()
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
            # self.krambeckArqueiro = KrambeckArqueiro.KrambeckArqueiro(self.Screen,self.DialogBox,self.Hero,self.Monstros,self.Npcs,self.Armas)
            # self.State = "KrambeckArqueiro"

    #endfunc
    def Inn(self):
        print("inn")
        # self.inn.RedrawWindow()
        self.Hero,state, continueStory = self.inn.Update("inn")
        self.State = state
        if(continueStory):
            if(self.Hero.classe.lower() == "mago"):
                self.caravan = Caravan.Caravan(self.Screen,self.DialogBox,self.Hero,self.Monstros,self.Npcs)
            elif(self.Hero.classe.lower() == "guerreiro"):
                self.caminhoTeofilo = ViagemTeofilotoni.ViagemTeofilotoni(self.Screen,self.DialogBox,self.Hero,self.Monstros,self.Npcs)
            elif(self.Hero.classe.lower() == "arqueiro"):
                self.recursos = Recursos.Recursos(self.Screen,self.DialogBox,self.Hero,self.Monstros,self.Npcs,self.Armas)
            #endif
        #endif
    #endfunc

    def Caravan(self):
        print('caravana')
        self.Hero,state, continueStory = self.caravan.Update("caravana")
        self.State = state
        if(continueStory):
            self.floripa = Florianopolis.Florianopolis(self.Screen,self.DialogBox,self.Hero,self.Monstros,self.Npcs,self.Armas)
        #endif
    #endfunc

    def ViagemTeofilotoni(self):
        print('caminhoTeofilo')
        self.Hero,state, continueStory = self.caminhoTeofilo.Update('caminhoTeofilo')
        self.State = state
        if(continueStory):
            self.teofilotoni = Teofilotoni.Teofilotoni(self.Screen,self.DialogBox,self.Hero,self.Monstros,self.Npcs,self.Armas)
        #endif
    #endfunc

    def Florianopolis(self):
        print('Florianopolis')
        self.Hero,state, continueStory = self.floripa.Update('Florianopolis')
        self.State = state
        if(continueStory):
            self.tobecontinued = Continue.Continue(self.Screen)
        #endif
    #endfunc

    def Teofilotoni(self):
        print('Teofilotoni')
        self.Hero,state, continueStory = self.teofilotoni.Update('Teofilotoni')
        self.State = state
        if(continueStory):
            self.tobecontinued = Continue.Continue(self.Screen)
        #endif
    #endfunc

    def Curitiba(self):
        print('Curitiba')
        self.Hero,state, continueStory = self.curitiba.Update('Curitiba')
        self.State = state
        if(continueStory):
            self.krambeckArqueiro = KrambeckArqueiro.KrambeckArqueiro(self.Screen,self.DialogBox,self.Hero,self.Monstros,self.Npcs,self.Armas)
        #endif
    #endfunc

    def Recursos(self):
        print('Recursos')
        self.Hero,state, continueStory = self.recursos.Update('Recursos')
        self.State = state
        if(continueStory):
            self.curitiba = Curitiba.Curitiba(self.Screen,self.DialogBox,self.Hero,self.Monstros,self.Npcs,self.Armas)
        #endif
    #endfunc

    def KrambeckArqueiro(self):
        print('KrambeckArqueiro')
        self.Hero,state, continueStory = self.krambeckArqueiro.Update('KrambeckArqueiro')
        self.State = state
        if(continueStory):
            self.santosBom = SantosBom.SantosBom(self.Screen,self.DialogBox,self.Hero,self.Monstros,self.Npcs,self.Armas)
        #endif
    #endfunc
    
    def SantosBom(self):
        print('SantosBom')
        self.Hero,state, continueStory = self.santosBom.Update('SantosBom')
        self.State = state
        if(continueStory):
            self.tobecontinued = Continue.Continue(self.Screen)
        #endif
    #endfunc

    def Felastus(self):
        print('Felastus')
        self.Hero,state, continueStory = self.teofilotoni.Update('Felastus')
        self.State = state
        if(continueStory):
            print("...")
        #endif
    #endfunc
    def Acre(self):
        print('Acre')
        self.Hero,state, continueStory = self.teofilotoni.Update('Acre')
        self.State = state
        if(continueStory):
            print("...")
        #endif
    #endfunc
    
    def ToBeContinued(self):
        print('ToBeContinued')
        state = self.tobecontinued.Update('ToBeContinued')
        self.State = state
    #endfunc
#endclass