# -*- coding: utf-8 -*-
from Domain import Heroi as bnc
from Domain import Monstro as mstr
from Domain import Arma as a
import sys
import random as rnd
import io
import os
import Interacoes as lib


def ConfereClasses(listaDeClasses, classeDesejada):
    for var in listaDeClasses:
        if classeDesejada.lower() == var.lower():
            return True
    return False


def CriaMonstros():
    arq = open("Arquivostxt/Monstros.txt", 'r')
    listaMonstros = [mstr.Monstro("erro", "Guerreiro")]
    for linha in arq:
        valores = linha.split(',')
        monstro = mstr.Monstro(valores[0], valores[1].strip())
        listaMonstros.append(monstro)
    return listaMonstros
# endfunc


def CriaArmas():
    arq = open("Arquivostxt/Armas.txt", 'r')
    listaArmas = [a.Arma("erro", 0, "erro especial", "armaErro")]
    for linha in arq:
        valores = linha.split(',')
        listaArmas.append(
            a.Arma(valores[1], valores[2], valores[3].strip(), valores[0]))
    return listaArmas
# endfunc


def GetMonstro(listaMonstros, nome):
    for monstro in listaMonstros:
        if(monstro.name.lower() == nome.lower()):
            return monstro
    print("Monstro não encontrado")
    return listaMonstros[0]
# endfunc


def GetArma(listaArmas, tag):
    for arma in listaArmas:
        if(arma.Tag.lower() == tag.lower()):
            return arma
    print("arma não encontrada")
    return listaArmas[0]
# endfunc


def Combate(Personagem, Monster):
    Monster.AutoLvl(Personagem.lvl)
    Monster.AdequaHP()
    turnCounter = rnd.randrange(1, 3)
    while(Personagem.HP > 0) and (Monster.HP > 0):
        print(Personagem.name + ".HP: " + str(Personagem.HP)+"/"+str(Personagem.HPmax) +
              "     "+Monster.name + ".HP: " + str(Monster.HP)+"/"+str(Monster.HPmax))
        print(Personagem.name + ".MP: " + str(Personagem.MP)+"/"+str(Personagem.MPmax) +
              "     "+Monster.name + ".MP: " + str(Monster.MP)+"/"+str(Monster.MPmax))
        if(turnCounter == 1):
            atkType = Personagem.acoes.Opcoes(Personagem)
            while(atkType == None):
                sys.stdout.flush()
                atkType = Personagem.acoes.Opcoes(Personagem)
            # endwhile
            os.system("cls")
            Personagem.acoes.Atk(Personagem, atkType, Monster, turnCounter)
            turnCounter += 1
        elif(turnCounter == 2):
            print("Vez do monstro atacar, segura na mão de Eru e vai!")
            lib.LimpaConsole()
            Monster.acoes.Atk(Monster, Monster.acoes.TipoAtk(
                Monster), Personagem, turnCounter)
            turnCounter -= 1

    if(Personagem.HP <= 0):
        print("Lanchado, se fodeu.")
        sys.exit()
    elif(Monster.HP <= 0):
        print("O "+Monster.name+" foi capinado.")
        Personagem.XP = XP(Monster.lvl)
        if(Personagem.XP >= 100):
            Personagem.LvlUP()
        else:
            print("XP: " + str(Personagem.XP)+'/' + str(100))
    else:
        print("Saiu da batalha antes do esperado.")


def XP(MonsterLevel):
    XP = 100 * 1/MonsterLevel
    return XP


def ProcuraTexto(ChaveInicio, ChaveFim, arquivoNome, nome):
    vetor = []
    with io.open(arquivoNome, "r", encoding="utf8") as file:
        for i, linha in enumerate(file):
            if(linha.strip() == ChaveInicio):
                vetor.append(i)
            # endif
            if(linha.strip() == ChaveFim):
                vetor.append(i)
            # endif
        # endfor
        PrintTexto(vetor[0], vetor[1], arquivoNome, nome)
    # endwith
# endfunc


def PrintTexto(li, lf, arquivoNome, nome):
    with io.open(arquivoNome, "r", encoding="utf8") as file:
        for i, linha in enumerate(file):
            if(i > li and i < lf):
                linha = linha.replace("Heroi", nome)
                print(linha.strip())
            # endif
        # endfor
    # endwith
# endfunc


def SubstituiNomeHeroiNoArquivo(fileName, nome):
    file = io.open(fileName, "r", encoding="utf8")
    texto = file.read()
    texto.replace("Heroi", nome)
# endfunc


def LimpaConsole():
    input("[enter]")
    os.system("cls")
# endfunc


def NaoTemMana(Personagem, mpNecessario):
    if(Personagem.MP < mpNecessario):
        return True
    else:
        return False
# endfunc
