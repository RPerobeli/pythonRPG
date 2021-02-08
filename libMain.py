#-*- coding: utf-8 -*-
import classes
import sys
import random as rnd


def ConfereClasses(listaDeClasses, classeDesejada):
    for var in listaDeClasses:
        if classeDesejada.lower() == var.lower():
            return True
    return False

def CriaMonstros():
    arq = open("Monstros.txt", 'r')
    listaMonstros = [classes.Personagem("erro", "Guerreiro")]
    for linha in arq:
        valores = linha.split(',')
        listaMonstros.append(classes.Personagem(valores[0],valores[1].strip()))
    return listaMonstros

def GetMonstro(listaMonstros, nome):
    for monstro in listaMonstros:
        if(monstro.name.lower() == nome.lower()):
            return monstro
    print("Monstro não encontrado")
    return listaMonstros[0]

def TipoAtkMontro(monstro):
    HPmax = 10*monstro.skills["vit"]
    if(monstro.HP > 0.7*HPmax):
        monster_atkType = 1
    elif(monstro.HP < 0.7*HPmax) and (monstro.HP > 0.4*HPmax):
        monster_atkType = 3
    elif(monstro.HP < 0.4*HPmax) and (monstro.HP > 0.2*HPmax):
        monster_atkType = 2
    else:
        monster_atkType = 4      
    return monster_atkType    



def Combate(Personagem, Monster):
    Monster.AutoLvl(Personagem.lvl)
    Monster.AdequaHP()
    turnCounter = rnd.randrange(1, 3)
    print(Personagem.skills)
    while(Personagem.HP > 0) and (Monster.HP > 0):
        print(Personagem.name +".HP: "+ str(Personagem.HP)+"/"+str(Personagem.HPmax)+"     "+Monster.name +".HP: "+ str(Monster.HP)+"/"+str(Monster.HPmax))
        print(Personagem.name +".MP: "+ str(Personagem.MP)+"/"+str(Personagem.MPmax)+"     "+Monster.name +".MP: "+ str(Monster.MP)+"/"+str(Monster.MPmax))
        if(turnCounter == 1):
            atkType = VerificaAtk()
            Personagem.Atk(atkType, Monster)
            turnCounter += 1
        elif(turnCounter == 2):
            print("Vez do monstro atacar, segura na mão de Eru e vai!")
            input("[enter]")
            Monster.Atk(TipoAtkMontro(Monster), Personagem)
            turnCounter -= 1
        

    if(Personagem.HP <=0):
        print("Lanchado, se fodeu.")
        sys.exit()
    elif(Monster.HP <=0):
        print("O "+Monster.name+" foi capinado.")
        Personagem.XP=XP(Monster.lvl)
        if(Personagem.XP >= 100):
            Personagem.LvlUP()
        else:
            print(str(Personagem.XP)+ '/'+ str(100))    
    else:
        print("Saiu da batalha antes do esperado.")


def XP(MonsterLevel):
    XP = 100 * 1/MonsterLevel
    return XP
    
def VerificaAtk():
    input("[enter]")
    print("[Narrador]: Sua vez de atacar, escolha qual ataque utilizar.")
    atkType = int(input("1 - Ataque Físico \n2 - Ataque especial  \n3 - Ataque mágico \n4 - Passar turno (Recupera parte de HP e MP)\n5 - Verificar Status"))
    if(atkType != 1 and atkType != 2 and atkType != 3 and atkType != 4 and atkType != 5):
        print("Ataque inválido, você tem demência? Tente de novo.")
        VerificaAtk()
    else:
        return atkType
     