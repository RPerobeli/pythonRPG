#encoding: utf-8
import sys
from Domain import Personagem
import Interacoes as lib
import os


monstros = lib.CriaMonstros()
armas = lib.CriaArmas()

def Intro(Heroi):
    arq = "Arquivostxt/Introducao.txt"
    lib.SubstituiNomeHeroiNoArquivo(arq, Heroi.name)
    lib.LimpaConsole()
    lib.ProcuraTexto("Q1-ini", "Q1-fim", arq, Heroi.name)
    resp = input()
    while(resp != "1" and resp != "2" and resp != "3"):
        print("Ta com pressa irmao? para de pular os dialogos.")
        lib.ProcuraTexto("Q1-ini", "Q1-fim", arq, Heroi.name)
        resp = input()
    # endwhile
    lib.Limpa()
    if(int(resp) == 1):
        lib.ProcuraTexto("R1-1-ini", "R1-1-p1", arq, Heroi.name)
        lib.LimpaConsole()
        Heroi.HP -= 2
        lib.Combate(Heroi, lib.GetMonstro(monstros, "Cao infernal"))
        lib.ProcuraTexto("R1-1-p1", "R1-1-fim", arq, Heroi.name)
    elif(int(resp) == 2):
        lib.ProcuraTexto("R1-2-ini", "R1-2-fim", arq, Heroi.name)

    elif(int(resp) == 3):
        lib.ProcuraTexto("R1-3-ini", "R1-3-p1", arq, Heroi.name)
        lib.LimpaConsole()
        lib.Combate(Heroi, lib.GetMonstro(monstros, "Cao infernal"))
        lib.ProcuraTexto("R1-3-p1", "R1-3-fim", arq, Heroi.name)

    lib.LimpaConsole()
    lib.ProcuraTexto("Q2-ini", "Q2-p1", arq, Heroi.name)

    lib.LimpaConsole()
    lib.ProcuraTexto("Q2-p1", "Q2-fim", arq, Heroi.name)
    resp = input()
    while(resp != "1" and resp != "2" and resp != "3"):
        print("Ta com pressa irmao? para de pular os dialogos.")
        lib.ProcuraTexto("Q2-p1", "Q2-fim", arq, Heroi.name)
        resp = input()
    # endwhile
    lib.Limpa()
    if(int(resp) == 1):
        lib.ProcuraTexto("R2-1-ini", "R2-1-p1", arq, Heroi.name)
        lib.LimpaConsole()
        lib.ProcuraTexto("R2-1-p1", "R2-1-p2", arq, Heroi.name)
        lib.LimpaConsole()
        Heroi.HP -= 10
        lib.ProcuraTexto("R2-1-p2", "R2-1-fim", arq, Heroi.name)
    elif(int(resp) == 2):
        lib.ProcuraTexto("R2-2-ini", "R2-2-fim", arq, Heroi.name)
    elif(int(resp) == 3):
        lib.ProcuraTexto("R2-3-ini", "R2-3-p1", arq, Heroi.name)
        lib.LimpaConsole()
        lib.ProcuraTexto("R2-3-p1", "R2-3-p2", arq, Heroi.name)
        lib.LimpaConsole()
        lib.ProcuraTexto("R2-3-p2", "R2-3-fim", arq, Heroi.name)

    lib.LimpaConsole()

    if(Heroi.classe.lower() == 'mago'):
        IntroMago(Heroi)
    elif(Heroi.classe.lower() == 'guerreiro'):
        IntroGuerreiro(Heroi)
    elif(Heroi.classe.lower() == 'arqueiro'):
        IntroLegolas(Heroi)


