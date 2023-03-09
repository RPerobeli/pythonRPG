import pygame
import Utils.JsonLoader as jsonL

class Sound:
    def __init__(self):
        self.MusicVolumeDict = {}
        self.SFXVolumeDict = {}
        self.CurrentMusic = None
        self.CurrentSFX = None
        self.SoundPath = jsonL.GetSoundPath()
        self.FXDict = self.fxCreator()
        self.MusicDict = self.musicCreator()


    def fxCreator(self):
        pygame.mixer.init()
        FXdictCreate ={}
        FXDictOpen = jsonL.GetSoundFXOrMusic("Sound")
        for key, values in FXDictOpen.items():
            values = dict(values)
            FXAux = {key: pygame.mixer.Sound(f'{self.SoundPath}/{values["file"]}')}
            volumeAux = {key: values["volume"]}
            self.SFXVolumeDict.update(volumeAux)
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
            volumeAux = {key: values["volume"]}
            self.MusicVolumeDict.update(volumeAux)
            musicDictCreate.update(MusicAux)
        return musicDictCreate

    def PlayMusic(self, filename):
        self.CurrentMusic = self.MusicDict[f"{filename}"]
        self.CurrentMusic.set_volume(self.MusicVolumeDict[f"{filename}"])
        self.CurrentMusic.play(-1)
    #endfunc
    def StopMusic(self):
        self.CurrentMusic.stop()
    #endfunc

    def PlaySFX(self, filename):
        self.CurrentSFX = self.MusicDict[f"{filename}"]
        self.CurrentSFX.set_volume(self.MusicVolumeDict[f"{filename}"])
        self.CurrentSFX.play()
    #endfunc
    def StopSFX(self):
        self.CurrentSFX.stop()
    #endfunc
#endclass
