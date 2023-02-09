import Domain.Personagem as personagem
import Domain.Bag as B
import Utils.JsonLoader as jsonL


class Heroi(personagem.Personagem):
    # Constructor
    def __init__(self, nome, classe):
        super().__init__(nome, classe)
        self.bag = B.Bag()
        self.bag.InserirArma(self.arma)
        self.magias = jsonL.GetSpells(self.classe)
        self.isMonstro = False
    # endFunc

    def SetArma(self, WeaponAtk, WeaponName):
        self.arma.danoBase = WeaponAtk
        self.arma.nome = WeaponName
    # endfunc

    def LvlUP(self):
        self.lvl += 1
        print("Você chegou ao NIVEL " + str(self.lvl) + "!")
        skill = input(
            "Selecione onde alocar seu ponto (força, vitalidade, agilidade ou inteligencia): ")
        if(skill.lower() == "forca" or skill.lower() == "força"):
            self.skills["str"] += 1
        elif(skill.lower() == "agilidade"):
            self.skills["agi"] += 1
        elif(skill == "inteligencia" or skill.lower() == "inteligência"):
            self.skills["int"] += 1
        elif(skill.lower() == "vitalidade"):
            self.skills["vit"] += 1
        else:
            print("Atributo inválido, digite novamente")
            self.lvl -= 1
            self.LvlUP()
        self.XP -= 100
        self.AtualizaStatus()
    # endfunc
# endClass