def IntroMago(Heroi):
    arq = "Arquivostxt/IntroMago.txt"
    lib.SubstituiNomeHeroiNoArquivo(arq, Heroi.name)
    #print("A missão descrita no anúncio pede que você vá até a capital da magia, Arianthe, entregar uma carta ao professor Willhelm, na universidade da cidade.")
    lib.ProcuraTexto("Q1-ini", "Q1-p1", arq, Heroi.name)
    lib.LimpaConsole()
    lib.ProcuraTexto("Q1-p1", "Q1-p2", arq, Heroi.name)
    lib.LimpaConsole()
    lib.ProcuraTexto("Q1-p2", "Q1-fim", arq, Heroi.name)
    resp = input()
    while(resp != "1" and resp != "2" and resp != "3"):
        print("Ta com pressa irmao? para de pular os dialogos.")
        lib.ProcuraTexto("Q1-p2", "Q1-fim", arq, Heroi.name)
        resp = input()
    # endwhile
    lib.Limpa()
    if(int(resp) == 1):
        lib.ProcuraTexto("R1-1-ini", "R1-1-p1", arq, Heroi.name)
        lib.LimpaConsole()
        lib.ProcuraTexto("R1-1-p1", "R1-1-p2", arq, Heroi.name)
        lib.LimpaConsole()
        lib.Combate(Heroi, lib.GetMonstro(monstros, "Bandido"))
        lib.LimpaConsole()
        lib.Combate(Heroi, lib.GetMonstro(monstros, "Bandido Atirador"))
        lib.LimpaConsole()
        lib.ProcuraTexto("R1-1-p2", "R1-1-p3", arq, Heroi.name)
        Heroi.MP = Heroi.MPmax
        lib.ProcuraTexto("R1-1-p3", "R1-1-fim", arq, Heroi.name)
    elif(int(resp) == 2):
        lib.ProcuraTexto("R1-2-ini", "R1-2-p1", arq, Heroi.name)
        lib.LimpaConsole()
        lib.Combate(Heroi, lib.GetMonstro(monstros, "Javali"))
        lib.ProcuraTexto("R1-2-p1", "R1-2-p2", arq, Heroi.name)
        lib.LimpaConsole()
        lib.Combate(Heroi, lib.GetMonstro(monstros, "Bandido"))
        lib.ProcuraTexto("R1-2-p2", "R1-2-p3", arq, Heroi.name)
        lib.LimpaConsole()
        lib.Combate(Heroi, lib.GetMonstro(monstros, "Bandido Atirador"))
        lib.ProcuraTexto("R1-2-p3", "R1-2-fim", arq, Heroi.name)
        Heroi.MP = Heroi.MPmax
    elif(int(resp) == 3):
        lib.ProcuraTexto("R1-3-ini", "R1-3-p1", arq, Heroi.name)
        lib.LimpaConsole()
        lib.Combate(Heroi, lib.GetMonstro(monstros, "Orc Besteiro"))
        lib.ProcuraTexto("R1-3-p1", "R1-3-p2", arq, Heroi.name)
        lib.LimpaConsole()
        lib.ProcuraTexto("R1-3-p2", "R1-3-p3", arq, Heroi.name)
        lib.LimpaConsole()
        lib.ProcuraTexto("R1-3-p3", "R1-3-fim", arq, Heroi.name)
        Heroi.MP = Heroi.MPmax
    # endif
    CapituloFloripaMago(Heroi)
# endfunc


