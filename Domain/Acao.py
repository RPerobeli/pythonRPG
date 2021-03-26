import random as rnd
class Acao:
    
    def Atk(self, personagem, atkType, target):
        if(personagem.classe.lower() == "guerreiro"):
            if(atkType == 1):
                dano = personagem.arma.danoBase*personagem.skills["str"] + 2*personagem.skills["agi"]
                dano = self.AcertoCritico(dano)
                print(personagem.name+ " causou "+str(dano)+ " de dano!")
                target.HP -= dano
            elif(atkType == 2):
                dano = 2*personagem.arma.danoBase*personagem.skills["str"] + personagem.skills["vit"]
                dano = self.AcertoCritico(dano)
                print(personagem.name+ " causou "+str(dano)+ " de dano!")
                target.HP -= dano
                personagem.HP -= 0.2*personagem.HPmax
            elif(atkType == 3):
                dano = 2*personagem.skills["int"]+ personagem.skills["str"]
                dano = self.AcertoCritico(dano)
                print(personagem.name+ " causou "+str(dano)+ " de dano!")
                target.HP -= dano 
                personagem.MP -= 0.2*personagem.MPmax
            elif(atkType == 4):  
                self.Curar(personagem)              
            else:
                print("Erro no ataque de guerreiro")
            #endif
        elif(personagem.classe.lower() == "arqueiro"):
            if(atkType == 1):
                dano =  2*personagem.skills["str"] + personagem.arma.danoBase*personagem.skills["agi"]
                dano = self.AcertoCritico(dano)
                print(personagem.name+ " causou "+str(dano)+ " de dano!")
                target.HP -= dano 
            elif(atkType == 2):
                dano =2*personagem.arma.danoBase*personagem.skills["agi"]
                dano = self.AcertoCritico(dano)
                print(personagem.name+ " causou "+str(dano)+ " de dano!")
                target.HP -= dano 
                personagem.MP -= 0.2*personagem.MPmax
            elif(atkType == 3):
                dano = 2*personagem.skills["int"]+ personagem.skills["agi"] #CHAMAR FUNCAO DE MAGIAS
                dano = self.AcertoCritico(dano)
                print(personagem.name+ " causou "+str(dano)+ " de dano!")
                target.HP -= dano
            elif(atkType == 4):
                self.Curar(personagem)
            else:
                print("Erro no ataque de arqueiro")
            #endif
        elif(personagem.classe.lower() == "mago"):
            if(atkType == 1):
                dano = 2*personagem.skills["int"] + 1*personagem.skills["str"]
                dano = self.AcertoCritico(dano)
                print(personagem.name+ " causou "+str(dano)+ " de dano!")
                target.HP -= dano
            elif(atkType == 2):
                dano = 2*personagem.arma.danoBase*personagem.skills["int"]
                dano = self.AcertoCritico(dano)
                print(personagem.name+ " causou "+str(dano)+ " de dano!")
                target.HP -= dano
                personagem.MP -= 0.5*personagem.MPmax
            elif(atkType == 3):
                dano = personagem.arma.danoBase*personagem.skills["int"] #CHAMAR FUNCAO DE MAGIAS
                dano = self.AcertoCritico(dano)
                print(personagem.name+" causou "+str(dano)+ " de dano!")
                target.HP -= dano
                personagem.MP -= 0.1*personagem.MPmax
            elif(atkType == 4):
                self.Curar(personagem)
            else:
                print("Erro no ataque de mago")
            #endif
        else:
            print("Erro no ataque, classe inválida")
        #endif
    #endfunc

    def Curar(self, personagem):
        personagem.HP += 0.25*personagem.HPmax
        personagem.MP += 0.25*personagem.MPmax
        if(personagem.HP > personagem.HPmax):
            personagem.HP = personagem.HPmax
        if(personagem.MP > personagem.MPmax):
            personagem.MP = personagem.MPmax
        #endif
    #endfunc

    def Opcoes(self, Personagem):
        input("[enter]")
        print("[Narrador]: Sua vez de atacar, escolha uma das opções.")
        atkType = int(input("1 - Ataque Físico \n2 - Ataque especial  \n3 - Ataque mágico \n4 - Passar turno (Recupera parte de HP e MP)\n5 - Verificar Status\n6 - Olhar Inventário"))
        if(atkType != 1 and atkType != 2 and atkType != 3 and atkType != 4 and atkType != 5 and atkType != 6):
            print("Ataque inválido, você tem demência? Tente de novo.")
            self.Opcoes(Personagem)
        elif(atkType == 5):
            print("Status de "+Personagem.name+": "+str(Personagem.GetSkills()))
            print("Atk arma: "+str(Personagem.arma.danoBase)+"   Xp: "+str(Personagem.XP))
            self.Opcoes(Personagem)
        elif(atkType == 6):
            Personagem.bag.ShowBag()
            self.Opcoes(Personagem)
        else:
            return atkType
        #endif
    #endfunc
    def AcertoCritico(self, dano):
        crit = rnd.randint(1,5)
        if(crit == 1):
            print("ACERTO CRÍTICO!!!")  
            return (2*dano)
        else:
            return(dano)
        #endif
    #endfunc
    def TipoAtk(self, monstro):
        if(monstro.HP < 0.5*monstro.HPmax):
            monster_atkType = rnd.randint(1,5)
        else:
            monster_atkType = rnd.randint(1,4)      
        return monster_atkType  
#endclass 
