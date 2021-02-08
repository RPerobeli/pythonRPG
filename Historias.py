#-*- coding: utf-8 -*-
import sys
import classes
import libMain as lib

monstros = lib.CriaMonstros()

def Intro(Heroi):
    input("[enter]")
    #print("[Narrador]")
    print("[Narrador]: Você acorda pela manha, com uma roupa cheia de lama e a cachorra na cama, qual é a primeira coisa a fazer?")
    print("1 - Você acaricia a cachorra.")
    print("2 - Você dá um tapa na cachorra.")
    print("3 - Imediatamente rola para o lado e saca sua arma e se prepara para matá-la.")
    resp = input()
    if(int(resp) == 1):
        print("[Narrador]: Ao acarariciar a cachorra, ela põe os dentes à mostra e morde sua mão, revelando ser um cão infernal.")
        print("Você rola para o lado e saca a sua arma.")
        Heroi.HP -= 2
        lib.Combate(Heroi,lib.GetMonstro(monstros, "Cao infernal"))
        print("[Narrador]: Após a luta com o cão dos demônios, você desce as escadas em direção à guilda.")
    elif(int(resp) == 2):
        print("A cachorra vazou,e deixou um cheiro infernal na cama...")
        print("[Narrador]: Aparentemente, você não curte cachorras, então se levanta, mexe com as piranhas no corredor, e se digire à guilda.")

    elif(int(resp) == 3):
        print("[Narrador]: A cachorra mostra sua verdadeira face, com os dentes à mostra, percebe-se que é um cão infernal que se prepara para combate!")
        lib.Combate(Heroi,lib.GetMonstro(monstros, "Cao infernal"))
        print("[Narrador]: Após a luta com o cão dos demônios, você desce as escadas em direção à guilda.")

    input("[enter]")
    print("[Narrador]: Indo em direção a praça da cidade, você avista, em meio à nevasca, o prédio da guilda Asas da Liberdade,")
    print("uma guilda famosa em todo o continente. Após sentar-se em uma mesa na taverna da guilda, a taverneira vem ao seu encontro.")
    input("[enter]")
    print("[Taverneira]: Bom dia, senhor, aceita uma bebida e uma boa refeição da casa?")
    print("1 - Oh, uma oferta irrecusável, pode trazer a melhor cerveja da casa por favor.")
    print("2 - Então, senhorita, no momento estou duro, não tenho 1 prata sequer...")
    print("3 - Ficar calado e deixar seu corpo falar por ti.")
    resp = input()
    if(int(resp) == 1):
        print("[Narrador]: A taverneira traz uma grande refeição para você, com a melhor cerveja. Você se sente saciado.")
        print("[Taverneira]: São apenas 30 peças de prata, senhor.")
        input("[enter]")
        print("["+Heroi.name+"] Ué, você me ofereceu comida, eu aceitei, agora tenho que pagar?")
        print("[Narrador]: Indignada com sua resposta, a taverneira te chuta no peito, causando muita dor, e talvez quebrando uma costela...")
        Heroi.HP -= 10
        print("[Aviso]: "+Heroi.name+" perdeu 10 de HP")
        input("[enter]")
        print("[Taverneira]: Você tem que pagar pela refeição, imbecil. Se não pode pagar, pegue uma missão no mural ali e faça dinheiro!")
        print("[Narrador]: Com as costelas doendo, você vai até  o mural e pega a única missão restante.")
    elif(int(resp) == 2):
        print("[Taverneira] Pois bem, "+Heroi.classe+", há uma certa tarefa que acabou de chegar até mim, ainda não pus no mural,")
        print(" se tiver interesse, como forma de pagamento, dou-lhe a refeição, você não parece má pessoa.")
        print("[Narrador]: Seus olhos brilham ao ver tamanha gentileza, que você pensa ter sido ajudado por um anjo. De prontidão você aceita a tarefa, enquanto saboreia o pagamento adiantado.")
    elif(int(resp) == 3):
        print("ROOOOOOONC...")
        print("[Narrador]: Ao escutar o som de seu estômago faminto, você desmaia...")
        input("[enter]")
        print("[Taverneira]: Moço, pude notar que você está sem comer há algum tempo, trouxe algo para ti.")
        print("[Narrador]: Você come sobras de comida, e sente que foi a melhor refeição da sua vida.")
        input("[enter]")
        print("[Narrador]: A taverneira, olhando para sua situação precária, te oferece uma missão, para que você possa pelo menos viver dignamente.")
        input("[enter]")

    if(Heroi.classe.lower() == 'mago'):
        IntroMago(Heroi)
    elif(Heroi.classe.lower() == 'guerreiro'):
        IntroGuerreiro(Heroi)
    elif(Heroi.classe.lower() == 'arqueiro'):
        IntroLegolas(Heroi)