def CapituloFloripaMago(Heroi):
    arq = "Arquivostxt/SoltosEmFloripa.txt"
    lib.SubstituiNomeHeroiNoArquivo(arq, Heroi.name)
    lib.ProcuraTexto("Q1-ini", "Q1-p1", arq, Heroi.name)
    lib.LimpaConsole()
    lib.ProcuraTexto("Q1-p1", "Q1-fim", arq, Heroi.name)
    resp = input()
    while(resp != "1" and resp != "2" and resp != "3"):
        print("Ta com pressa irmao? para de pular os dialogos.")
        lib.ProcuraTexto("Q1-p1", "Q1-fim", arq, Heroi.name)
        resp = input()
    # endwhile
    lib.Limpa()
    if(int(resp) == 1):
        lib.ProcuraTexto("R1-1-ini", "R1-1-fim", arq, Heroi.name)
        lib.Combate(Heroi, lib.GetMonstro(monstros, "Guarda Magico"))
    elif(int(resp) == 2):
        lib.ProcuraTexto("R1-2-ini", "R1-2-p1", arq, Heroi.name)
        lib.LimpaConsole()
        lib.ProcuraTexto("R1-2-p1", "R1-2-fim", arq, Heroi.name)
    elif(int(resp) == 3):
        lib.ProcuraTexto("R1-3-ini", "R1-3-fim", arq, Heroi.name)
        lib.LimpaConsole()
    # endif
    lib.ProcuraTexto("Q2-ini", "Q2-p1", arq, Heroi.name)
    lib.LimpaConsole()
    lib.ProcuraTexto("Q2-p1", "Q2-p2", arq, Heroi.name)
    lib.LimpaConsole()
    lib.ProcuraTexto("Q2-p2", "Q2-fim", arq, Heroi.name)
    resp = input()
    while(resp != "1" and resp != "2" and resp != "3"):
        print("Ta com pressa irmao? para de pular os dialogos.")
        lib.ProcuraTexto("Q2-p2", "Q2-fim", arq, Heroi.name)
        resp = input()
    # endwhile
    lib.Limpa()
    if(int(resp) == 1):
        lib.ProcuraTexto("R2-1-ini", "R2-1-fim", arq, Heroi.name)
        lib.LimpaConsole()
    elif(int(resp) == 2):
        lib.ProcuraTexto("R2-2-ini", "R2-2-p1", arq, Heroi.name)
        lib.LimpaConsole()
        lib.ProcuraTexto("R2-2-p1", "R2-2-fim", arq, Heroi.name)
        lib.LimpaConsole()
        print("Literalmente lanchado.")  # GameOver
        sys.exit()
    elif(int(resp) == 3):
        lib.ProcuraTexto("R2-3-ini", "R2-3-p1", arq, Heroi.name)
        lib.LimpaConsole()
        lib.ProcuraTexto("R2-3-p1", "R2-3-p2", arq, Heroi.name)
        lib.LimpaConsole()
        lib.Combate(Heroi, lib.GetMonstro(monstros, "Willhelm"))
        lib.ProcuraTexto("R2-3-p2", "R2-3-fim", arq, Heroi.name)
        lib.LimpaConsole()
        Heroi.HP = Heroi.HPmax
        Heroi.MP = Heroi.MPmax
    # endif
    lib.ProcuraTexto("Q3-ini", "Q3-p1", arq, Heroi.name)
    lib.LimpaConsole()
    lib.ProcuraTexto("Q3-p1", "Q3-fim", arq, Heroi.name)
    resp = input()
    while(resp != "1" and resp != "2" and resp != "3"):
        print("Ta com pressa irmao? para de pular os dialogos.")
        lib.ProcuraTexto("Q3-p1", "Q3-fim", arq, Heroi.name)
        resp = input()
    # endwhile
    lib.Limpa()
    if(int(resp) == 1):
        lib.ProcuraTexto("R3-1-ini", "R3-1-p1", arq, Heroi.name)
        lib.LimpaConsole()
        lib.ProcuraTexto("R3-1-p1", "R3-1-p2", arq, Heroi.name)
        lib.LimpaConsole()
        lib.ProcuraTexto("R3-1-p2", "R3-1-p3", arq, Heroi.name)
        lib.LimpaConsole()
        lib.ProcuraTexto("R3-1-p3", "R3-1-p4", arq, Heroi.name)
        lib.LimpaConsole()
        lib.ProcuraTexto("R3-1-p4", "R3-1-p5", arq, Heroi.name)
        lib.LimpaConsole()
        lib.ProcuraTexto("R3-1-p5", "R3-1-p6", arq, Heroi.name)
        lib.LimpaConsole()
        lib.Combate(Heroi, lib.GetMonstro(monstros, "Demonio Inferior"))
        lib.ProcuraTexto("R3-1-p6", "R3-1-p7", arq, Heroi.name)
        lib.LimpaConsole()
        lib.ProcuraTexto("R3-1-p7", "R3-1-p8", arq, Heroi.name)
        lib.LimpaConsole()
        lib.ProcuraTexto("R3-1-p8", "R3-1-p9", arq, Heroi.name)
        lib.LimpaConsole()
        lib.ProcuraTexto("R3-1-p9", "R3-1-fim", arq, Heroi.name)
        lib.LimpaConsole()
    elif(int(resp) == 2):
        lib.ProcuraTexto("R3-2-ini", "R3-2-p1", arq, Heroi.name)
        lib.LimpaConsole()
        lib.ProcuraTexto("R3-2-p1", "R3-2-p2", arq, Heroi.name)
        lib.LimpaConsole()
        lib.ProcuraTexto("R3-2-p2", "R3-2-p3", arq, Heroi.name)
        lib.LimpaConsole()
        lib.Combate(Heroi, lib.GetMonstro(monstros, "Demonio Inferior"))
        lib.ProcuraTexto("R3-2-p3", "R3-2-p4", arq, Heroi.name)
        lib.LimpaConsole()
        lib.ProcuraTexto("R3-2-p4", "R3-2-p5", arq, Heroi.name)
        lib.LimpaConsole()
        lib.ProcuraTexto("R3-2-p5", "R3-2-fim", arq, Heroi.name)
        lib.LimpaConsole()
        Heroi.arma = lib.GetArma(armas, "arma1mago")
        print("Voce recebeu uma nova arma: ", Heroi.arma.name)
    elif(int(resp) == 3):
        lib.ProcuraTexto("R3-3-ini", "R3-3-p1", arq, Heroi.name)
        lib.LimpaConsole()
        lib.ProcuraTexto("R3-3-p1", "R3-3-p2", arq, Heroi.name)
        lib.LimpaConsole()
        lib.ProcuraTexto("R3-3-p2", "R3-3-p3", arq, Heroi.name)
        lib.LimpaConsole()
        lib.Combate(Heroi, lib.GetMonstro(monstros, "Demonio Inferior"))
        lib.ProcuraTexto("R3-3-p3", "R3-3-fim", arq, Heroi.name)
        lib.LimpaConsole()
    # endif
    lib.ProcuraTexto("Q4-ini", "Q4-p1", arq, Heroi.name)
    lib.LimpaConsole()
    lib.ProcuraTexto("Q4-p1", "Q4-p2", arq, Heroi.name)
    lib.LimpaConsole()
    lib.ProcuraTexto("Q4-p2", "Q4-p3", arq, Heroi.name)
    lib.LimpaConsole()
    lib.ProcuraTexto("Q4-p3", "Q4-p4", arq, Heroi.name)
    lib.LimpaConsole()
    lib.ProcuraTexto("Q4-p4", "Q4-fim", arq, Heroi.name)
    resp = input()
    while(resp != "1" and resp != "2" and resp != "3"):
        print("Ta com pressa irmao? para de pular os dialogos.")
        lib.ProcuraTexto("Q4-p4", "Q4-fim", arq, Heroi.name)
        resp = input()
    # endwhile
    lib.Limpa()
    if(int(resp) == 1):
        lib.ProcuraTexto("R4-1-ini", "R4-1-p1", arq, Heroi.name)
        lib.LimpaConsole()
        lib.ProcuraTexto("R4-1-p1", "R4-1-p2", arq, Heroi.name)
        lib.LimpaConsole()
        lib.ProcuraTexto("R4-1-p2", "R4-1-p3", arq, Heroi.name)
        lib.LimpaConsole()
        lib.ProcuraTexto("R4-1-p3", "R4-1-p4", arq, Heroi.name)
        lib.LimpaConsole()
        lib.ProcuraTexto("R4-1-p4", "R4-1-p5", arq, Heroi.name)
        lib.LimpaConsole()
        lib.ProcuraTexto("R4-1-p5", "R4-1-fim", arq, Heroi.name)
        lib.LimpaConsole()
        CapituloKrambeckMago(Heroi)
    elif(int(resp) == 2):
        lib.ProcuraTexto("R4-2-ini", "R4-2-p1", arq, Heroi.name)
        lib.LimpaConsole()
        lib.ProcuraTexto("R4-2-p1", "R4-2-p2", arq, Heroi.name)
        lib.LimpaConsole()
        lib.ProcuraTexto("R4-2-p2", "R4-2-p3", arq, Heroi.name)
        lib.LimpaConsole()
        lib.Combate(Heroi, lib.GetMonstro(monstros, "Guarda Magico de Elite"))
        lib.LimpaConsole()
        lib.Combate(Heroi, lib.GetMonstro(monstros, "Guarda Magico de Elite"))
        lib.ProcuraTexto("R4-2-p3", "R4-2-fim", arq, Heroi.name)
        lib.LimpaConsole()
        CapituloFelastusMago(Heroi)
    # endif


def CapituloFelastusMago(Heroi):
    print("")


def CapituloFelastusGuerreiro(Heroi):
    print("")


def CapituloKrambeckArqueiro(Heroi):
    print("")


def CapituloKrambeckMago(Heroi):
    print("")


def IntroGuerreiro(Heroi):
    arq = "Arquivostxt/IntroGuerreiro.txt"
    lib.SubstituiNomeHeroiNoArquivo(arq, Heroi.name)


def IntroLegolas(Heroi):
    print("")
