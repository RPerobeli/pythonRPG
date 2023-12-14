#import Domain.Acao as Acao
import pygame
import Utils.JsonLoader as jsonL
from Domain import Acao as Acao
import Domain.Arma as A
import Interface.Img.Image as img

class Monstro():
    # Constructor
    def __init__(self, nome, classe, isBoss):
        self.name = nome
        self.XP = 0
        self.SP = 0
        self.SPmax = 100
        self.lvl = 1
        self.classe = classe
        self.skills = {"str": 0, "agi": 0, "int": 0, "vit": 0, "sab":0}
        self.acoes = Acao.Acao()
        self.arma = A.Arma(
            "Arma desgastada", 2, "Ataque Especial da Arma Mais Fraca Do Jogo!!!", "arma0")
        self.magias = jsonL.GetSpells(self.classe)
        self.isMonstro = True
        self.isBoss = isBoss
        config = self.GetConfigFromList(nome)
        self.ImageMultiplier = config["ImageMultiplier"]
        auxImg =  self.GetImageByMonsterName()
        if(config["needFlip"] == "True"):
            auxImg = pygame.transform.flip(auxImg, True, False)
        #endif
        self.Image = img.Image(auxImg,auxImg.get_width()*self.ImageMultiplier,auxImg.get_height()*self.ImageMultiplier)
        self.Status = []
        
        if(self.classe.lower() == "guerreiro"):
            self.skills['str'] = 4
            self.skills['agi'] = 2
            self.skills['vit'] = 4
            self.skills["int"] = 2
            self.skills["sab"] = 2

        elif(self.classe.lower() == "arqueiro"):
            self.skills['str'] = 1
            self.skills['agi'] = 4
            self.skills['vit'] = 4
            self.skills["int"] = 3
            self.skills["sab"] = 3

        elif(self.classe.lower() == "mago"):
            self.skills['str'] = 2
            self.skills['agi'] = 2
            self.skills['vit'] = 4
            self.skills["int"] = 4
            self.skills["sab"] = 4
        else:
            print("Erro no construtor")
        # endif
        self.AtualizaStatus()
    #endfunc


    def GetConfigFromList(self, name):
        monsterConfig = jsonL.GetAllMonstersConfig()
        for config in monsterConfig:
            if(config["Nome"] == name):
                return config
    # endfunc

    def GetImageByMonsterName(self):
        imagePath = jsonL.GetImagePath()
        image =  pygame.image.load(f'{imagePath}/Monstros/{self.name}.png').convert_alpha() 
        if(image != None):
            return image
        else:
            return None
        #endif
    def GetClasse(self):
        return self.classe

    def GetSkills(self):
        return self.skills

    def GetNome(self):
        return self.nome
    # endfunc

    def SetClasse(self):
        self.classe = input("Digite sua classe:")
    # endfunc

    def SetNome(self):
        self.nome = input("Digite o nome do seu personagem:")
    # endfunc

    def AtualizaStatus(self):
        self.HP = 10*self.skills["vit"]+ 4*(self.lvl-1)
        self.MP = 10*self.skills["sab"]+ 4*(self.lvl-1)
        self.HPmax = 10*self.skills["vit"]+ 4*(self.lvl-1)
        self.MPmax = 10*self.skills["sab"]+ 4*(self.lvl-1)
    # endfunc

    def AutoLvl(self, level):
        lvl_old = self.lvl
        self.lvl = level
        skillPoints = self.lvl-lvl_old
        self.AutoLvlUpSKills(skillPoints)
    # endfunc

    def AutoLvlUpSKills(self, sPoints):
        vet = [0, 0, 0, 0, 0]
        if(self.classe.lower() == "guerreiro"):
            vet[0] = int(sPoints*0.4)
            vet[3] = int(sPoints*0.3)
            vet[2] = int(sPoints*0.1)
            vet[1] = int(sPoints*0.1)
            vet[4] = int(sPoints*0.1)
            self.skills["str"] += vet[0]
            self.skills["vit"] += vet[3]
            self.skills["int"] += vet[2]
            self.skills["agi"] += vet[1]
            self.skills["sab"] += vet[4]
            soma = sum(vet)
            extraPoints = sPoints - soma
            self.skills["str"] += extraPoints
        elif(self.classe.lower() == "arqueiro"):
            vet[0] = int(sPoints*0.1)
            vet[3] = int(sPoints*0.3)
            vet[2] = int(sPoints*0.1)
            vet[1] = int(sPoints*0.3)
            vet[4] = int(sPoints*0.2)
            self.skills["str"] += vet[0]
            self.skills["vit"] += vet[3]
            self.skills["int"] += vet[2]
            self.skills["agi"] += vet[1]
            self.skills["sab"] += vet[4]
            soma = sum(vet)
            extraPoints = sPoints - soma
            self.skills["agi"] += extraPoints

        elif(self.classe.lower() == "mago"):
            vet[0] = int(sPoints*0.1)
            vet[3] = int(sPoints*0.3)
            vet[2] = int(sPoints*0.3)
            vet[1] = int(sPoints*0.1)
            vet[4] = int(sPoints*0.2)
            self.skills["str"] += vet[0]
            self.skills["vit"] += vet[3]
            self.skills["int"] += vet[2]
            self.skills["agi"] += vet[1]
            self.skills["sab"] += vet[4]
            soma = sum(vet)
            extraPoints = sPoints - soma
            self.skills["int"] += extraPoints
        else:
            print("Erro na distribuição de skill points")
        self.AtualizaStatus()
    # endfunc

    def AdequaHP(self):
        # dobra o hp dos monstros pra ficar mais interessante
        if(self.isBoss == "True"):
            self.HP = (0.5*self.lvl+0.75)*self.HP
            self.MP = (0.5*self.lvl+0.75)*self.MP
            self.HPmax = (0.5*self.lvl+0.75)*self.HPmax
            self.MPmax = (0.5*self.lvl+0.75)*self.MPmax
        else:
            self.HP = (0.25*self.lvl+0.75)*self.HP
            self.MP = (0.25*self.lvl+0.75)*self.MP
            self.HPmax = (0.25*self.lvl+0.75)*self.HPmax
            self.MPmax = (0.25*self.lvl+0.75)*self.MPmax
        #se for boss final melhora mais ainda
        if(self.isBoss and self.name == "Metherax"):
            self.HP = 3*self.HP
            self.MP = 2*self.MP
            self.HPmax = 3*self.HPmax
            self.MPmax = 2*self.MPmax
        #endif
    # endfunc
    def AtualizaSpecialPoints(self, value):
        self.SP += value
        if(self.SP > self.SPmax):
            self.SP = self.SPmax
        #endif
    #endfunc
# endclass
