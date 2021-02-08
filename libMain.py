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
    if(monstro.HP < 0.5*monstro.HPmax):
        monster_atkType = rnd.randint(1,5)
    else:
        monster_atkType = rnd.randint(1,4)      
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
            atkType = Personagem.VerificaAtk()
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
