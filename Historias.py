#-*- coding: utf-8 -*-
import sys
import classes
import libMain as lib

monstros = lib.CriaMonstros()

def Intro(Heroi):
    input("[enter]")
    print("[Narrador]")
    print("Você acorda pela manha, com uma roupa cheia de lama e a cachorra na cama, qual é a primeira coisa a fazer?")
    print("1 - Você acaricia a cachorra.")
    print("2 - Você dá um tapa na cachorra.")
    print("3 - Imediatamente rola para o lado e saca sua arma e se prepara para matá-la")
    resp = input()
    if(int(resp) == 1):
        print("Ao acarariciar a cachorra, ela põe os dentes à mostra e morde sua mão, revelando ser um cão infernal.")
        print("Você rola para o lado e saca a sua arma.")
        Heroi.HP -= 2
        lib.Combate(Heroi,lib.GetMonstro(monstros, "Cao infernal"))
        print("Após a luta com o cão dos demônios, você desce as escadas em direção à taverna.")
    elif(int(resp) == 2):
        print("A cachorra vazou,e deixou um cheiro infernal na cama...")
        print("Aparentemente, você não curte cachorras, então se levanta, mexe com as piranhas no corredor, e se digire à taverna.")

    elif(int(resp) == 3):
        print("A cachorra mostra sua verdadeira face, com os dentes à mostra, percebe-se que é um cão infernal que se prepara para combate!")
        lib.Combate(Heroi,lib.GetMonstro(monstros, "Cao infernal"))
        print("Após a luta com o cão dos demônios, você desce as escadas em direção à taverna.")



def IntroMago():
    print("")

def IntroGuerreiro():
    print("")

def IntroLegolas():
    print("")
