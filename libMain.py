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
        print(valores)
        listaMonstros.append(classes.Personagem(valores[0],valores[1]))
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
    turnCounter = rnd.randrange(1, 2)
    # print("Sua vida: "+ Personagem.HP/Personagem.HPmax)
    # print("Sua mana: "+ Personagem.MP/Personagem.MPmax)
    # print("Vida do inimigo: "+ Monster.HP/Monster.HPmax)
    # print("Mana do inimigo: "+ Monster.MP/Monster.MPmax) 
    while(Personagem.HP > 0) or (Monster.HP > 0):
        print("Sua vida: "+ Personagem.HP/Personagem.HPmax)
        print("Sua mana: "+ Personagem.MP/Personagem.MPmax)
        print("Vida do inimigo: "+ Monster.HP/Monster.HPmax)
        print("Mana do inimigo: "+ Monster.MP/Monster.MPmax)
        if(turnCounter == 1):
            print("Sua vez de atacar, escolha qual ataque utilizar seu pedaço de bosta perfumada")
            atkType = int(input("1 - Ataque Físico \n 2 - Ataque especial  \n 3 - Ataque mágico \n 4 - Passar turno (Recupera parte de HP e MP)"))
            Personagem.Atk(atkType, Monster)
            turnCounter += 1
        elif(turnCounter == 2):
            print("Vez do monstro atacar, segura na mão de Eru e vai!")

            Monster.Atk(TipoAtkMontro(Monster), Personagem)
            turnCounter -= 1
        

    if(Personagem.HP <=0):
        print("Lanchado, se fodeu.")
        sys.exit()
    elif(Monster.HP <=0):
        print("O "+Monster.name+" foi capinado.")
        Personagem.LvlUP()
    else:
        print("Saiu da batalha antes do esperado.")
     