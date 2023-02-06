#import Domain.Acao as Acao
import pygame
import Utils.JsonLoader as jsonL
import Interface.Img.Image as img


class Npc():
    # Constructor
    def __init__(self, nome):
        self.name = nome
        config = self.GetConfigFromList(nome)
        self.ImageMultiplier = config["ImageMultiplier"]
        auxImg =  self.GetImageByNpcName()
        self.Image = img.Image(auxImg,auxImg.get_width()*self.ImageMultiplier,auxImg.get_height()*self.ImageMultiplier)
    #endfunc

    def GetConfigFromList(self, name):
        npcConfig = jsonL.GetAllNpcs()
        for config in npcConfig:
            if(config["Nome"] == name):
                return config
    # endfunc

        
    def GetImageByNpcName(self):
        imagePath = jsonL.GetImagePath()
        image =  pygame.image.load(f'{imagePath}/Npc/{self.name}.png').convert_alpha() 
        if(image != None):
            return image
        else:
            return None
        #endif
    #endfunc

    def GetNome(self):
        return self.nome
    # endfunc
# endclass
