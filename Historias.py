#encoding: utf-8
import sys
import classes
import libMain as lib
import io


monstros = lib.CriaMonstros()

def Intro(Heroi):
    arq = "Arquivostxt/Introducao.txt"
    #lib.SubstituiNomeHeroiNoArquivo(arq, Heroi.name)
    input("[enter]")
    lib.ProcuraTexto("Q1-ini","Q1-fim",arq, Heroi.name)
    resp = input()
    if(int(resp) == 1):
        lib.ProcuraTexto("R1-1-ini","R1-1-p1",arq, Heroi.name)
        Heroi.HP -= 2
        lib.Combate(Heroi,lib.GetMonstro(monstros, "Cao infernal"))
        lib.ProcuraTexto("R1-1-p1","R1-1-fim",arq, Heroi.name)
    elif(int(resp) == 2):
        lib.ProcuraTexto("R1-2-ini","R1-2-fim",arq, Heroi.name)
    elif(int(resp) == 3):
        lib.ProcuraTexto("R1-3-ini","R1-3-p1",arq, Heroi.name)
        lib.Combate(Heroi,lib.GetMonstro(monstros, "Cao infernal"))
        lib.ProcuraTexto("R1-3-p1","R1-3-fim",arq, Heroi.name)

    input("[enter]")
    lib.ProcuraTexto("Q2-ini", "Q2-p1",arq, Heroi.name)
        
    input("[enter]")
    lib.ProcuraTexto("Q2-p1","Q2-fim",arq, Heroi.name)
    resp = input()
    if(int(resp) == 1):
        lib.ProcuraTexto("R2-1-ini","R2-1-p1",arq, Heroi.name)
        input("[enter]")
        lib.ProcuraTexto("R2-1-p1","R2-1-p2",arq, Heroi.name)
        Heroi.HP -= 10
        lib.ProcuraTexto("R2-1-p2","R2-1-fim",arq, Heroi.name)
    elif(int(resp) == 2):
        lib.ProcuraTexto("R2-2-ini","R2-2-fim",arq, Heroi.name)
    elif(int(resp) == 3):
        lib.ProcuraTexto("R2-3-ini","R2-3-p1",arq, Heroi.name)
        input("[enter]")
        lib.ProcuraTexto("R2-3-p1","R2-3-p2",arq, Heroi.name)
        input("[enter]")
        lib.ProcuraTexto("R2-3-p2","R2-3-fim",arq, Heroi.name)
        input("[enter]")

    if(Heroi.classe.lower() == 'mago'):
        IntroMago(Heroi)
    elif(Heroi.classe.lower() == 'guerreiro'):
        IntroGuerreiro(Heroi)
    elif(Heroi.classe.lower() == 'arqueiro'):
        IntroLegolas(Heroi)


def IntroMago(Heroi):
    arq = "Arquivostxt/IntroMago.txt"
    #print("A missão descrita no anúncio pede que você vá até a capital da magia, Arianthe, entregar uma carta ao professor Willhelm, na universidade da cidade.")
    lib.ProcuraTexto("Q1-ini","Q1-p1",arq, Heroi.name)
    input("[enter]")
    lib.ProcuraTexto("Q1-p1","Q1-p2",arq, Heroi.name)
    input("[enter]")
    lib.ProcuraTexto("Q1-p2","Q1-fim",arq, Heroi.name)
    resp = input()
    if(int(resp) == 1):
        lib.ProcuraTexto("R1-1-ini","R1-1-p1",arq, Heroi.name)
        input("[enter]")
        lib.ProcuraTexto("R1-1-p1","R1-1-p2",arq, Heroi.name)
        lib.Combate(Heroi,lib.GetMonstro(monstros, "Bandido"))
        input("[enter]")
        lib.Combate(Heroi,lib.GetMonstro(monstros, "Bandido Atirador"))
        input("[enter]")
        lib.ProcuraTexto("R1-1-p2","R2-1-p3",arq, Heroi.name)
        Heroi.MP = Heroi.MPmax
        lib.ProcuraTexto("R1-1-p3", "R1,1-fim",arq, Heroi.name)
    elif(int(resp) == 2):
        lib.ProcuraTexto("R1-2-ini", "R1-2-p1", arq, Heroi.name)
        lib.Combate(Heroi,lib.GetMonstro(monstros,"Javali"))
        lib.ProcuraTexto("R1-2-p1", "R1-2-p2", arq, Heroi.name)
        lib.Combate(Heroi,lib.GetMonstro(monstros, "Bandido"))
        lib.ProcuraTexto("R1-2-p2", "R1-2-p3", arq, Heroi.name)
        input("[enter]")
        lib.Combate(Heroi,lib.GetMonstro(monstros, "Bandido Atirador"))
        lib.ProcuraTexto("R1-2-p3", "R1-2-fim", arq, Heroi.name)
        Heroi.MP = Heroi.MPmax  
    elif(int(resp) == 3):
        lib.ProcuraTexto("R1-3-ini","R1-3-p1",arq, Heroi.name)
        lib.Combate(Heroi,lib.GetMonstro(monstros, "Orc Besteiro"))
        lib.ProcuraTexto("R1-3-p1","R1-3-p2",arq, Heroi.name)
        input("[enter]")
        lib.ProcuraTexto("R1-3-p2","R1-3-p3",arq, Heroi.name)
        input("[enter]")
        lib.ProcuraTexto("R1-3-p3","R1-3-fim",arq, Heroi.name)
        Heroi.MP = Heroi.MPmax
        CapituloFloripaMago(Heroi)

def CapituloFloripaMago(Heroi):
    sys.exit()
    
def IntroGuerreiro(Heroi):
    print("")

def IntroLegolas(Heroi):
    print("")