def IntroMago(Heroi):
    #print("A missão descrita no anúncio pede que você vá até a capital da magia, Arianthe, entregar uma carta ao professor Willhelm, na universidade da cidade.")
    print("[Narrador]:  A missão descrita no anúncio pede que você vá até a capital da magia, Florianópolis, entregar uma carta ao professor Willhelm, na universidade da cidade.")
    print("[Narrador]:  Você suspeita da recompensa, um pouco alta para uma simples entrega, mas aceita de qualquer maneira.")
    input("[enter]")
    print("[Narrador]: Após guardar a carta na sua bolsa, você se dirige à saída.")
    print("[Taverneira]: Ei, mago, você não disse o seu nome, aliás, me chamo Jessie.")
    print("[Narrador]: Você sorri, diz seu nome, e parte para sua viagem.")
    print("[Jessie]: Volte sempre, "+Heroi.name+".")
    input("[enter]")
    print("[Narrador]: Enquanto saía de Asas da Liberdade, você notou uma caravana que estava de partida, o líder da caravana te oferece uma carona até Florianópolis, você:")
    print("1 - Aceita acompanhar a caravana.")
    print("2 - Prefere seguir sozinho sua viagem.")
    print("3 - Rouba um cavalo da caravana e sai correndo.")
    resp = input()
    if(int(resp) == 1):
        print("[Narrador]: Após alguns dias, ao cair da noite, a caravana monta o último acampamento antes de chegarem em Florianópolis.")
        print("[Narrador]: Enquanto comiam em volta da fogueira, você escuta murmúrios advindos da floresta... ")
        input("[enter]")
        print("[Narrador]: Um dos guardas da caravana adentra nos arbustos. Ouve-se um grito, e o ataque começa.")
        print("[Narrador]: Um grupo de bandidos ataca a caravana, os guardas já se encontram em combate, e 2 dos bandidos vêm em sua direção.")
        lib.Combate(Heroi,lib.GetMonstro(monstros, "Bandido"))
        input("[enter]")
        lib.Combate(Heroi,lib.GetMonstro(monstros, "Bandido Atirador"))
        input("[enter]")
        print("[Narrador]: Ao olhar em volta, percebe-se que todos os guardas pereceram em batalha, levando consigo seus adversários.")
        print("[Narrador]: Os únicos restantes são o líder da caravana e os mercadores. Nesse momento, o líder se aproxima de você, agradece seus grandes feitos e te presenteia com um elixir revigorante.")
        Heroi.MP = Heroi.MPmax
        print("[Aviso]: Seus pontos de mana foram restaurados")
    elif(int(resp) == 2):
        print("[Narrador]: Já está anoitecendo e a fome volta a te assombrar, olhando à volta, no meio da neve, você vê um pequeno filhote de javali.")
        print("[Narrador]: Antes mesmo que você mate o pequeno filhote, a javali mãe te ataca rapidamente.")
        lib.Combate(Heroi,lib.GetMonstro(monstros,"Javali"))
        print("[Narrador]: Após matar a família suína, você nota que terá refeições para alguns dias.")
        input("[enter]")
        print("[Narrador]: Alguns dias depois, você encontra a mesma caravana que encontrara anteriormente, eles parecem em apuros, lutando com um grupo de ladrões,")
        print("você escolhe ajudá-los e parte para cima dos inimigos mais próximos.")
        lib.Combate(Heroi,lib.GetMonstro(monstros, "Bandido"))
        input("[enter]")
        lib.Combate(Heroi,lib.GetMonstro(monstros, "Bandido Atirador"))
        print("[Narrador]: Ao olhar em volta, percebe-se que todos os guardas pereceram em batalha, levando consigo seus adversários.")
        print("[Narrador]: Os únicos restantes são o líder da caravana e os mercadores. Nesse momento, o líder se aproxima de você, agradece seus grandes feitos e te presenteia com um elixir revigorante.")
        Heroi.MP = Heroi.MPmax
        print("[Aviso]: Seus pontos de mana foram restaurados")        
    elif(int(resp) == 3):
        print("[Narrador]: Já está anoitecendo e a fome volta a te assombrar, olhando à volta, você percebe uma fogueira ao longe.")
        print("[Narrador]: Após se aproximar, percebe que há um ensopado sendo cozido, sem ninguém por perto, você se aproxima do caldeirão e escuta um zumbido.")
        input("[enter]")
        print("[Narrador]: Por puro reflexo, você desvia de uma flecha, e em sua direção vem o Orc o qual atirou.")
        lib.Combate(Heroi,lib.GetMonstro(monstros, "Orc Besteiro"))
        print("[Narrador]: Olhando o corpo à sua frente, você decide que comerá carne de orc nos próximos dias.")
        input("[enter]")
        print("[Narrador]: Alguns dias depois, você encontra a mesma caravana que encontrara anteriormente, eles parecem em apuros, lutando com um grupo de ladrões")
        print("você decide ficar de fora da ação, e acaba presenciando uma chacina, de onde ninguém saíra vivo.")
        input("[enter]")
        print("[Narrador]: No meio dos corpos, estava o cadáver do líder da caravana.")
        print("[Narrador]: Você vasculha o corpo e encontra um elixir, após tomá-lo, se sente revigorado.")
        Heroi.MP = Heroi.MPmax
        print("[Aviso]: Seus pontos de mana foram restaurados.")
        CapituloFloripaMago(Heroi)

def CapituloFloripaMago(Heroi):
    sys.exit()
    
def IntroGuerreiro(Heroi):
    print("")

def IntroLegolas(Heroi):
    print("")
