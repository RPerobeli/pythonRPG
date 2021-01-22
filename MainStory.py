#-*- coding: utf-8 -*-
import sys
import classes
import libMain as lib
import Historias

###############INTRODUCAO ###############################################################################
classesDisponiveis = ("Guerreiro", "Arqueiro", "Mago")
print("Bem vindo ao D&D da Deepweb, aqui você vai encontrar diversas aventuras(nem todas vão ser divertidas).")
nome = input("Digite o nome do seu personagem: ")
print("Perfeito, "+nome+", agora escolha a classe com a qual voce vai se foder!")
print("As classes disponíveis são: "+ str(classesDisponiveis) + ".")
classe = input("E então, qual será a sua?")
while(lib.ConfereClasses(classesDisponiveis, classe)==False):
    classe = input("Classe invalida, digite novamente:")

print("Beleza, então você se chama "+nome+ " e é um "+classe+".")
Heroi = classes.Personagem(nome, classe)

print("status de "+str(Heroi.name)+": "+ str(Heroi.skills))

resp = input("Deseja iniciar sua jornada? (s/n)")
if(resp == "n"):
    sys.exit()
###############INICIO DA HISTORIA###############################################################################
for i in range(0,20):
    print(".")

#começa a contar a historia
monstros = lib.CriaMonstros()
print("[Narrador]")
print("Você acorda pela manha, com uma roupa cheia de lama e a cachorra na cama, qual é a primeira coisa a fazer?")
print("1 - Você acaricia a cachorra.")
print("2 - Você dá um tapa na cachorra.")
print("3 - Imediatamente rola para o lado e saca sua espada e se prepara para matá-la")
resp = input()
if(int(resp) == 1):
    print("Ao acarariciar a cachorra, ela põe os dentes à mostra e morde sua mão, revelando ser um cão infernal.")
    print("Você rola para o lado e saca a sua arma.")
    Heroi.HP -= 2
    lib.Combate(Heroi,lib.GetMonstro(monstros, "Cao infernal"))
    print(Heroi.HP)
    print("Após a luta com o cão dos demônios, você desce as escadas em direção à taverna.")
elif(int(resp) == 2):
    print("A cachorra vazou,e deixou um cheiro infernal na cama...")
    print("Aparentemente, você não curte cachorras, então se levanta, mexe com as piranhas no aquário do corredor da hospedaria, e se digire à taverna.")

elif(int(resp) == 3):
    print("A cachorra mostra sua verdadeira face, com os dentes à mostra, percebe-se que é um cão infernal que se prepara para combate!")
    lib.Combate(Heroi,lib.GetMonstro(monstros, "Cao infernal"))
    print("Após a luta com o cão dos demônios, você desce as escadas em direção à taverna.")

    





