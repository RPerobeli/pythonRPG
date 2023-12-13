import random as rnd
from Domain import Magia as m
import Interacoes as lib
import os


class Acao:

    def Atk(self, personagem, atkType, target, magiaEscolhida = None):  # Ribamar == turnCounter
        self.isCrit = False
        danoBaseEspecial = 30
        if(personagem.classe.lower() == "guerreiro"):
            if(atkType == 1):
                dano = 2*personagem.skills["str"] + personagem.arma.danoBase*2 + personagem.skills["agi"]
                dano = int(dano)
                dano = self.AcertoCritico(dano, personagem)
                print(personagem.name + " causou "+str(dano) + " de dano!")
                target.HP -= dano
                personagem.AtualizaSpecialPoints(dano/2)
                return dano
            elif(atkType == 2):
                if(personagem.SP < 100):
                    return -2
                else:
                    dano = danoBaseEspecial + personagem.arma.danoBase*(1.5*personagem.skills["str"]+personagem.skills["agi"])
                    dano = int(dano)
                    dano = self.AcertoCritico(dano, personagem)
                    if(not personagem.isMonstro):
                        print(personagem.arma.textoAtkEspecial)
                    # endif
                    print(personagem.name + " causou "+str(dano) + " de dano!")
                    target.HP -= dano
                    personagem.SP = 0
                    return dano
                #endif
            elif(atkType == 3):
                if (lib.NaoTemMana(personagem, magiaEscolhida["Cost"])):
                    return -1
                else:
                    dano = 2 * \
                        personagem.skills["int"] + \
                        personagem.skills["str"] + magiaEscolhida["BaseDamage"]
                    dano = int(dano)
                    dano = self.AcertoCritico(dano, personagem)
                    print(personagem.name + " causou "+str(dano) + " de dano!")
                    target.HP -= dano
                    personagem.MP -= magiaEscolhida["Cost"]
                    personagem.AtualizaSpecialPoints(dano/2)
                    return dano
                # endif
            elif(atkType == 4):
                self.Curar(personagem)
            elif(atkType == 69):
                self.Hack(personagem)
                dano = 696969
                target.HP -= dano
            else:
                print("Erro no ataque de guerreiro")
            # endif
        elif(personagem.classe.lower() == "arqueiro"):
            if(atkType == 1):
                dano = 2*personagem.skills["agi"] + personagem.arma.danoBase*2 + personagem.skills["int"]
                dano = int(dano)
                dano = self.AcertoCritico(dano, personagem)
                print(personagem.name + " causou "+str(dano) + " de dano!")
                target.HP -= dano
                personagem.AtualizaSpecialPoints(dano/2)
                return dano
            elif(atkType == 2):
                if(personagem.SP < 100):
                    return -2
                else:
                    dano = danoBaseEspecial + personagem.arma.danoBase*(1.5*personagem.skills["agi"]+personagem.skills["int"])
                    dano = int(dano)
                    dano = self.AcertoCritico(dano, personagem)
                    print(personagem.arma.textoAtkEspecial)
                    print()
                    print(personagem.name + " causou "+str(dano) + " de dano!")
                    target.HP -= dano
                    personagem.SP = 0
                    return dano
                # endif
            elif(atkType == 3):
                if (lib.NaoTemMana(personagem, magiaEscolhida["Cost"])):
                    return -1
                else:
                    dano = personagem.skills["int"] + \
                        2*personagem.skills["agi"] + magiaEscolhida["BaseDamage"]
                    dano = self.AcertoCritico(dano, personagem)
                    dano = int(dano)
                    print(personagem.name + " causou "+str(dano) + " de dano!")
                    target.HP -= dano
                    personagem.MP -= magiaEscolhida["Cost"]
                    personagem.AtualizaSpecialPoints(dano/2)
                    return dano
                # endif
            elif(atkType == 4):
                self.Curar(personagem)
            elif(atkType == 69):
                self.Hack(personagem)
                dano = 696969
                target.HP -= dano
            else:
                print("Erro no ataque de arqueiro")
            # endif
        elif(personagem.classe.lower() == "mago"):
            if(atkType == 1):
                dano = 2*personagem.skills["int"] + personagem.arma.danoBase*2 + personagem.skills["str"]
                dano = int(dano)
                dano = self.AcertoCritico(dano, personagem)
                print(personagem.name + " causou "+str(dano) + " de dano!")
                target.HP -= dano
                personagem.AtualizaSpecialPoints(dano/2)
                return dano
            elif(atkType == 2):
                if(personagem.SP < 100):
                    return -2
                else:
                    dano = danoBaseEspecial + personagem.arma.danoBase*(1.5*personagem.skills["int"]+personagem.skills["str"])
                    dano = int(dano)
                    dano = self.AcertoCritico(dano, personagem)
                    print(personagem.arma.textoAtkEspecial)
                    print()
                    print(personagem.name + " causou "+str(dano) + " de dano!")
                    target.HP -= dano
                    personagem.SP = 0
                    return dano
                # endif
            elif(atkType == 3):
                if (lib.NaoTemMana(personagem, magiaEscolhida["Cost"])):
                    print("Mana insuficiente.")
                else:
                    dano = personagem.arma.danoBase * \
                        personagem.skills["int"] + \
                        magiaEscolhida["BaseDamage"]  
                    dano = int(dano)
                    dano = self.AcertoCritico(dano, personagem)
                    print(personagem.name+" causou "+str(dano) + " de dano!")
                    target.HP -= dano
                    personagem.MP -= magiaEscolhida["Cost"]
                    personagem.AtualizaSpecialPoints(dano/2)
                    return dano
                # endif
            elif(atkType == 4):
                self.Curar(personagem)
            elif(atkType == 69):
                self.Hack(personagem)
                dano = 696969
                target.HP -= dano
            else:
                print("Erro no ataque de mago")
            # endif
        else:
            print("Erro no ataque, classe inválida")
        # endif
    # endfunc

    def Curar(self, personagem):
        baseHeal = 5
        multiplicadorCura = rnd.randint(1,2)/10.0
        multiplicadorCuraMonstro = rnd.randint(2,4)/10.0
        if(personagem.isMonstro):
            personagem.HP += int(multiplicadorCuraMonstro*personagem.HPmax)
            personagem.MP += int(multiplicadorCuraMonstro*personagem.MPmax)
        else:
            personagem.HP += int(baseHeal + multiplicadorCura*personagem.HPmax + \
                personagem.skills["str"] + personagem.skills["agi"] + personagem.skills["int"])
            personagem.MP += int(0.4*personagem.MPmax)
        # endif
        print("Regenerou vida e mana")
        if(personagem.HP > personagem.HPmax):
            personagem.HP = personagem.HPmax
        if(personagem.MP > personagem.MPmax):
            personagem.MP = personagem.MPmax
        # endif
    # endfunc

    def Hack(self, personagem):
        personagem.HP = personagem.HPmax
        personagem.MP = personagem.MPmax

    def Opcoes(self, Personagem):
        #lib.LimpaConsole()
        print("[Narrador]: Sua vez de atacar, escolha uma das opções.")
        atkType = input(
            "1 - Ataque Físico \n2 - Ataque especial  \n3 - Habilidades \n4 - Passar turno (Recupera parte de HP e MP)\n5 - Verificar Status\n6 - Olhar Inventário\n")
        if(atkType == ''):
            print("Ataque inválido, você tem demência? Tente de novo.")
            atkType = self.Opcoes(Personagem)
        # endif
        atkType = int(atkType)
        if(atkType != 1 and atkType != 2 and atkType != 3 and atkType != 4 and atkType != 5 and atkType != 6 and atkType != 69):
            print("Ataque inválido, você tem demência? Tente de novo.")
            atkType = self.Opcoes(Personagem)
        elif(atkType == 5):
            print("Status de "+Personagem.name +
                  ": "+str(Personagem.GetSkills()))
            print("Atk arma: "+str(Personagem.arma.danoBase) +
                  "   Xp: "+str(Personagem.XP))
            atkType = self.Opcoes(Personagem)
        elif(atkType == 6):
            Personagem.bag.ShowBag()
            atkType = self.Opcoes(Personagem)
        else:
            return atkType
        # endif
        return atkType
    # endfunc

    def AcertoCritico(self, dano, personagem):
        crit = rnd.randint(1, 5)
        if(crit == 1):
            self.isCrit = True
            print("ACERTO CRÍTICO!!!")
            if(personagem.isMonstro):
                return (int((1.1+(0.1*personagem.lvl))*dano))
            # endif
            return (2*dano)
        else:
            return(dano)
        # endif
    # endfunc

    def TipoAtk(self, monstro):
        monster_atkType = 1
        if(monstro.classe == "mago"):
            monster_atkType = 3
        # endif
        if(monstro.HP < 0.5*monstro.HPmax):
            if(rnd.randint(0, 2) == 1):
                monster_atkType = 4
            # endif
        # endif
        return monster_atkType
    # endfunc

    def SelectMagia(self, personagem):
        cont = 0
        print("Essas são suas magias parça:")
        for magia in personagem.magias:
            if(magia.name == "erro"):
                continue
            # endif
            if(magia.lvl <= personagem.lvl):
                cont += 1
                print(str(cont) + ": " + magia.name + " - " + str(magia.cost) + "MP" )
            # endif
        # endfor
        try:
            resp = int(input("Qual magia deseja usar?\n"))
        except:
            resp = 0
        # endtry
        if(resp <= 0 or resp > cont):
            print("vai se fuder QA")
            lib.LimpaConsole()
            magiaSelecionada = self.SelectMagia(personagem)
            if(magiaSelecionada != None):
                return magiaSelecionada
            # endif
        else:
            return personagem.magias[resp]
        # endif
    # endfunc

    def SelectMagiaMonstro(self, personagem):
        cont = 0
        magiasSelecionaveis = []
        for magia in personagem.magias:
            if(magia.name == "erro"):
                continue
            # endif
            if(magia.lvl <= personagem.lvl):
                cont += 1
                print(str(cont) + ": " + magia.name + "\n")
                magiasSelecionaveis.append(magia)
            # endif
        # endfor
        resp = rnd.randint(0, len(magiasSelecionaveis))
        return magiasSelecionaveis[resp]
    # endfunc

    def SelectMonsterSpell(self, personagem):
        cont = 0
        magiasSelecionaveis = []
        for magia in personagem.magias:
            if(magia["Lvl"] <= personagem.lvl):
                cont += 1
                magiasSelecionaveis.append(magia)
            # endif
        # endfor
        resp = rnd.randint(0, len(magiasSelecionaveis))
        return magiasSelecionaveis[resp]
    # endfunc

    def CriaMagias(self, Personagem):
        if(Personagem.classe.lower() == 'guerreiro'):
            arq = open("Arquivostxt/MagiasGuerreiro.txt", 'r')
        elif(Personagem.classe.lower() == 'arqueiro'):
            arq = open("Arquivostxt/MagiasArqueiro.txt", 'r')
        elif(Personagem.classe.lower() == 'mago'):
            arq = open("Arquivostxt/MagiasMago.txt", 'r')
        else:
            print("que porra tu ta fazendo da vida?")
        # endif
        livroMagias = [m.Magia("erro", 0, 0, 0)]
        for linha in arq:
            valores = linha.split(',')
            livroMagias.append(m.Magia(valores[0], int(
                valores[1]), int(valores[2]), int(valores[3].strip())))
        return livroMagias
# endclass
