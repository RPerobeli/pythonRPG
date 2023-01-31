import Domain.Acao as Acao
import Domain.Arma as A


class Monstro():
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
        self.isMonstro = True

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
            #self.atk = 4

        else:
            print("Erro no construtor")
        # endif
        self.AtualizaStatus()
    # endfunc

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

    def AutoLvl(self, level):
        lvl_old = self.lvl
        self.lvl = level
        skillPoints = self.lvl-lvl_old
        self.AutoLvlUpSKills(skillPoints)
        # TODO: ESCALAR BALANCEADAMENTE O ATK DO MONSTRO
    # endfunc

    def AutoLvlUpSKills(self, sPoints):
        vet = [0, 0, 0, 0]
        if(self.classe.lower() == "guerreiro"):
            vet[0] = int(sPoints*0.4)
            vet[3] = int(sPoints*0.3)
            vet[2] = int(sPoints*0.1)
            vet[1] = int(sPoints*0.2)
            self.skills["str"] += vet[0]
            self.skills["vit"] += vet[3]
            self.skills["int"] += vet[2]
            self.skills["agi"] += vet[1]
            soma = sum(vet)
            extraPoints = sPoints - soma
            self.skills["str"] += extraPoints
        elif(self.classe.lower() == "arqueiro"):
            vet[0] = int(sPoints*0.2)
            vet[3] = int(sPoints*0.4)
            vet[2] = int(sPoints*0.2)
            vet[1] = int(sPoints*0.2)
            self.skills["str"] += vet[0]
            self.skills["vit"] += vet[3]
            self.skills["int"] += vet[2]
            self.skills["agi"] += vet[1]
            soma = sum(vet)
            extraPoints = sPoints - soma
            self.skills["agi"] += extraPoints

        elif(self.classe.lower() == "mago"):
            vet[0] = int(sPoints*0.1)
            vet[3] = int(sPoints*0.2)
            vet[2] = int(sPoints*0.4)
            vet[1] = int(sPoints*0.3)
            self.skills["str"] += vet[0]
            self.skills["vit"] += vet[3]
            self.skills["int"] += vet[2]
            self.skills["agi"] += vet[1]
            soma = sum(vet)
            extraPoints = sPoints - soma
            self.skills["int"] += extraPoints
        else:
            print("Erro na distribuição de skill points")
        self.AtualizaStatus()
    # endfunc

    def AdequaHP(self):
        # dobra o hp dos monstros pra ficar mais interessante
        self.HP = (0.25*self.lvl+0.75)*self.HP
        self.MP = (0.25*self.lvl+0.75)*self.MP
        self.HPmax = (0.25*self.lvl+0.75)*self.HPmax
        self.MPmax = (0.25*self.lvl+0.75)*self.MPmax
    # endfunc
# endclass