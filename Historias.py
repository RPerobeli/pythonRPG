#-*- coding: utf-8 -*-
import sys
import classes
import libMain as lib

monstros = lib.CriaMonstros()

def Intro(Heroi):
    input("[enter]")
    #print("[Narrador]")
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
        print("Após a luta com o cão dos demônios, você desce as escadas em direção à guilda.")
    elif(int(resp) == 2):
        print("A cachorra vazou,e deixou um cheiro infernal na cama...")
        print("Aparentemente, você não curte cachorras, então se levanta, mexe com as piranhas no corredor, e se digire à guilda.")

    elif(int(resp) == 3):
        print("A cachorra mostra sua verdadeira face, com os dentes à mostra, percebe-se que é um cão infernal que se prepara para combate!")
        lib.Combate(Heroi,lib.GetMonstro(monstros, "Cao infernal"))
        print("Após a luta com o cão dos demônios, você desce as escadas em direção à guilda.")

    input("[enter]")
    print("Indo em direção a praça da cidade, você avista, em meio à nevasca, o prédio da guilda Asas da Liberdade,")
    print("uma guilda famosa em todo o continente. Após sentar-se em uma mesa na taverna da guilda, a taverneira vem ao seu encontro.")
    input("[enter]")
    print("[Taverneira]: Bom dia, senhor, aceita uma bebida e uma boa refeição da casa?")
    print("1 - Oh, uma oferta irrecusável, pode trazer a melhor cerveja da casa por favor.")
    print("2 - Então, senhorita, no momento estou duro, não tenho 1 prata sequer...")
    print("3 - Ficar calado e deixar seu corpo falar por ti.")
    resp = input()
    if(int(resp) == 1):
        print("A taverneira traz uma grande refeição para você, com a melhor cerveja. Você se sente saciado.")
        print("[Taverneira]: São apenas 30 peças de prata, senhor.")
        input("[enter]")
        print("["+Heroi.name+"] Ué, você me ofereceu comida, eu aceitei, agora tenho que pagar?")
        print("Indignada com sua resposta, a taverneira te chuta no peito, causando muita dor, e talvez quebrando uma costela...")
        Heroi.HP -= 10
        print("[Aviso]: "+Heroi.name+" perdeu 10 de HP")
        input("[enter]")
        print("[Taverneira]: Você tem que pagar pela refeição, imbecil. Se não pode pagar, pegue uma missão no mural ali e faça dinheiro!")
        print("Com as costelas doendo, você vai até  o mural e pega a única missão restante.")
    if(int(resp) == 2):
        print("[Taverneira] Pois bem, "+Heroi.classe+", há uma certa tarefa que acabou de chegar até mim, ainda não pus no mural,")
        print(" se tiver interesse, como forma de pagamento, dou-lhe a refeição, você não parece má pessoa.")
        print("Seus olhos brilham ao ver tamanha gentileza, que você pensa ter sido ajudado por um anjo. De prontidão você aceita a tarefa, enquanto saboreia o pagamento adiantado.")
    if(int(resp) == 3):
        print("ROOOOOOONC...")
        print("Ao escutar o som de seu estômago faminto, você desmaia...")
        input("[enter]")
        print("[Taverneira]: Moço, pude notar que você está sem comer há algum tempo, trouxe algo para ti.")
        print("Você come sobras de comida, e sente que foi a melhor refeição da sua vida.")
        print("A taverneira, olhando para sua situação precária, te oferece uma missão, para que você possa pelo menos viver dignamente.")
        input("[enter]")
    if(Heroi.classe.lower == 'mago'):
        IntroMago(Heroi)
    elif(Heroi.classe.lower == 'guerreiro'):
        IntroGuerreiro(Heroi)
    elif(Heroi.classe.lower == 'arqueiro'):
        IntroLegolas(Heroi)


def IntroMago(Heroi):
    print("A missão descrita no anúncio pede que você vá até a capital da magia, Xand'ora, entregar uma carta ao professor Willhelm, na universidade da cidade.")
    print("Você suspeita da recompensa, um pouco alta para uma simples entrega, mas aceita de qualquer maneira.")
    input("[enter]")
    print("Após guardar a carta na sua bolsa, você se dirige à saída.")
    print("[Taverneira]: Ei, mago, você não disse o seu nome, aliás, me chamo Jessie.")
    print("Você sorri, diz seu nome, e parte para sua viagem.")
    print("[Jessie]: Volte sempre, "+Heroi.name+".")
    input("[enter]")

def IntroGuerreiro(Heroi):
    print("")

def IntroLegolas(Heroi):
    print("")
