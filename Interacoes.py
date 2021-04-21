#-*- coding: utf-8 -*-
from Domain import Personagem as bnc
import sys
import random as rnd
import io


def ConfereClasses(listaDeClasses, classeDesejada):
    for var in listaDeClasses:
        if classeDesejada.lower() == var.lower():
            return True
    return False

def CriaMonstros():
    arq = open("Arquivostxt/Monstros.txt", 'r')
    listaMonstros = [bnc.Personagem("erro", "Guerreiro")]
    for linha in arq:
        valores = linha.split(',')
        listaMonstros.append(bnc.Personagem(valores[0],valores[1].strip()))
    return listaMonstros

def GetMonstro(listaMonstros, nome):
    for monstro in listaMonstros:
        if(monstro.name.lower() == nome.lower()):
            return monstro
    print("Monstro não encontrado")
    return listaMonstros[0]

def Combate(Personagem, Monster):
    Monster.AutoLvl(Personagem.lvl)
    Monster.AdequaHP()
    turnCounter = rnd.randrange(1, 3)
    while(Personagem.HP > 0) and (Monster.HP > 0):
        print(Personagem.name +".HP: "+ str(Personagem.HP)+"/"+str(Personagem.HPmax)+"     "+Monster.name +".HP: "+ str(Monster.HP)+"/"+str(Monster.HPmax))
        print(Personagem.name +".MP: "+ str(Personagem.MP)+"/"+str(Personagem.MPmax)+"     "+Monster.name +".MP: "+ str(Monster.MP)+"/"+str(Monster.MPmax))
        if(turnCounter == 1):
            atkType = Personagem.acoes.Opcoes(Personagem)
            while(atkType == None):
                sys.stdout.flush()
                atkType = Personagem.acoes.Opcoes(Personagem)
            #endwhile
            Personagem.acoes.Atk(Personagem, atkType, Monster)
            turnCounter += 1
        elif(turnCounter == 2):
            print("Vez do monstro atacar, segura na mão de Eru e vai!")
            input("[enter]")
            Monster.acoes.Atk(Monster, Monster.acoes.TipoAtk(Monster), Personagem)
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
            print(str(Personagem.XP)+'/'+ str(100))    
    else:
        print("Saiu da batalha antes do esperado.")


def XP(MonsterLevel):
    XP = 100 * 1/MonsterLevel
    return XP

def ProcuraTexto(ChaveInicio, ChaveFim, arquivoNome, nome):
    vetor = []
    with io.open(arquivoNome,"r",encoding="utf8") as file:
        for i, linha in enumerate(file):
            if(linha.strip() == ChaveInicio):
                vetor.append(i)
            #endif
            if(linha.strip() == ChaveFim):
                vetor.append(i)
            #endif
        #endfor
        PrintTexto(vetor[0], vetor[1], arquivoNome,nome)
    #endwith
#endfunc
        

def PrintTexto(li, lf, arquivoNome,nome):
    with io.open(arquivoNome,"r",encoding="utf8") as file:
        for i, linha in enumerate(file):
            if(i > li and i < lf):
                linha= linha.replace("Heroi", nome)
                print(linha.strip())
            #endif
        #endfor
    #endwith       
#endfunc

def SubstituiNomeHeroiNoArquivo(fileName,nome):
    file = io.open(fileName,"r",encoding="utf8")
    texto = file.read()
    texto.replace("Heroi", nome)
#endfunc