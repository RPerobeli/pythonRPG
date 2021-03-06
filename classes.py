#-*- coding: utf-8 -*-
import random
class Personagem:
    #Constructor
    def __init__(self, nome, classe):
        self.name = nome
        self.XP = 0
        self.lvl = 1
        self.classe = classe
        self.skills = {"str" : 0,"agi": 0, "int" : 0,"vit": 0}
        self.atk = 3 
        

        if(self.classe.lower() == "guerreiro"):
            self.skills['str'] = 4
            self.skills['agi'] = 2
            self.skills['vit'] = 3
            self.skills["int"] = 1
            
        elif(self.classe.lower() == "arqueiro"):
            self.skills['str'] = 2
            self.skills['agi'] = 4
            self.skills['vit'] = 2
            self.skills["int"] = 2
            
        elif(self.classe.lower() == "mago"):
            self.skills['str'] = 1
            self.skills['agi'] = 2
            self.skills['vit'] = 3
            self.skills["int"] = 4
            self.atk = 4
            
        else:
            print("Erro no construtor")

        self.AtualizaStatus()
    #########################################################################################
    def GetClasse(self):
        return self.classe
    def GetSkills(self):
        return self.skills
    
    def GetNome(self):
        return self.nome
    #########################################################################################
    def SetClasse(self):
        self.classe = input("Digite sua classe:")
    def SetNome(self):
        self.nome = input("Digite o nome do seu personagem:")    
    #########################################################################################    
    def SetAtk(self, WeaponAtk):
        self.atk = WeaponAtk  
    
    def AtualizaStatus(self):
        self.HP = 10*self.skills["vit"]
        self.MP = 10*self.skills["int"] 
        self.HPmax = 10*self.skills["vit"]
        self.MPmax = 10*self.skills["int"] 

    def LvlUP(self):
        
        self.lvl += 1
        print("Você chegou ao NIVEL " + str(self.lvl)+ "!")
        skill =input("Selecione onde alocar seu ponto (força, vitalidade, agilidade ou inteligencia): ")
        if(skill.lower() == "forca" or skill.lower() == "força"):
            self.skills["str"] += 1
        elif(skill.lower() == "agilidade"):
            self.skills["agi"] +=1 
        elif(skill == "inteligencia" or skill.lower() == "inteligência"):
            self.skills["int"] +=1
        elif(skill.lower() == "vitalidade"):
            self.skills["vit"] += 1       
        else:
            print("Atributo inválido, digite novamente")
            self.lvl -= 1
            self.LvlUP()
        self.XP -= 100
        self.AtualizaStatus()

    def AutoLvl(self, level):
        lvl_old = self.lvl
        self.lvl = level
        skillPoints = self.lvl-lvl_old
        self.AutoLvlUpSKills(skillPoints)
    def AutoLvlUpSKills(self, sPoints):
        vet = [0,0,0,0]
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
            extraPoints = sPoints -soma
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
            extraPoints = sPoints -soma
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
            extraPoints = sPoints -soma
            self.skills["int"] += extraPoints
        else:
            print("Erro na distribuição de skill points")
        self.AtualizaStatus()

    def Atk(self, atkType, target):
        if(self.classe.lower() == "guerreiro"):
            if(atkType == 1):
                dano = self.atk*self.skills["str"] + 2*self.skills["agi"]
                dano = self.AcertoCritico(dano)
                print(self.name+ " causou "+str(dano)+ " de dano!")
                target.HP -= dano
            elif(atkType == 2):
                dano = 2*self.atk*self.skills["str"] + self.skills["vit"]
                dano = self.AcertoCritico(dano)
                print(self.name+ " causou "+str(dano)+ " de dano!")
                target.HP -= dano
                self.HP -= 0.2*self.HPmax
            elif(atkType == 3):
                dano = 2*self.skills["int"]+ self.skills["str"]
                dano = self.AcertoCritico(dano)
                print(self.name+ " causou "+str(dano)+ " de dano!")
                target.HP -= dano 
                self.MP -= 0.2*self.MPmax
            elif(atkType == 4):
                self.HP += 0.25*self.HPmax
                self.MP += 0.25*self.MPmax
                if(self.HP > self.HPmax):
                    self.HP = self.HPmax
                if(self.MP > self.MPmax):
                    self.MP = self.MPmax                
            else:
                print("Erro no ataque de guerreiro")
        elif(self.classe.lower() == "arqueiro"):
            if(atkType == 1):
                dano =  2*self.skills["str"] + self.atk*self.skills["agi"]
                dano = self.AcertoCritico(dano)
                print(self.name+ " causou "+str(dano)+ " de dano!")
                target.HP -= dano 
            elif(atkType == 2):
                dano =2*self.atk*self.skills["agi"]
                dano = self.AcertoCritico(dano)
                print(self.name+ " causou "+str(dano)+ " de dano!")
                target.HP -= dano 
                self.MP -= 0.2*self.MPmax
            elif(atkType == 3):
                dano = 2*self.skills["int"]+ self.skills["agi"] #CHAMAR FUNCAO DE MAGIAS
                dano = self.AcertoCritico(dano)
                print(self.name+ " causou "+str(dano)+ " de dano!")
                target.HP -= dano
            elif(atkType == 4):
                self.HP += 0.25*self.HPmax
                self.MP += 0.25*self.MPmax
                if(self.HP > self.HPmax):
                    self.HP = self.HPmax
                if(self.MP > self.MPmax):
                    self.MP = self.MPmax
            else:
                print("Erro no ataque de arqueiro")
        elif(self.classe.lower() == "mago"):
            if(atkType == 1):
                dano = 2*self.skills["int"] + 1*self.skills["str"]
                dano = self.AcertoCritico(dano)
                print(self.name+ " causou "+str(dano)+ " de dano!")
                target.HP -= dano
            elif(atkType == 2):
                dano = 2*self.atk*self.skills["int"]
                dano = self.AcertoCritico(dano)
                print(self.name+ " causou "+str(dano)+ " de dano!")
                target.HP -= dano
                self.MP -= 0.5*self.MPmax
            elif(atkType == 3):
                dano = self.atk*self.skills["int"] #CHAMAR FUNCAO DE MAGIAS
                dano = self.AcertoCritico(dano)
                print(self.name+" causou "+str(dano)+ " de dano!")
                target.HP -= dano
                self.MP -= 0.1*self.MPmax
            elif(atkType == 4):
                self.HP += 0.25*self.HPmax
                self.MP += 0.25*self.MPmax
                if(self.HP > self.HPmax):
                    self.HP = self.HPmax
                if(self.MP > self.MPmax):
                    self.MP = self.MPmax
            else:
                print("Erro no ataque de mago")
        else:
            print("Erro no ataque, classe inválida")

    
    def VerificaAtk(self):
        input("[enter]")
        print("[Narrador]: Sua vez de atacar, escolha qual ataque utilizar.")
        atkType = int(input("1 - Ataque Físico \n2 - Ataque especial  \n3 - Ataque mágico \n4 - Passar turno (Recupera parte de HP e MP)\n5 - Verificar Status\n"))
        if(atkType != 1 and atkType != 2 and atkType != 3 and atkType != 4 and atkType != 5):
            print("Ataque inválido, você tem demência? Tente de novo,taokey.")
            self.VerificaAtk()
        elif(atkType == 5):
            print("Status de "+self.name+": "+str(self.GetSkills()))
            print("Atk: "+str(self.atk)+"        Xp: "+str(self.XP))
            self.VerificaAtk()
        else:
            return atkType
     
    def AdequaHP(self):
        #dobra o hp dos monstros pra ficar mais interessante
        self.HP = (0.25*self.lvl+0.75)*self.HP
        self.MP = (0.25*self.lvl+0.75)*self.MP
        self.HPmax = (0.25*self.lvl+0.75)*self.HPmax
        self.MPmax = (0.25*self.lvl+0.75)*self.MPmax
    
    def AcertoCritico(self, dano):
        crit = random.randint(1,5)
        if(crit == 1):
            print("ACERTO CRÍTICO!!!")  
            return (2*dano)
        else:
            return(dano)
