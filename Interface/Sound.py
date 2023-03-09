import pygame
import Utils.JsonLoader as jsonL

class Sound:
    def __init__(self):
        self.SoundPath = jsonL.GetSoundPath()
        self.FXDict = self.fxCreator()
        self.MusicDict = self.musicCreator()


    def fxCreator(self):
        pygame.mixer.init()
        FXdictCreate ={}
        FXDictOpen = jsonL.GetSoundFXOrMusic("Sound")
        for key, values in FXDictOpen.items():
            FXAux = {key: pygame.mixer.Sound(f'{self.SoundPath}/{values}')}
            FXdictCreate.update(FXAux)
        #endfor
        return FXdictCreate

    def musicCreator(self):
        pygame.mixer.init()
        musicDictCreate ={}
        musicDictOpen = jsonL.GetSoundFXOrMusic("Music")
        for key,values in musicDictOpen.items():
            values = dict(values)
            MusicAux = {key : pygame.mixer.Sound(f'{self.SoundPath}/{values["file"]}')}
            musicDictCreate.update(MusicAux)
        return musicDictCreate

    def Play(self, filename):
        music = self.MusicDict[f"{filename}"]
        music.set_volume(self.MusicDict[f"{filename}"]["volume"])
        music.play()
    #endfunc
#endclass
