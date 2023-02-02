import pygame
from Interface import Inn
from Interface import DialogBox



def HistoriaIntro(screen,dialogBox,personagem):
    dialogBox.LoadImage()
    
    inn = Inn.Inn(screen,dialogBox, personagem)
    inn.InnDialog1()

#endfunc