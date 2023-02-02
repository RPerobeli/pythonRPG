import pygame
from Interface import Inn
from Interface import DialogBox
from Interface import BattleWindow as bw
import copy as cp
import Interacoes as lib

#monstros = lib.CriaMonstros()
#armas = lib.CriaArmas()

def HistoriaIntro(screen,dialogBox,personagem):
    dialogBox.LoadImage()
    
    inn = Inn.Inn(screen,dialogBox, personagem)
    inn.InnDialog1()
    #battle1= bw.BattleWindow(screen,dialogBox,"quarto")
    #battle1.SetActors(personagem, lib.GetMonstro(monstros, "Cao infernal"))
    #battle1.Battle()
    


#endfunc