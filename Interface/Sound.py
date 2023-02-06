import pygame
from Utils import JsonLoader


class Sound:
    def __init__():
        FXDict = fxCreator()
        MusicDict = musicCreator()

def fxCreator():
    pygame.mixer.init()
    FXdictCreate ={}
    FXDictOpen = JsonLoader.GetSoundFXOrMusic("Sound")
    for key,values in FXDictOpen:
        FXAux = {key, pygame.mixer.Sound(values)}
        FXdictCreate.update(FXAux)
    return FXdictCreate

def musicCreator():
    pygame.mixer.init()
    musicDictCreate ={}
    musicDictOpen = JsonLoader.GetSoundFXOrMusic("Music")
    for key,values in musicDictOpen:
        MusicAux = {key, pygame.mixer.Sound(values)}
        musicDictCreate.update(MusicAux)
    return musicDictCreate

