class Personagem:
    #Constructor
    def __init__(self, nome, classe):
        self.name = nome
        self.lvl = 1
        self.classe = classe
        self.skills = {"str" : 0,"agi": 0, "int" : 0,"vit": 0}

        if(self.classe.lower() == "guerreiro"):
            self.skills['str'] = 4
            self.skills['agi'] = 2
            self.skills['vit'] = 3
            self.skills["int"] = 1
            self.AtualizaStatus()
            
        elif(self.classe.lower() == "arqueiro"):
            self.skills['str'] = 2
            self.skills['agi'] = 4
            self.skills['vit'] = 2
            self.skills["int"] = 2
            self.AtualizaStatus()
            
            
        elif(self.classe.lower() == "mago"):
            self.skills['str'] = 1
            self.skills['agi'] = 2
            self.skills['vit'] = 3
            self.skills["int"] = 4
            
        else:
            print("Erro no construtor")
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
    
    def AtualizaStatus(self):
        self.HP = 10*self.skills["vit"]
        self.MP = 10*self.skills["int"] 

    def LvlUP(self):
        skill =input("Selecione onde alocar seu ponto (força, vitalidade, agilidade ou inteligencia): ")
        self.lvl += 1
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
            self.LvlUP()
        self.AtualizaStatus()

    def AutoLvl(self, level):
        lvl_old = self.lvl
        self.lvl = level
        skillPoints = self.lvl-lvl_old
        self.AutoLvlUpSKills(skillPoints)
    def AutoLvlUpSKills(self, sPoints):
        vet = []
        if(self.classe == "guerreiro"):
            vet[0] = int(sPoints*0.4)
            vet[3] = int(sPoints*0.3)
            vet[2] = int(sPoints*0.1)
            vet[1] = int(sPoints*0.2)
            self.skills["str"] += vet[0]
            self.skills["vit"] += vet[3]
            self.skills["int"] += vet[2]
            self.skills["agi"] += vet[1]
            soma = sum(vet)
            extraPoints = lambda soma,sPoints : sPoints - soma
            self.skills["str"] += extraPoints
        elif(self.classe == "arqueiro"):
            vet[0] = int(sPoints*0.2)
            vet[3] = int(sPoints*0.4)
            vet[2] = int(sPoints*0.2)
            vet[1] = int(sPoints*0.2)
            self.skills["str"] += vet[0]
            self.skills["vit"] += vet[3]
            self.skills["int"] += vet[2]
            self.skills["agi"] += vet[1]
            soma = sum(vet)
            extraPoints = lambda soma,sPoints : sPoints - soma
            self.skills["agi"] += extraPoints
            
        elif(self.classe == "mago"):
            vet[0] = int(sPoints*0.1)
            vet[3] = int(sPoints*0.2)
            vet[2] = int(sPoints*0.4)
            vet[1] = int(sPoints*0.3)
            self.skills["str"] += vet[0]
            self.skills["vit"] += vet[3]
            self.skills["int"] += vet[2]
            self.skills["agi"] += vet[1]
            soma = sum(vet)
            extraPoints = lambda soma,sPoints : sPoints - soma
            self.skills["int"] += extraPoints
        else:
            print("Erro na distribuição de skill points")
