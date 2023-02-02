# -*- coding: utf-8 -*-
import pygame
import Domain.Acao as Acao
import Domain.Arma as A
import Utils.JsonLoader as jsonL
import Interface.Img.Image as img


class Personagem:
    # Constructor
    def __init__(self, nome, classe):
        self.name = nome
        self.XP = 0
        self.lvl = 1
        self.classe = classe
        self.skills = {"str": 0, "agi": 0, "int": 0, "vit": 0}
        self.acoes = Acao.Acao()
        self.arma = A.Arma(
            "Arma desgastada", 2, "Ataque Especial da Arma Mais Fraca Do Jogo!!!", "arma0")
        self.magias = self.acoes.CriaMagias(self)
        self.Image = img.Image(self.GetImage(),300,450)

        if(self.classe.lower() == "guerreiro"):
            self.skills['str'] = 4
            self.skills['agi'] = 2
            self.skills['vit'] = 5
            self.skills["int"] = 2

        elif(self.classe.lower() == "arqueiro"):
            self.skills['str'] = 2
            self.skills['agi'] = 4
            self.skills['vit'] = 4
            self.skills["int"] = 3

        elif(self.classe.lower() == "mago"):
            self.skills['str'] = 1
            self.skills['agi'] = 2
            self.skills['vit'] = 3
            self.skills["int"] = 4
        else:
            print("Erro no construtor")
        # endif
        self.AtualizaStatus()
    # endfunc

    def GetImage(self):
        imagePath = jsonL.GetImagePath()
        return pygame.image.load(f'{imagePath}/Personagens/{self.classe.lower()}.png').convert_alpha() 

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
        self.HP = 10*self.skills["vit"]
        self.MP = 10*self.skills["int"]
        self.HPmax = 10*self.skills["vit"]
        self.MPmax = 10*self.skills["int"]
    # endfunc
