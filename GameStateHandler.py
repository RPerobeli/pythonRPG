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
from Interface.States import KrambeckMago
from Interface.States import SantosBom
from Interface.States import RetornoAdLArqueiro
from Interface.States import SagaFinal
from Interface.States import Good
from Interface.States import Neutral
from Interface.States import Evil
from Interface.States import Title as t
from Interface import TheEndWindow as End
from Interface import DialogBox
from Interface import BattleWindow as bw
from Utils import JsonLoader as jsonL
from Utils.ConstText import ClassesText
from Utils.ConstText import StatesText as txt
import copy as cp
import Interacoes as lib

class GameStateHandler:
    def __init__(self, screen):
        self.State = txt.Title
        self.Screen = screen
        self.Title = t.Title(self.Screen)
        self.DialogBox = DialogBox.DialogBox(self.Screen)
        self.Hero = None
        self.Monstros = lib.CreateMonsters()
        self.Armas = lib.CriaArmas()
        self.Npcs = lib.CreateNpcs()
        
    #endfunc

    def ManageState(self):
        if(self.State == txt.Title):
            self.IntroTitle()
        if(self.State == txt.Inn):
            self.Inn()
        if(self.State == txt.CaminhoTeofilo):
            self.ViagemTeofilotoni()
        if(self.State == txt.Caravana):
            self.Caravan()
        if(self.State == txt.Recursos):
            self.Recursos()
        if(self.State == txt.Florianopolis):
            self.Florianopolis()
        #endif
        if(self.State == txt.Juazeiro):
            self.Juazeiro()
        #endif
        if(self.State == txt.KrambeckMago):
            self.KrambeckMago()
        #endif
        if(self.State == txt.Teofilotoni):
            self.Teofilotoni()
        #endif
        if(self.State == txt.Curitiba):
            self.Curitiba()
        #endif
        if(self.State == txt.KrambeckArqueiro):
            self.KrambeckArqueiro()
        #endif
        if(self.State == txt.SantosBom):
            self.SantosBom()
        #endif
        if(self.State == txt.RetornoAdLArqueiro):
            self.RetornoAdLArqueiro()
        #endif
        if(self.State == txt.FelastusGuerreiro):
            self.Felastus()
        #endif
        if(self.State == txt.AcreArqueiro):
            self.Acre()
        #endif
        if(self.State == txt.Final):
            self.SagaFinal()
        #endif
        if(self.State == txt.Good):
            self.Good()
        #endif
        if(self.State == txt.Neutral):
            self.Neutral()
        #endif
        if(self.State == txt.Evil):
            self.Evil()
        #endif
        if(self.State == txt.Continue):
            self.ToBeContinued()
        #endif
        if(self.State == txt.TheEnd):
            self.End()
        #endif
    #endfunc

    #endfunc
    def IntroTitle(self):
        print(txt.Title)
        self.Title.RedrawWindow()
        self.Hero = self.Title.Update()
        if(self.Hero!=None):
            self.inn = Inn.Inn(self.Screen,self.DialogBox,self.Hero,self.Monstros, self.Npcs)
            self.State = txt.Inn
    #         self.krambeckMago = KrambeckMago.KrambeckMago(self.Screen,self.DialogBox,self.Hero,self.Monstros,self.Npcs,self.Armas)
    #         self.State = txt.KrambeckMago
    # #endfunc
    def Inn(self):
        print(txt.Inn)
        self.Hero,state, continueStory = self.inn.Update(txt.Inn)
        self.State = state
        if(continueStory):
            if(self.Hero.classe.lower() == ClassesText.Mago):
                self.caravan = Caravan.Caravan(self.Screen,self.DialogBox,self.Hero,self.Monstros,self.Npcs)
            elif(self.Hero.classe.lower() == ClassesText.Guerreiro):
                self.caminhoTeofilo = ViagemTeofilotoni.ViagemTeofilotoni(self.Screen,self.DialogBox,self.Hero,self.Monstros,self.Npcs)
            elif(self.Hero.classe.lower() == ClassesText.Arqueiro):
                self.recursos = Recursos.Recursos(self.Screen,self.DialogBox,self.Hero,self.Monstros,self.Npcs,self.Armas)
            #endif
        #endif
    #endfunc

    def Caravan(self):
        print(txt.Caravana)
        self.Hero,state, continueStory = self.caravan.Update(txt.Caravana)
        self.State = state
        if(continueStory):
            self.floripa = Florianopolis.Florianopolis(self.Screen,self.DialogBox,self.Hero,self.Monstros,self.Npcs,self.Armas)
        #endif
    #endfunc

    def ViagemTeofilotoni(self):
        print(txt.CaminhoTeofilo)
        self.Hero,state, continueStory = self.caminhoTeofilo.Update(txt.CaminhoTeofilo)
        self.State = state
        if(continueStory):
            self.teofilotoni = Teofilotoni.Teofilotoni(self.Screen,self.DialogBox,self.Hero,self.Monstros,self.Npcs,self.Armas)
        #endif
    #endfunc

    def Florianopolis(self):
        print(txt.Florianopolis)
        self.Hero,state, continueStory = self.floripa.Update(txt.Florianopolis)
        self.State = state
        if(continueStory):
            self.krambeckMago = KrambeckMago.KrambeckMago(self.Screen,self.DialogBox,self.Hero,self.Monstros,self.Npcs,self.Armas)
        #endif
    #endfunc

    def KrambeckMago(self):
        print(txt.KrambeckMago)
        self.Hero,state, continueStory = self.krambeckMago.Update(txt.KrambeckMago)
        self.State = state
        if(continueStory):
            self.juazeiro = Continue.Continue(self.Screen)
        #endif
    #endfunc

    def Juazeiro(self):
        print(txt.Juazeiro)
        self.Hero,state, continueStory = self.juazeiro.Update(txt.Juazeiro)
        self.State = state
        if(continueStory):
            self.tobecontinued = Continue.Continue(self.Screen)
        #endif
    #endfunc

    def Teofilotoni(self):
        print(txt.Teofilotoni)
        self.Hero,state, continueStory = self.teofilotoni.Update(txt.Teofilotoni)
        self.State = state
        if(continueStory):
            self.tobecontinued = Continue.Continue(self.Screen)
        #endif
    #endfunc

    def Curitiba(self):
        print(txt.Curitiba)
        self.Hero,state, continueStory = self.curitiba.Update(txt.Curitiba)
        self.State = state
        if(continueStory):
            self.krambeckArqueiro = KrambeckArqueiro.KrambeckArqueiro(self.Screen,self.DialogBox,self.Hero,self.Monstros,self.Npcs,self.Armas)
        #endif
    #endfunc

    def Recursos(self):
        print(txt.Recursos)
        self.Hero,state, continueStory = self.recursos.Update(txt.Recursos)
        self.State = state
        if(continueStory):
            self.curitiba = Curitiba.Curitiba(self.Screen,self.DialogBox,self.Hero,self.Monstros,self.Npcs,self.Armas)
        #endif
    #endfunc

    def KrambeckArqueiro(self):
        print(txt.KrambeckArqueiro)
        self.Hero,state, continueStory = self.krambeckArqueiro.Update(txt.KrambeckArqueiro)
        self.State = state
        if(continueStory):
            self.santosBom = SantosBom.SantosBom(self.Screen,self.DialogBox,self.Hero,self.Monstros,self.Npcs,self.Armas)
        #endif
    #endfunc
    
    def SantosBom(self):
        print(txt.SantosBom)
        self.Hero,state, continueStory = self.santosBom.Update(txt.SantosBom)
        self.State = state
        if(continueStory):
            self.retornoAdLArqueiro = RetornoAdLArqueiro.RetornoAdLArqueiro(self.Screen,self.DialogBox,self.Hero,self.Monstros,self.Npcs,self.Armas)
        #endif
    #endfunc

    def SagaFinal(self):
        print(txt.Final)
        self.Hero,state, continueStory = self.sagaFinal.Update(txt.Final)
        self.State = state
        if(continueStory):
            if(self.State == txt.Good):
                self.good = Good.Good(self.Screen,self.DialogBox,self.Hero,self.Monstros,self.Npcs,self.Armas)
            if(self.State == txt.Neutral):
                self.neutral = Neutral.Neutral(self.Screen,self.DialogBox,self.Hero,self.Monstros,self.Npcs,self.Armas)
            if(self.State == txt.Evil):
                self.evil = Evil.Evil(self.Screen,self.DialogBox,self.Hero,self.Monstros,self.Npcs,self.Armas)
        #endif
    #endfunc

    def RetornoAdLArqueiro(self):
        print('RetornoAdLArqueiro')
        self.Hero,state, continueStory = self.retornoAdLArqueiro.Update('RetornoAdLArqueiro')
        self.State = state
        if(continueStory):
            self.sagaFinal = SagaFinal.SagaFinal(self.Screen,self.DialogBox,self.Hero,self.Monstros,self.Npcs,self.Armas)
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

    def Good(self):
        print('good')
        self.Hero,state, continueStory = self.good.Update('good')
        self.State = state
        if(continueStory):
            self.theEnd = End.TheEndWindow(self.Screen)
        #endif
    #endfunc

    def Neutral(self):
        print('neutral')
        self.Hero,state, continueStory = self.neutral.Update('neutral')
        self.State = state
        if(continueStory):
            self.theEnd = End.TheEndWindow(self.Screen)
        #endif
    #endfunc

    def Evil(self):
        print('evil')
        self.Hero,state, continueStory = self.evil.Update('evil')
        self.State = state
        if(continueStory):
            self.theEnd = End.TheEndWindow(self.Screen)
        #endif
    #endfunc
    
    def ToBeContinued(self):
        print('ToBeContinued')
        state = self.tobecontinued.Update('ToBeContinued')
        self.State = state
    #endfunc
    def End(self):
        print('TheEnd')
        state = self.theEnd.End()
        self.State = state
    #endfunc
#endclass